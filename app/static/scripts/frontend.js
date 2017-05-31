var PAGE_DETAIL = 2;
var PAGE_FILTER_DEFAULT = 0;
var PAGE_FILTER_BY_TIMING = 1;
var PAGE_SEARCH = 3;
var scroll_position = 0;
var POSITION_TO_SCROLL_TO = 204;
$(document).ready(function () {
    $(window).scroll(function () {
        scroll_position = $(window).scrollTop();
    })
    $('#select-baodientu-repository').change(function () {
        $('#select-tag option').remove();
        $.ajax('/ajax/tag/get_by_source/' + this.value, {
            success: function (data) {

                $.each(data, function (index, item) {
                    $('#select-tag').append('<option value="' + item._id + '">' + item.name + ' (' + item.count + ')' + '</option>');
                });

                $('#select-tag').selectpicker('refresh');
            },
            error: function () {
                display_error_mesage();
                console.log('ERROR: GET TAG BY SOURCE');
            }
        });

    }).change();

    $('.lv-body').on('click', '#filter-timing', function () {
        var sourceid = $(this).attr('sourceid');
        var timingid = $(this).attr('timingid');
        var page = $(this).attr('page');


        $.ajax('/ajax/content/filter_by_ptiming/' + sourceid + '/' + timingid + '/' + page, {
            success: function (data) {

                $('.table-responsive').html(data);

            },
            error: function () {
                display_error_mesage();
                console.log('ERROR: GET CONTENT');
            }
        });
    });

    $('.menu-tree-link').on('click', function () {
        display_busy_mark();
        var sourceid = $(this).attr('sourceid');
        var timingid = $(this).attr('timingid');
        var page = $(this).attr('page');
        var pageid = $(this).attr('pageid');
        if (pageid == PAGE_FILTER_DEFAULT || pageid == PAGE_FILTER_BY_TIMING || pageid == PAGE_SEARCH) {
            $.ajax('/repository/filter-by-timing/' + sourceid + '/' + timingid + '/' + page + '/' + pageid, {
                success: function (data) {
                    hide_busy_mark();
                    $('.midle-content').html(data);
                    return scroll_to_top();
                },
                error: function () {
                    display_error_mesage();
                    console.log('ERROR: GET CONTENT');
                }
            });
        } else {
            $(location).attr('href', '/repository/filter-by-timing/' + sourceid + '/' + timingid + '/' + page + '/' + pageid);
        }

    });

    $('#show_iframe').on('click', function () {
        display_busy_mark();
        var cid = $(this).attr('cid');
        var idx = $(this).attr('idx');
        $.ajax('/repository/detail-iframe/' + cid + '/' + idx, {
            success: function (data) {
                hide_busy_mark();
                $('.midle-content').html(data);
            },
            error: function () {
                display_error_mesage();
                console.log('ERROR: GET CONTENT');
            }
        });
    });


    $('#btn-search').click(function () {
        display_busy_mark();
        var source = $('#select-baodientu-repository').val();
        var tag = $('#select-tag').val();
        var kw = $('#txt-search').val();
        var published = $('#txt-date-from-picker').val();

        if (!kw) {
            kw = "*";
        }

        if (!published) {
            published = "*";
        }

        var newchar = '-'
        published = published.split('/').join(newchar);

        var url = '/repository/search/' + source + '/' + tag + '/' + published + '/' + kw + '/1';
        $.ajax(encodeURI(url), {
            success: function (data) {
                hide_busy_mark();
                $('.midle-content').css("display", "block");
                $('.midle-content').html(data);

            },
            error: function () {
                display_error_mesage();
                console.log('ERROR: GET CONTENT');
            }
        });
    });

});

function init_repository() {

    $.ajax('/ajax/content/list_by_default', {
        success: function (data) {

            $('.table-responsive').html(data);

        },
        error: function () {
            display_error_mesage();
            console.log('ERROR: GET CONTENT');
        }
    });
}

function pagination_ajax(obj) {

    var sourceid = $(obj).attr('sourceid');
    var timingid = $(obj).attr('timingid');
    var page = $(obj).attr('page');

    $('.table-responsive').html('Xin đợi trong giây lát ...');
    $.ajax('/ajax/content/filter_by_ptiming/' + sourceid + '/' + timingid + '/' + page, {
        success: function (data) {

            $('.table-responsive').html(data);

        },
        error: function () {
            display_error_mesage();
            console.log('ERROR: GET CONTENT');
        }
    });
}

function pagination_ajax_v2(obj) {
    display_busy_mark();
    var sourceid = $(obj).attr('sourceid');
    var timingid = $(obj).attr('timingid');
    var page = $(obj).attr('page');

    $('.midle-content').html('Xin đợi trong giây lát ...');
    $.ajax('/repository/filter-by-timing/' + sourceid + '/' + timingid + '/' + page, {
        success: function (data) {
            hide_busy_mark();
            $('.midle-content').html(data);
            return scroll_to_top();
        },
        error: function () {
            display_error_mesage();
            console.log('ERROR: GET CONTENT');
        }
    });
}

function pagination_ajax_content_default(obj) {


    var page = $(obj).attr('page');

    $('.table-responsive').html('Xin đợi trong giây lát ...');
    $.ajax('/ajax/content/list_by_default/' + page, {
        success: function (data) {

            $('.table-responsive').html(data);

        },
        error: function () {
            display_error_mesage();
            console.log('ERROR: GET CONTENT');
        }
    });
}

function pagination_ajax_content_default_v2(obj) {

    display_busy_mark();
    var page = $(obj).attr('page');

    $.ajax('/repository/' + page, {
        success: function (data) {
            hide_busy_mark();
            $('.midle-content').html(data);
            return scroll_to_top();
        },
        error: function () {
            display_error_mesage();
            console.log('ERROR: GET CONTENT');
        }
    });
}

function pagination_ajax_search_content(obj) {
    var page = $(obj).attr('page');
    var source = $('#select-baodientu-repository').val();
    var tag = $('#select-tag').val();
    var kw = $('#txt-search').val();
    var published = $('#txt-published-date').val();

    if (!kw) {
        kw = "*";
    }

    if (!published) {
        published = "*";
    }

    var newchar = '-'
    published = published.split('/').join(newchar);

    var url = '/ajax/content/search/' + source + '/' + tag + '/' + published + '/' + kw + '/' + page;
    $.ajax(encodeURI(url), {
        success: function (data) {

            $('.table-responsive').html(data);

        },
        error: function () {
            display_error_mesage();
            console.log('ERROR: GET CONTENT');
        }
    });
}


function pagination_ajax_search_content_v2(obj) {
    display_busy_mark();
    var page = $(obj).attr('page');
    var source = $('#select-baodientu-repository').val();
    var tag = $('#select-tag').val();
    var kw = $('#txt-search').val();
    var published = $('#txt-date-from-picker').val();

    if (!kw) {
        kw = "*";
    }

    if (!published) {
        published = "*";
    }

    var newchar = '-'
    published = published.split('/').join(newchar);

    var url = '/repository/search/' + source + '/' + tag + '/' + published + '/' + kw + '/' + page;
    $.ajax(encodeURI(url), {
        success: function (data) {
            hide_busy_mark();
            $('.midle-content').html(data);
            return scroll_to_top();
        },
        error: function () {
            display_error_mesage();
            console.log('ERROR: GET CONTENT');
        }
    });
}

function pagination_ajax_page_version(obj) {
    var page = $(obj).attr('page');
    var totalCount = $(obj).attr('totalcount');
    for (var i = 1; i <= totalCount; i++) {

        if (page == i) {
            $('#menubar_' + i).css("display", "block");
            $('#middle_' + i).css("display", "block");
        } else {
            $('#menubar_' + i).css("display", "none");
            $('#middle_' + i).css("display", "none");
        }
    }
    return scroll_to_top();
}


function display_busy_mark() {
    $('.error_message').css("display", "none");
    $('.midle-content').css("display", "none");
    $('.busy_mark').css("display", "block");
}

function hide_busy_mark() {
    $('.error_message').css("display", "none");
    $('.midle-content').css("display", "block");
    $('.busy_mark').css("display", "none");
}

function display_error_mesage() {
    $('.midle-content').css("display", "none");
    $('.error_message').css("display", "block");
    $('.busy_mark').css("display", "none");
}

function hide_error_message() {
    $('.midle-content').css("display", "block");
    $('.error_message').css("display", "none");
}

function scroll_to_top() {
    if (scroll_position > POSITION_TO_SCROLL_TO) {
        $('html,body').animate({scrollTop: POSITION_TO_SCROLL_TO}, 1000);
        return false;
    }
    return true;
}

