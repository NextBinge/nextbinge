$(document).ready(() => {
    console.log($('.title').attr('id'));
    var length = $('.title').attr('id');
    for (let i = 0; i < length; i++) {
        let film = $("#"+i).text();
        if(film != "") {
            $.getJSON("https://api.themoviedb.org/3/search/movie?api_key=7346d90da037566a43b6a0414c77ea40&query=" + film + "&callback=?", function(json) {
                if (json.results[0].poster_path != null){                 
                    console.log(json);
                    $("#"+$("#"+i).text().replace(/ /g, '_').replace(/'/g, '').replace(/:/g, '').split('.').join("").split('&').join("")).attr("src", "http://image.tmdb.org/t/p/w500/"+json.results[0].poster_path);
                    } else {
                        $.getJSON("https://api.themoviedb.org/3/search/movie?api_key=15d2ea6d0dc1d476efbca3eba2b9bbfb&query=Interstellar&callback=?", function(json) {
                        console.log(json);
                        $("#"+$("#"+i).text().replace(/ /g, '_').replace(/'/g, '').replace(/:/g, '').split('.').join("").split('&').join("")).attr("src", "http://image.tmdb.org/t/p/w500/"+json.results[0].poster_path);
                    });
                }
            });
        }
    }
})