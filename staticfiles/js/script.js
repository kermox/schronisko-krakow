// Init AOS module.
AOS.init({
    once: true
});


// Init stickyTabs module.
$(document).ready(function () {
    options = {
        scrollToTab: $(".nav-pills"),
    }
    $('.nav-pills').stickyTabs(options);
})


// Init AnimateNumber module.

$('.count').each(function () {
    $(this).animateNumber(
        {
            number: $(this).text(),
            numberStep: $.animateNumber.numberStepFactories.separator(' ')
        },
        2500
    )
});

// Detect the browser and change background image attachment if its Mobile IOS
let ua = detect.parse(navigator.userAgent)
if (ua.browser.family === 'Mobile Safari') {
    $('.welcome-header').css('background-attachment', 'inherit')
}


// When redirecting to tabs from home page on small and medium screen size devices, close the navigation menu
// and remove classes connected to it.
$('.external-tab-link').on('click', function () {
    $('#navbarSupportedContent').collapse('hide')
    $('body').removeClass('overflow-hidden')
    $('nav').removeClass('bg-dark')
})


// SearchForm radio inputs handling (to make them look as select inputs)
let selected = document.querySelectorAll(".selected");

selected.forEach(function (x) {
    x.addEventListener("click", () => {
        let i = document.getElementById(x.id)
        let j = document.getElementById(i.closest('.select-box').id)
        j.querySelector('.option-container').classList.toggle("active");
        j.querySelector('.selected').classList.toggle("active");
        let optionList = j.querySelectorAll('.option')
        optionList.forEach(o => {
            o.addEventListener("click", () => {
                if (x.id === 'searchAge') {
                    x.innerHTML = "wiek" + " : " + '<span class="form-select-input">' + o.querySelector("label").innerHTML + '</span>';
                } else if (x.id === 'searchSpecies') {
                    x.innerHTML = "gatunek" + " : " + '<span class="form-select-input">' + o.querySelector("label").innerHTML + '</span>';
                } else if (x.id === 'searchSize') {
                    x.innerHTML = "rozmiar" + " : " + '<span class="form-select-input">' + o.querySelector("label").innerHTML + '</span>';
                } else if (x.id === 'searchGender') {
                    x.innerHTML = "płeć" + " : " + '<span class="form-select-input">' + o.querySelector("label").innerHTML + '</span>';
                }
                j.querySelector('.option-container').classList.remove("active");
                j.querySelector('.selected').classList.remove("active");
                j.querySelector('.reset').classList.add('show')
            });
        });
    })
});


// Reset button in SearchForm handling
let reset = document.querySelectorAll('.reset')
reset.forEach(function (x) {
    x.addEventListener('click', () => {
        let selectBox = document.getElementById(x.closest('.select-box').id)
        let selected = selectBox.querySelector(".selected")
        if (selected.id === 'searchAge') {
            selected.innerHTML = "wiek"
        } else if (selected.id === 'searchSpecies') {
            selected.innerHTML = "gatunek"
        } else if (selected.id === 'searchSize') {
            selected.innerHTML = "rozmiar"
        } else if (selected.id === 'searchGender') {
            selected.innerHTML = "płeć"
        }
        x.classList.remove('show')
    })
})


// Handling navigation active state
let navigation = document.getElementById("navigation");
window.addEventListener("scroll", function () {
    if (window.pageYOffset >= 100) {
        navigation.classList.add("active")
    } else if (window.pageYOffset < 90) {
        navigation.classList.remove("active")
    }
})

// Handling navigation open and close classes on small and medium devices
let openNavigation = $('.navbar-toggler')
openNavigation.click(function () {
    $('body').toggleClass("overflow-hidden")
    $('nav').toggleClass('bg-dark')
})