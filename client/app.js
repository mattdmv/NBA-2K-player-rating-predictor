function onClickedCalculate() {
    console.log("Calculate rating button clicked!");
    var player = document.getElementById("player-name-form");
    var playerName = document.getElementById("player-name-placeholder");
    var estRating = document.getElementById("predicted-rating-placeholder");
    
    var url = "http://127.0.0.1:8000/predict_player_rating"

    $.post(url, {player_name: player}, function(data, status) {
        console.log(data.predicted_value);
        estRating.innerHTML = "<h1>" + data.predicted_value.toString() + "</h1>";
        console.log(status);
    });
}