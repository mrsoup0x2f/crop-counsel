let menuIcon = document.querySelector('#menu-icon') ;
let navbar = document.querySelector('.navbar');
menuIcon.onclick = () => {
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');
};

let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');
window.onscroll = () => {
    sections.forEach(sec =>  {
        let top = window.scrollY;
        let offset = sec.offsetTop - 150;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if(top >= offset && top < offset+height) {
            navLinks.forEach(links => {
                links.classList.remove('active');
                document.querySelector('header nav a[href*=' + id + ']').classList.add('active');
            });
        };
    });
    

    // Remove toggle icon and navbar when click navbar link

    menuIcon.classList.remove('bx-x');
    navbar.classList.remove('active');
};

// Swiper JS
var swiper = new Swiper('.slide-content', {
    slidesPerView: 3,   
    spaceBetween: 30,
    slidesPerGroup: 3,
    centerSlide: true,
    fade: true,
    loop: false,
    loopFillGroupWithBlank: true,
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
      dynamicBullets: true,
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },

    breakpoints: {
        0 : {
            slidesPerView: 1,
        },
        540 : {
            slidesPerView: 2,
        },
        950 : {
            slidesPerView: 3,
        },
    }

});


const hamburger = document.getElementById("hamburger");
const navList = document.getElementById("navbar");

hamburger.addEventListener('click', () => {
    navList.classList.toggle('show');
});


let loginBtn = document.getElementById('loginBtn');
loginBtn.addEventListener('click', function() {

        if (loginBtn.textContent === 'Login') {
            loginBtn.textContent = 'Logout';
            window.location.href = 'http://localhost/login-register/index.php';
            
        } else {
            loginBtn.textContent = 'Login';
            window.location.href = 'http://localhost/login-register/login.php';
        }
    }
);

const isLoggedIn = false;
function handleToggle(event) {

    event.preventDefault();

    if(isLoggedIn) {
        loginBtn.innerHTML = "Logout";
        isLoggedIn = false;

    } else {
        loginBtn.innerHTML = "Login";
        isLoggedIn = true;
    }
}