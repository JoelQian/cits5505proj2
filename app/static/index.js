$(document).ready(function(){
    $(window).scroll(function(){
        if($(this).scrollTop() > 0){
            $('header').addClass('shadow'); 
        } else {
            $('header').removeClass('shadow'); 
        }
    });
});