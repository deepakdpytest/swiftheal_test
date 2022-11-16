let slider = $(".myslider");
let prev = $(".myslider_controls--left");
let next = $(".myslider_controls--right");
let margin = $(".myslider_cards").css("margin");
margin = Number(margin.slice(0, -2));
let width = $(".myslider_cards").width() + 2 * margin;
let activeSlider = 1;
let totalSlider = Math.round($(".myslider")[0].scrollWidth / $(".myslider_cards").width()) + 1;
next.on("click", function() {
    if (activeSlider == totalSlider - 1) {
        slider.scrollLeft(0);
        activeSlider = 1;
    } else {
        slider.scrollLeft(slider.scrollLeft() + width);
        activeSlider++;
    }
});
prev.on("click", function() {
    if (activeSlider == 1) {
        activeSlider = totalSlider;
        slider.scrollLeft(width * totalSlider);

    } else {
        slider.scrollLeft(slider.scrollLeft() - width);
        activeSlider--;
    }
});
setInterval(function() {
    next.click();
}, 3000);