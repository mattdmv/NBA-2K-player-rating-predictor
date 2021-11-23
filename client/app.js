function onClickedCalculate() {
    console.log("Calculate rating button clicked!");
    var player = document.getElementById("player-name-form");
    var playerName = document.getElementById("player-name-placeholder");
    var estRating = document.getElementById("predicted-rating-placeholder");
    var statsPts = document.getElementById("pts-placeholder");
    var statsReb = document.getElementById("reb-placeholder");
    var statsAst = document.getElementById("ast-placeholder");
    var statsStl = document.getElementById("stl-placeholder");
    var statsBlk = document.getElementById("blk-placeholder");
    var stats3p = document.getElementById("3p-placeholder");
    var statsPlusMinus = document.getElementById("plus-minus-placeholder");
    var statsGp = document.getElementById("gp-placeholder");
    
    var url = "http://127.0.0.1:5000/predict_player_rating"

    $.post(url, {player_name: player.value}, function(data, status) {
        console.log(data.predicted_value);
        estRating.innerHTML = "<h1>" + data.predicted_value.toString() + "</h1>";
        playerName.innerHTML = "<h1>" + player.value.toString() + "</h1>";
        statsPts.innerHTML = "<td>" + data.player_stats[0] + "</td>"
        statsReb.innerHTML = "<td>" + data.player_stats[1] + "</td>"
        statsAst.innerHTML = "<td>" + data.player_stats[2] + "</td>"
        statsStl.innerHTML = "<td >" + data.player_stats[3] + "</td>"
        statsBlk.innerHTML = "<td >" + data.player_stats[4] + "</td>"
        stats3p.innerHTML = "<td>" + data.player_stats[5] + "</td>"
        statsPlusMinus.innerHTML = "<td>" + data.player_stats[6] + "</td>"
        statsGp.innerHTML = "<td>" + data.player_stats[7] + "</td>"
        player.value = "";
        console.log(status);
    });
}