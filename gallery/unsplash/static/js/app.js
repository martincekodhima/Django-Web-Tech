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
          // clean the screen
          cleanScreen();
          // pass the keyword so function
          searchTerm = $("#search").val();
          displayImages(searchTerm,page);
          return false;
      }
    });
    
    // when the x is pressed on the bar clean input
    $("#close-search").click(function() {
        $("#search").val(""); 
        $("#search").focus();
    });
    
    // if the random button is pressed then show random pictures
    $("#random").click(function() {
        if (!$("#random").hasClass("active")) {
            $("#random").addClass("active");
        }
        cleanScreen();
        searchTerm = null;
        displayImages(searchTerm,page);
    });
    // same as above only for mobile also hides side nav
    $("#random-mobile").click(function() {
        if (!$("#random").hasClass("active")) {
            $("#random").addClass("active");
        }
        cleanScreen();
        // close side nav
        $(".button-collapse").sideNav("hide");
        searchTerm = null;
        displayImages(searchTerm,page);
    });
    
    // start side nav
    $(".button-collapse").sideNav();
    
    // start collapsable in front page
    $('.collapsible').collapsible();
    
    // function to clean the screen
    function cleanScreen() {
        // set page number to 0
        page = 0;
        // remove everything in container and append a new row
        $(".container").html("").append('<div class="row"><div class="col s12 cards-container main-content-0" id="page-'+page+'"></div></div>');
    }
    
    // function to display the images
    function displayImages(keyword,page) {
        if (keyword == null) {
            // show random pictures
            for (var i = 0; i < 30; i++) {
                tick++;
                $(".main-content-"+page).append('<div class="card"><div class="card-image waves-effect waves-block waves-light" data-src="https://source.unsplash.com/random?sig='+tick+'"><img class="activator" src="https://source.unsplash.com/random?sig='+tick+'"></div></div>');
            }
        } else {
            // show pictures from a specific keyword
            for (var i = 0; i < 30; i++) {
                tick++;
                $(".main-content-"+page).append('<div class="card"><div class="card-image waves-effect waves-block waves-light" data-src="https://source.unsplash.com/all/random?'+ keyword  +'&sig='+tick+'"><img class="activator" src="https://source.unsplash.com/all/random?'+ keyword  +'&sig='+tick+'"></div></div>');
            }
        }
        // show the show more button at the end
        $(".container").append('</div></div><center id="centerButton"><a class="waves-effect waves-light btn yellow darken-2 grey-text text-darken-4 showMore"><i class="material-icons right">expand_more</i>Show More</a><br><br><br></center>');
        
        // attach listener so if the button is clicked show more pages
        $(".showMore").click(function() {
            // fade and remove the button
            $("#centerButton").fadeToggle("400", "easeOutSine", function() { $(this).remove(); });
            page++;
            // show page number
            $(".container").append('<center><h5 class="darken-2 grey-text text-darken-4">Page '+page+'</h5></center><div class="divider"></div><div class="row"><div class="col s12 cards-container main-content-'+page+'" id="page-'+page+'">');
            // display new images
            displayImages(searchTerm, page);
        });
        
        // init the light gallery
        $('.cards-container').lightGallery({
            selector: '.card-image',
            zoom: true,
            download: false
        });
    }
});