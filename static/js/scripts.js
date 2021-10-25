$(document).ready(function() {
    //Preloader
    $(window).on("load", function() {
    let preloaderFadeOutTime = 1000;
    function hidePreloader() {
    var preloader = $('.spinner-wrapper');
    preloader.fadeOut(preloaderFadeOutTime);
    }
    hidePreloader();
    });
    });
    
    /* Set the width of the side navigation to 250px and the left margin of the page content to 250px and add a black background color to body */
    function openNav() {
      document.getElementById("mySidenav").style.width = "250px";
      document.body.style.marginLeft = "250px";
      document.body.style.marginRight = "-250px";
      document.getElementById("opacitified").style.opacity = "0.3";
      document.getElementById("opacitified").style.transition = "1s";
        document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
    }
    
    /* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
    function closeNav() {
      document.getElementById("mySidenav").style.width = "0";
      document.body.style.marginLeft = "0px";
      document.body.style.marginRight = "0px";
      document.getElementById("opacitified").style.transition = "1s";
      document.getElementById("opacitified").style.opacity = "1";
      document.body.style.backgroundColor = "#EBF6F6";
    }
    
    function mySearch() {
      // Declare variables
      var input, filter, ul, li, a, i, txtValue;
      input = document.getElementById('myInput');
      filter = input.value.toUpperCase();
      ul = document.getElementById("myUL");
      li = ul.getElementsByTagName('li');
    
      // Loop through all list items, and hide those who don't match the search query
      for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          li[i].style.display = "";
        } else {
          li[i].style.display = "none";
        }
      }
    }
    