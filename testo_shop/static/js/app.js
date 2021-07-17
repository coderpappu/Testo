
$('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    responsiveClass:true,
    responsive:{
        0:{
            items:2,
            // nav:true
        },
        600:{
            items:4,
            // nav:false
        },
        1000:{
            items:6,
            // nav:true,
            loop:true
        }
    }
})


$('.our_admin_carousel').owlCarousel({
    loop:true,
    margin:10,
    autoplay : true,
    smartSpeed : 400,
    autoplaySpeed: 1000,
    responsiveClass:true,
    dots:true,
    responsive:{
        0:{
            items:1,
            // nav:true
        },
        600:{
            items:1,
            // nav:false
        },
        1000:{
            items:1,
            // nav:true,
            loop:true
        }
    }
})



var login = document.querySelector("#Link_click")
login.addEventListener("click", function () {
    console.log("Hmm");
    let sure = confirm("Are You Sure Want To Login ?")
    // if (sure == true){
    //     alert("OK")

    // }

    var log = (sure ==true) ? window.location = "shopperApp/login" : alert("KKK");
})


alert("Welcome TO Our Testo Burger Shop")
