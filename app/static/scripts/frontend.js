$(document).ready(function () {

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
                console.log('ERROR: GET CONTENT');
            }
        });
    });

    $('.menu-tree-link').on('click', function () {
        var sourceid = $(this).attr('sourceid');
        var timingid = $(this).attr('timingid');
        var page = $(this).attr('page');


        $.ajax('/repository/filter-by-timing/' + sourceid + '/' + timingid + '/' + page, {
            success: function (data) {
                  $('.midle-content').html(data);

            },
            error: function () {
                console.log('ERROR: GET CONTENT');
            }
        });
    });

    $('#btn-search').click(function () {
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

        var url = '/ajax/content/search/' + source + '/' + tag + '/' + published + '/' + kw + '/1';
        $.ajax(encodeURI(url), {
            success: function (data) {

                $('.table-responsive').html(data);

            },
            error: function () {
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
            console.log('ERROR: GET CONTENT');
        }
    });
}