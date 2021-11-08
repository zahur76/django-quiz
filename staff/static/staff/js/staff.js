$(document).ready(function(){

   $(".results-additional-info").hide();
   $(".hide").hide();

   $(".show-more").click(function(){
        $(".results-additional-info").show();
        $(".show-more").hide();
        $(".hide").show();
   })

   $(".hide").click(function(){
    $(".results-additional-info").show();
    $(".show-more").show();
    $(".hide").hide();
    $(".results-additional-info").hide();
})

});