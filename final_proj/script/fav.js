console.log("page load - fav.js");

var clear_button    = document.getElementById("clear-button");
var delete_button   = document.getElementById("delete-button");
var rec_button      = document.getElementById("rec-button");
var add_button      = document.getElementById("add-button");
var chapter         = document.getElementById("input-chapter-number");
var verse           = document.getElementById("input-verse-number");

// show "My Favorite"
show_my_favorite(); 

//Perform Action Upon Click
add_button.onmouseup     = add_request;
delete_button.onmouseup  = delete_request;
clear_button.onmouseup   = clear_request;
rec_button.onmouseup     = rec_request;

//show my favorite Functionality
function show_my_favorite() {

    console.log('show_my_favorite');
    var requester        = new XMLHttpRequest();
    requester.responseType= "json";
    var total_url = "http://localhost:" + 51060;

    total_url = total_url + "/favorite/";
    requester.open("GET", total_url, true);
    
    // set up onload
    console.log("before requester.onload() in show_my_favorite");

    requester.onload = function(e) { // triggered when response is received
        
        if (requester.response["result"] === "error") // error occurs
            alert(requester.response["message"]);
        else {
            var resp = document.getElementById("answer-label");
            resp.innerHTML = requester.response['favorite'].map(function(val){return "Ps. " + (val[0] + 1) + ":" + (val[1] + 1) + " | " + val[2]}).join("<br><br>")
        }

        console.log("entered on.load()");
    }//end of onload

    requester.onerror = function(e) {
        console.error(requester.statusText);
    }//end of onerror

    console.log("message off");
    requester.send(null); //this actually makes the network call

}

//Add Button Functionality
function add_request() {

    console.log('add_request');
    var requester        = new XMLHttpRequest();
    requester.responseType= "json";
    var total_url = "http://localhost:" + 51060;

    if (chapter.value && verse.value) { // Add a verse
        total_url = total_url + "/favorite/";
        // request body
        var message = '{"chapter_number" :"' + String(chapter.value) +
            '", "verse_number":"' + String(verse.value) + '"}';
        console.log(message);
        requester.open("POST", total_url, true);
    } else {
        alert("Invalid Input Method.");
    }
    
    // set up onload
    console.log("before requester.onload() in add_request");

    requester.onload = function(e) { // triggered when response is received
        
        if (requester.response["result"] === "error") // error occurs
            alert(requester.response["message"]);
        else {
            show_my_favorite() // update my_favorite
            alert("You have added " + "Ps. " + String(chapter.value) + ":" + String(verse.value) + ' to "My Favorite" successfully');
        }

        console.log("entered on.load()");
    }//end of onload

    requester.onerror = function(e) {
        console.error(requester.statusText);
    }//end of onerror

    console.log("message off");
    requester.send(message); //this actually makes the network call

}

//Delete Button Functionality
function delete_request() {

    console.log('delete_request');
    var requester        = new XMLHttpRequest();
    requester.responseType= "json";
    var total_url = "http://localhost:" + 51060;

    if (chapter.value && verse.value) { // delete a verse
        total_url = total_url + "/favorite/" + chapter.value + "_" + verse.value;
        requester.open("DELETE", total_url, true);
    } else {
        alert("Invalid Input Method.");
    }
    
    // set up onload
    console.log("before requester.onload() in delete_request");

    requester.onload = function(e) { // triggered when response is received
        
        if (requester.response["result"] === "error") // error occurs
            alert(requester.response["message"]);
        else {
            show_my_favorite() // update my_favorite
            alert("You have deleted " + "Ps. " + String(chapter.value) + ":" + String(verse.value) + ' from "My Favorite" successfully');
        }

        console.log("entered on.load()");
    }//end of onload

    requester.onerror = function(e) {
        console.error(requester.statusText);
    }//end of onerror

    console.log("message off");
    requester.send(null); //this actually makes the network call

}

//Clear Button Functionality
function clear_request() {

    console.log('clear_request');
    var requester        = new XMLHttpRequest();
    requester.responseType= "json";
    var total_url = "http://localhost:" + 51060;

    total_url = total_url + "/favorite/";
    requester.open("DELETE", total_url, true);
    
    // set up onload
    console.log("before requester.onload() in clear_request");

    requester.onload = function(e) { // triggered when response is received
        
        if (requester.response["result"] === "error") // error occurs
            alert(requester.response["message"]);
        else {
            show_my_favorite() // update my_favorite
            alert('You have cleared "My Favorite" successfully');
        }

        console.log("entered on.load()");
    }//end of onload

    requester.onerror = function(e) {
        console.error(requester.statusText);
    }//end of onerror

    console.log("message off");
    requester.send(null); //this actually makes the network call

}

//Rec Button Functionality
function rec_request() {

    console.log('rec_request');
    var requester        = new XMLHttpRequest();
    requester.responseType= "json";
    var total_url = "http://localhost:" + 51060;

    var default_number = 20
    total_url = total_url + "/recommendation/" + String(default_number);
    requester.open("GET", total_url, true);
    
    // set up onload
    console.log("before requester.onload() in rec_request");

    requester.onload = function(e) { // triggered when response is received
        
        if (requester.response["result"] === "error") // error occurs
            alert(requester.response["message"]);
        else {
            var resp = document.getElementById("recommendation-label");
            resp.innerHTML = requester.response['recommendation'].map(function(val){return "Ps. " + (val[0] + 1) + ":" + (val[1] + 1) + " | " + val[2]}).join("<br><br>")
            alert('The Recommendations for You have been Updated');
        }

        console.log("entered on.load()");
    }//end of onload

    requester.onerror = function(e) {
        console.error(requester.statusText);
    }//end of onerror

    console.log("message off");
    requester.send(null); //this actually makes the network call

}