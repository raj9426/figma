const menuBtn = document.querySelector('.menu-btn');
const menu = document.querySelector('.ul');
let menuOpen = false;
menuBtn.addEventListener('click', () => {
    if(!menuOpen) {
        menuBtn.classList.add('open');
        menu.classList.add('menu');
        menuOpen = true;
    }else{
        menuBtn.classList.remove('open');
        menu.classList.remove('menu');
        menuOpen = false;
    }
} )

// const navSlide = () => {
//     const burger = document.querySelector('.menu-btn');
//     const nav = document.querySelector('.nav-sidebarToggle');
//     burger.addEventListener('click', () => {
//         nav.classList.toggle('nav-active');
//         });
    
//     }

// navSlide();