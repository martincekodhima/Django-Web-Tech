$(document).ready(function () {
    // declare a search-term variable
    var searchTerm;
    // we use tick so that the browser knows that its a different image
    var tick = 0;
    // for formatting reasons 
    var page = 0;
    
    // onclick of the search in the menu toggle the search bar
    $("#search-navigation").click(function () {
        // if the window is not at the top scroll to the top
        if($(window).scrollTop() != 0) {
            // animate the scrolling up
            $("html,body").animate({ scrollTop: 0 }, "slow");
        }
        // fade in or out the search bar
        $("#search-dropdown").fadeToggle("slow", "easeOutSine", function() {
            // focus the text area
            $("#search").focus();
        });
    });
    
    // for searching in mobile view
    $("#search-navigation-mobile").click(function() {
        // close side nav
        $(".button-collapse").sideNav("hide");
        // if the window is not at the top scroll to the top
        if($(window).scrollTop() != 0) {
            // animate the scrolling up
            $("html,body").animate({ scrollTop: 0 }, "slow");
        }
        // fade in or out the search bar
        $("#search-dropdown").fadeToggle("slow", "easeOutSine", function() {
            // focus the text area
            $("#search").focus();
        });
    });
    
    // if enter is pressed while the search bar is active reset the screen and display images
    $('#search').keypress(function (e) {
      if (e.which == 13) {
          // togge the dropdown search
          $("#search-dropdown").fadeToggle("fast", "easeOutSine");
          // pass the keyword so function
          searchTerm = $("#search").val();
          searchTerm = searchTerm.split(/[ ,]+/).filter(function(v){return v!==''}).join(',')
          // redirect 
          window.location.href = "/search/"+searchTerm;
      }
    });
    
    // when the x is pressed on the bar clean input
    $("#close-search").click(function() {
        $("#search").val(""); 
        $("#search").focus();
    });
    
    // start side nav
    $(".button-collapse").sideNav();
    
    // start collapsable in front page
    $('.collapsible').collapsible();
    
    // init the light gallery
    $('.cards-container').lightGallery({
        selector: '.card-image',
        zoom: true,
        download: true
    });
    
    // for the dropdown
    $(".dropdown-button").dropdown();
    
});