$(document).ready(function(){

    $('#select-baodientu-repository').change(function(){
        $('#select-tag option').remove();
        $.ajax('/ajax/tag/get_by_source/' + this.value, {
              success: function(data) {

                $.each(data, function(index, item){
                    $('#select-tag').append('<option value="'+ item._id +'">' + item.name  + ' ('+item.count+')'+ '</option>');
                });

                $('#select-tag').selectpicker('refresh');
              },
              error: function() {
                 console.log('ERROR: GET TAG BY SOURCE');
              }
           });

    }).change();

    $('.lv-body').on('click', '#filter-timing', function(){
        var sourceid = $(this).attr('sourceid');
        var timingid = $(this).attr('timingid');
        var page = $(this).attr('page');


          $.ajax('/ajax/content/filter_by_ptiming/' + sourceid + '/' + timingid + '/' + page, {
              success: function(data) {

                $('.table-responsive').html(data);

              },
              error: function() {
                 console.log('ERROR: GET CONTENT');
              }
           });
    });

});

function init_repository(){

      $.ajax('/ajax/content/list_by_default', {
          success: function(data) {

            $('.table-responsive').html(data);

          },
          error: function() {
             console.log('ERROR: GET CONTENT');
          }
       });
}

function pagination_ajax(obj){

    var sourceid = $(obj).attr('sourceid');
    var timingid = $(obj).attr('timingid');
    var page = $(obj).attr('page');


      $.ajax('/ajax/content/filter_by_ptiming/' + sourceid + '/' + timingid + '/' + page, {
          success: function(data) {

            $('.table-responsive').html(data);

          },
          error: function() {
             console.log('ERROR: GET CONTENT');
          }
       });
}

function pagination_ajax_content_default(obj){


    var page = $(obj).attr('page');


      $.ajax('/ajax/content/list_by_default/' + page, {
          success: function(data) {

            $('.table-responsive').html(data);

          },
          error: function() {
             console.log('ERROR: GET CONTENT');
          }
       });
}