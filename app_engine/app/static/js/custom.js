

$(window).scroll(function(event){
    
    $('nav').removeClass('nav-hide');
});

$(window).scroll(function() {
    if ($(this).scrollTop() == 0) {
        
        $('nav').addClass('nav-hide');
    }
});
