document.addEventListener("DOMContentLoaded", function(){
    window.addEventListener('scroll', function() {
        // document.getElementById("bannerr").style.height = "auto";
        if (window.scrollY > 747 && window.scrollY > 1056) {
          document.getElementById('navbar_top').classList.add('fixed-top');
          // add padding top to show content behind navbar
          navbar_height = document.querySelector('.navbar').offsetHeight;
          document.body.style.paddingTop = navbar_height + 'px';
          document.getElementById("navbar_top").style.backgroundColor = "#f8f9fa";
          document.getElementById("pro-btn").style.backgroundColor = "#ff6a00";
          document.getElementById("pro-btn").style.color = "#fff";
          document.getElementById("pro-icon").style.color = "#fff";
          document.getElementById("navbar_top").style.boxShadow = "0 4px 8px 0 rgb(0 0 0 / 20%), 0 6px 20px 0 rgb(0 0 0 / 19%)";
        } else {
          document.getElementById('navbar_top').classList.remove('fixed-top');
           // remove padding top from body
          document.body.style.paddingTop = '0';
          document.getElementById("navbar_top").style.backgroundColor = 'transparent';
          document.getElementById("navbar_top").style.boxShadow = "0 0px 0px 0";
          document.getElementById("pro-btn").style.backgroundColor = "#fff";
          document.getElementById("pro-btn").style.color = "#ff6a00";
          document.getElementById("pro-icon").style.color = "#ff6a00";
        } 
    });
  }); 
  // DOMContentLoaded  end

  document.addEventListener("DOMContentLoaded", function(){
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
          document.getElementById('navs').classList.add('fixed-top');
          // add padding top to show content behind navbar
          navbar_height = document.querySelector('.navbar').offsetHeight;
          document.body.style.paddingTop = navbar_height + 'px';
          document.getElementById("navs").style.boxShadow = "0 4px 8px 0 rgb(0 0 0 / 20%), 0 6px 20px 0 rgb(0 0 0 / 19%)";
        } else {
          document.getElementById('navs').classList.remove('fixed-top');
           // remove padding top from body
          document.body.style.paddingTop = '0';
          document.getElementById("navs").style.boxShadow = "0 0px 0px 0";
        } 
    });
  }); 
  // DOMContentLoaded  end
  