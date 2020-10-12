$(document).ready(() => {
    var movieid = $(".line-1.anim-typewriter").attr('id');
    console.log(movieid);
    window.location.href = "http://127.0.0.1:8000/movie/"+movieid;
});