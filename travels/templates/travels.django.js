FULL_BASE_URL = '{{ FULL_BASE_URL }}';
BASE_URL = '{{ BASE_URL }}';
MEDIA_URL = '{{ MEDIA_URL }}';
STATIC_URL = '{{ STATIC_URL }}';

APP_NAME = '{{ APP_NAME }}';
PROJECT_DESCRIPTION = '{{ PROJECT_DESCRIPTION }}';

FLOWPLAYER_SWF = '{{ FLOWPLAYER_SWF }}'

ITINERARY_API_URL = '{% url "itinerary_api" %}';
CAST_API_URL = '{% url "cast_api" %}';
EVENT_API_URL = '{% url "event_api" %}';
USER_API_URL = '{% url "user_api" %}';

FEATURES_API_URL = '{% url "geofeatures_api" %}'

SEARCH_API_URL = '{% url "search_api" %}';

MAP_DEFAULTS = {
    zoom: {{DEFAULT_ZOOM}},
    zoomOffset: {{ZOOM_OFFSET}},
    center: [{{ project_settings.location.x }}, {{ project_settings.location.y }}],
}

MAP_BOUNDRY = {{boundry|safe}};

// this is set right above the close body tag. Used for UI login prompt only.
TRAVELS_USER = null;

// taken from:
// http://tobiascohen.com/files/stackoverflow/jquery-form-serializeObject.html
$.fn.serializeObject = function()
{
    var o = {};
    var a = this.serializeArray();
    $.each(a, function() {
        if (o[this.name]) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return o;
};

// taken from:
// http://ozanakcora.com/urlize/
$.fn.urlize = function(base) {
    var x = this.html();
    list = x.match( /\b(http:\/\/|www\.|http:\/\/www\.)[^ ]{2,100}\b/g );
    if ( list ) {
        for ( i = 0; i < list.length; i++ ) {
            x = x.replace( list[i], "<a target='_blank' href='" + base + list[i] + "'>"+ list[i] + "</a>" );
        }
        this.html(x);
    }
};

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    dataType: 'json',
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

function update_auth_redirects() {
    var next = get_next();
    $('#logout-link').attr('href', '{% url "logout"%}?next=' + next);
    $('#login-form input[name$="next"]').val(next);
}

function get_next() {
    return BASE_URL + '/' + location.hash;
}

// var templates is defined in templates.js

function translate_template(templ) {
    var list = templ.match( /gettext\('.+'\)/g );

    if ( list ) {
        for ( var i = 0; i < list.length; i++ ) {
            templ = templ.replace(list[i], eval(list[i]+';'));
        }
    }
    return templ;
};

for ( i in templates ) { templates[i] = translate_template(templates[i]); }

function render_to_string(templ, context) {
    return Mustache.to_html(templates[templ], context);
}

function form_to_json(form_jq) {
    var obj = form_jq.serializeObject();
    return JSON.stringify(obj, null, 2);
}

function format_date(jq_obj, pretty) {
    var format = 'M d, yy';

    // force pretty. auto pretties anything up to a month old.
    if ( pretty ) {
        jq_obj.prettyDate(format);
    }

    else {
        jq_obj.each(function() {
            var _this = $(this);
            var date = new Date(_this.html());
            var res = $.datepicker.formatDate(format, date);
            _this.html(res);
        });
    }
}

function mapValue(value, istart, istop, ostart, ostop) {
       return ostart + (ostop - ostart) * ((value - istart) / (istop - istart));
}

function is_same_day(rawstr1, rawstr2){
     var date1 = new Date((rawstr1 || "").replace(/-/g,"/").replace(/[TZ]/g," "));
     var date2 = new Date((rawstr2 || "").replace(/-/g,"/").replace(/[TZ]/g," "));

     if ( date1.getDate() == date2.getDate() &&
          date1.getMonth() == date2.getMonth() &&
          date1.getYear() == date2.getYear() ) {
        return true;
     }

    return false;
}

