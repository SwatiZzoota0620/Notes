function changeDivBG() {
    var navBar = document.getElementById('navBG');
    var navBarUL = document.getElementById('navUL');
    var scrollValue = window.scrollY;
    var tous = document.getElementById('tours');
    if (scrollValue > 600 && scrollValue<650) {
        navBar.classList.add('navbar-BG1');
        navBarUL.classList.add('navbar-BG1');
    }
    else if(scrollValue>650 && scrollValue<700){
        navBar.classList.remove('navbar-BG');
        navBarUL.classList.remove('navbar-BG');
        navBar.classList.add('navbar-BG2');
        navBarUL.classList.add('navbar-BG2');
    }
    else if(scrollValue>700 && scrollValue<750){
        navBar.classList.remove('navbar-BG2');
        navBarUL.classList.remove('navbar-BG2');
        navBar.classList.add('navbar-BG3');
        navBarUL.classList.add('navbar-BG3');
    }
    else if(scrollValue>750){
        navBar.classList.remove('navbar-BG3');
        navBarUL.classList.remove('navbar-BG3');
        navBar.classList.add('navbar-BG4');
        navBarUL.classList.add('navbar-BG4');
    }
    else {
        navBar.classList.remove('navbar-BG1');
        navBar.classList.remove('navbar-BG2');
        navBar.classList.remove('navbar-BG3');
        navBar.classList.remove('navbar-BG4');
        navBarUL.classList.remove('navbar-BG1');
        navBarUL.classList.remove('navbar-BG2');
        navBarUL.classList.remove('navbar-BG3');
        navBarUL.classList.remove('navbar-BG4');
        
    }
}

window.addEventListener('scroll', changeDivBG);