var PAGE_DETAIL = 2;
var PAGE_FILTER_DEFAULT = 0;
var PAGE_FILTER_BY_TIMING = 1;
var PAGE_SEARCH = 3;
var scroll_position = 0;
var POSITION_TO_SCROLL_TO = 204;
var isLeftMenuTreeDisplay = false;
var MOBILE_WIDTH = 840;
var MOBILE_SCROLL_POSITION = 350;
var mobile_check = false;
var tablet_check = false;
var is_navigationbar_opened = false;
$(document).ready(function () {
    window.mobilecheck = function () {
        (function (a) {
            if (/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i.test(a) || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0, 4))) mobile_check = true;
        })(navigator.userAgent || navigator.vendor || window.opera);
        return mobile_check;
    };
    window.mobileAndTabletcheck = function () {
        (function (a) {
            if (/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino|android|ipad|playbook|silk/i.test(a) || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0, 4))) tablet_check = true;
        })(navigator.userAgent || navigator.vendor || window.opera);
        return tablet_check;
    };
    mobile_check = window.mobilecheck;
    tablet_check = window.mobileAndTabletcheck;
    if (mobile_check == true || tablet_check == true) {
        MOBILE_WIDTH = 840;
    } else {
        MOBILE_WIDTH = 823;
    }
    resize_for_mobile();
    $('#btn_collapsed').on('click', function () {
        if (is_navigationbar_opened == false) {
            $('#defaultNavbar1').css({background: '#134e70'});
            is_navigationbar_opened = true;
        } else {
            $('#defaultNavbar1').css({background: 'transparent'});
            is_navigationbar_opened = false;
        }
    });
    $('#btn_slide_right').on('click', function () {
        if (isLeftMenuTreeDisplay == false) {
            open_left_menu_tree();
        } else {
            close_left_menu_tree(0);
        }
    });
    $('.open_popup').on('click', function () {
        var index = $(this).attr('index');
        resize_iframe(index);
    });
    reset_leftMenuTree_height();
    $(window).resize(function () {
        if ($(window).width() >= 750) {
            $('#defaultNavbar1').css({background: 'transparent'});
        } else {
            $('#defaultNavbar1').css({background: '#134e70'});
        }
        if ($(window).width() > MOBILE_WIDTH) {
            var windowHeight = $(window).height();
            if (scroll_position >= POSITION_TO_SCROLL_TO) {
                $('#left-menu-tree').css({height: windowHeight});
            } else {
                reset_leftMenuTree_height();
            }
            // if (isLeftMenuTreeDisplay == true) {
            //     close_left_menu_tree(1);
            // }
            fast_close_leftmenutree();
        }
        resize_for_mobile();
    });

    $('#left-menu-tree').bind('mousewheel DOMMouseScroll', function (e) {
        var scrollTo = null;

        if (e.type == 'mousewheel') {
            scrollTo = (e.originalEvent.wheelDelta * -1);
        }
        else if (e.type == 'DOMMouseScroll') {
            scrollTo = 40 * e.originalEvent.detail;
        }

        if (scrollTo) {
            e.preventDefault();
            $(this).scrollTop(scrollTo + $(this).scrollTop());
        }
    });
    var windowHeight = $(window).height() - $('#footer').height();
    $(window).scroll(function () {
        scroll_position = $(window).scrollTop();
        if ($(window).width() > MOBILE_WIDTH) {
            if (scroll_position >= POSITION_TO_SCROLL_TO) {

                var height = 0;
                if (isFooterViewOnScreen()) {
                    height = $(window).height() - $('#footer').height() - 5;
                } else {
                    height = $(window).height();
                }
                $('#left-menu-tree').css({
                    position: 'fixed',
                    top: 0,
                    z_index: -1,
                    height: height
                });
            } else {
                $('#left-menu-tree').css({position: 'relative'});
                reset_leftMenuTree_height();
            }
        } else {
            if ($(window).scrollTop() >= MOBILE_SCROLL_POSITION) {
                $('#btn_slide_right').css({display: 'block'});
            } else {
                $('#btn_slide_right').css({display: 'none'});
                if (isLeftMenuTreeDisplay) {
                    close_left_menu_tree(1);
                }
            }
        }
    });
    $('#select-baodientu-repository').change(function () {
        $('#select-tag option').remove();
        $.ajax('/ajax/tag/get_by_source/' + this.value, {
            success: function (data) {
                $('#select-tag').append('<option value="*">' + 'Tất cả' + '</option>');
                $.each(data, function (index, item) {
                    var savedid = $('#lbl_tag').text();
                    var item_id = item._id;
                    if (savedid == item_id) {
                        $('#select-tag').append('<option value="' + item._id
                            + '"selected>' + item.name + ' ('
                            + item.count + ')' + '</option>');
                    }
                    else {
                        $('#select-tag').append('<option value="' + item._id
                            + '">' + item.name + ' (' + item.count + ')' + '</option>');
                    }
                });

                //  $('#select-tag').selectpicker('refresh');
            },
            error: function () {
                display_error_mesage();
                console.log('ERROR: GET TAG BY SOURCE');
            }
        });

    }).change();

    // $('.lv-body').on('click', '#filter-timing', function () {
    //     var sourceid = $(this).attr('sourceid');
    //     var timingid = $(this).attr('timingid');
    //     var page = $(this).attr('page');
    //
    //
    //     $.ajax('/ajax/content/filter_by_ptiming/' + sourceid + '/' + timingid + '/' + page, {
    //         success: function (data) {
    //
    //             $('.table-responsive').html(data);
    //
    //         },
    //         error: function () {
    //             display_error_mesage();
    //             console.log('ERROR: GET CONTENT');
    //         }
    //     });
    // });

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
    var savedDate = $('#lbl_published').text();
    if (savedDate != null && savedDate != "" && savedDate != "*") {
        savedDate = convertFormatDate(savedDate);
        $('#txt-date-from-picker').val(savedDate);
    }
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
    $('.midle-content').css("visibility", "hidden");
    $('.busy_mark').css("display", "block");
}

function hide_busy_mark() {
    $('.error_message').css("display", "none");
    $('.midle-content').css("visibility", "visible");
    $('.busy_mark').css("display", "none");
}

function display_error_mesage() {
    $('.midle-content').css("visibility", "hidden");
    $('.error_message').css("display", "block");
    $('.busy_mark').css("display", "none");
}

function hide_error_message() {
    $('.midle-content').css("visibility", "visible");
    $('.error_message').css("display", "none");
}

function scroll_to_top() {
    if (scroll_position >= POSITION_TO_SCROLL_TO) {
        $('html,body').animate({scrollTop: POSITION_TO_SCROLL_TO}, 1000);
        return false;
    }
    return true;
}

function reset_leftMenuTree_height() {
    var elementOffset = $('#left-menu-tree').offset().top;
    var apply_height = $(window).height() - Math.abs(($(window).scrollTop() - elementOffset));
    $('#left-menu-tree').css({height: apply_height});
}

function isFooterViewOnScreen() {
    var docViewTop = $(window).scrollTop();
    var docViewBottom = docViewTop + $(window).height();

    var elemTop = $('.footer').offset().top;
    var elemBottom = elemTop + $('.footer').height();

    return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
}

function resize_iframe(index) {
    $('#modalDefault' + index).css({display: "block"});
    document.getElementById("iframe_" + index)
        .style.height = document.getElementById("iframe_" + index)
            .contentWindow.document.body.scrollHeight + 'px';
}

function convertFormatDate(date) {
    var returnDate = date.split("-");
    var year = returnDate[0];
    var month = returnDate[1];
    var day = returnDate[2];
    date = day + "/" + month + "/" + year;
    return date;
}

function resize_for_mobile() {
    var horizontalMenubar_height = $('#horizontal-menubar').height();
    if ($(window).width() <= MOBILE_WIDTH) {
        $('#admin-area').css({height: horizontalMenubar_height});
        $('#btn-search').appendTo('#horizontal-menubar-date');
        $('#btn-search').css("margin-top", 2 + "px");
        $('#btn-search').css("margin-bottom", 1 + "px");
        var leftMenuTreeWidth = $('#left-menu-tree').width();
        if (isLeftMenuTreeDisplay == false) {
            var h = $(window).height();
            $('#left-menu-tree').css({position: 'fixed', left: -leftMenuTreeWidth, height: h});
            var slide_right_top = ($('#left-menu-tree').height / 2) - ($('#btn_slide_right').height() / 2);
            $('#btn_slide_right').css({top: slide_right_top});
        }
        $('.midle-content').css({float: 'left', width: 100 + '%'});
    } else {
        $('#admin-area').css({height: horizontalMenubar_height});
        $('#btn-search').appendTo('#horizontal-menubar-column3');
        $('#btn-search').css("margin-top", 20 + "%");
        $('.midle-content').css({float: 'right', width: 77 + '%'});
        if (scroll_position >= POSITION_TO_SCROLL_TO) {
            $('#left-menu-tree').css({position: 'fixed', left: 0, top: 0});
        } else {
            $('#left-menu-tree').css({position: 'relative', left: 0});
        }
    }
}

function open_left_menu_tree() {
    $('#open_menutree').css({display: 'none'});
    $('#close_menutree').css({display: 'block'});
    var destination = $('#left-menu-tree').width();
    $('#left-menu-tree').animate({
        left: "+=" + destination + "px",
    }, 1000);
    $('#left-menu-tree').css({top: 0});
    $('#btn_slide_right').animate({
        left: "+=" + destination + "px",
    }, 1000);
    isLeftMenuTreeDisplay = true;
    var h = $(window).height();
    $('#left-menu-tree').css({height: h, top: 5});
}

function close_left_menu_tree(speed) {
    $('#open_menutree').css({display: 'block'});
    $('#close_menutree').css({display: 'none'});
    var destination = $('#left-menu-tree').width();
    if (speed == 0) {
        $('#left-menu-tree').animate({
            left: "-=" + destination + "px",
        }, 1000);
        $('#btn_slide_right').animate({
            left: "-=" + destination + "px",
        }, 1000);
    } else {
        $('#left-menu-tree').animate({
            left: "-=" + destination + "px",
        }, 1);
        $('#btn_slide_right').animate({
            left: "-=" + destination + "px",
        }, 1);
    }
    isLeftMenuTreeDisplay = false;
}
function fast_close_leftmenutree() {
    isLeftMenuTreeDisplay = false;
    $('#btn_slide_right').css({display: 'none', left: -1});
    $('#open_menutree').css({display: 'block'});
    $('#close_menutree').css({display: 'none'});
}
