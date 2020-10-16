var movies = []

function makeToast() {
    // Get the snackbar DIV
    var x = document.getElementById("snackbar");
  
    // Add the "show" class to DIV
    x.className = "show";
  
    // After 3 seconds, remove the show class from DIV
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
  }

  function makeToast1() {
    // Get the snackbar DIV
    var x = document.getElementById("snackbar1");
  
    // Add the "show" class to DIV
    x.className = "show";
  
    // After 3 seconds, remove the show class from DIV
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
  }

$(document).ready(() => {
    $("#add").on("click", () => {
        var film = $("#searchbox").val();
        if(film != "") {
            console.log(film);
            $.getJSON("https://api.themoviedb.org/3/search/movie?api_key=7346d90da037566a43b6a0414c77ea40&query=" + film + "&callback=?", function(json) {
                if (json.results[0] != null && !movies.includes(film)){                 
                    console.log(json);
                    var imagelink = "http://image.tmdb.org/t/p/w500/"+json.results[0].poster_path;
                    $('<div class="gall one" style = "margin-left: 200px; margin-top: 100px; padding: 15px border: 0px solid #ccc; float: left; width: 250px;"><div class="w3-card-4"><div class="w3-display-container w3-text-white"><img src="'+imagelink+'" alt="" style="width:100%"></div></div></div>').hide().appendTo("#movierow").fadeIn("fast");
                    
                    movies.push(film);
                    if(movies.length == 3) {
                        document.getElementById("add").disabled = true;
                        document.getElementById("search").disabled = false;
                    }
                    else {
                        document.getElementById("add").disabled = false;
                        document.getElementById("search").disabled = true;
                    }
                } else {
                    if(movies.includes(film)){
                        makeToast1();
                    }
                    else{
                        makeToast();
                    } 
                }
            });
        }
    });
});