from locast.api import *
from locast.api import qstranslate, exceptions

from django.contrib.gis.geos import Polygon
from django.db.models import Q
from django.views.decorators.cache import cache_page

from locast.api import cache

from travels import cache_control, models
from travels.api.cast import CastAPI
from time import time

import time

def get_geofeatures(request):
    cache_key = _generate_cache_key(request)
    cache_val = cache.get(cache_key, cache_control.GEOFEATURES_CACHE_GROUP)

    if cache_val:
        user_new_casts = get_user_new_casts(request, cache_key)
        add_user_casts(cache_val, user_new_casts)

        return APIResponseOK(content=cache_val)

    bounds_param = get_param(request.GET, 'within')
    query = request.GET.copy()

    if bounds_param:
        pnts = bounds_param.split(',')

        bbox = (float(pnts[0]), float(pnts[1]),
                float(pnts[2]), float(pnts[3]))

        poly = Polygon.from_bbox(bbox)
        poly.set_srid(4326)

        del query['within']

    base_query = Q()
    if bounds_param:
        base_query = base_query & Q(location__within=poly)

    # cast within bounds
    cast_base_query = models.Cast.get_privacy_q(request) & base_query

    q = qstranslate.QueryTranslator(models.Cast, CastAPI.ruleset, cast_base_query)

    try:
        casts = q.filter(query).select_related('author').prefetch_related('media_set').prefetch_related('tags')
    except qstranslate.InvalidParameterException, e:
        raise exceptions.APIBadRequest(e.message)

    cast_arr = []

    for c in casts:
        if c.location:
            s = geojson_serialize(c, c.location, request)
            cast_arr.append(s)

    #event within bounds
    events = models.Event.objects.filter(base_query)

    event_arr = []
    for e in events:
        if e.location:
            event_arr.append(geojson_serialize(e, e.location, request))

    # itinerary intersects bounds
    if bounds_param:
        base_query = Q(path__intersects = poly)

    itins = models.Itinerary.objects.filter(base_query)

    itin_arr = []
    for i in itins:
        if i.path:
            itin_arr.append(geojson_serialize(i, i.path, request))

    features_dict = {}
    features_dict['casts'] = dict(type='FeatureCollection', features=cast_arr)
    features_dict['events'] = dict(type='FeatureCollection', features=event_arr)
    features_dict['itineraries'] = dict(type='FeatureCollection', features=itin_arr)

    cache.set(_generate_cache_key(request), features_dict, cache_control.GEOFEATURES_CACHE_GROUP)

    return APIResponseOK(content=features_dict)

def get_user_new_casts(request, cache_key):
    query = request.GET.copy()

    cache_timestamp = cache_key.split('@')[1]

    cache_time = int(cache_timestamp) * 60 * 10 # last cache generation time

    # FIXME: the cast could appear twice on the map if the user modifies
    # the cast after the cache was created - ie, adding a picture
    # Until the next cache invalidation (up to 10 minutes), the map will
    # show both the old version of the cast and the new one with all the
    # changes. We should look for duplicates when merging user_casts with
    # the cached_casts

    # search only casts modified _after_ the cache creation
    base_query = Q(modified__gte=datetime.fromtimestamp(cache_time))

    cast_base_query = models.Cast.get_privacy_q(request) & base_query

    q = qstranslate.QueryTranslator(models.Cast, CastAPI.ruleset, cast_base_query)

    try:
      casts = q.filter(query).select_related('author').prefetch_related('media_set').prefetch_related('tags')
    except qstranslate.InvalidParameterException, e:
      raise exceptions.APIBadRequest(e.message)

    cast_arr = []

    for c in casts:
      if c.location:
          s = geojson_serialize(c, c.location, request)
          cast_arr.append(s)

    return cast_arr

def add_user_casts(cache_val, user_new_casts):
    cache_val['casts']['features'].extend(user_new_casts)

def _generate_cache_key(request):
    itinerary = "all-casts"
    if 'itinerary' in request.GET:
        itinerary = str(request.GET['itinerary'])
    cache_slot = int(time.time() / (60*10)) # change cache key every ten minutes (60 * 10)
    return str(itinerary) + "@" + str(cache_slot)
