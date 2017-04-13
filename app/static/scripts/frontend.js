$(document).ready(function(){

    $('#select-baodientu-repository').change(function(){
        $('#select-tag option').remove();


        $.ajax('/ajax/tag_get_by_source/' + this.value, {
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

});