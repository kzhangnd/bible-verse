console.log("page load - main.js");

var search_button   = document.getElementById("search-button");
var goto_button     = document.getElementById("goto-button");
var chapter         = document.getElementById("input-chapter-number");
var keyword         = document.getElementById("input-keyword");
var verse           = document.getElementById("input-verse-number");

//Perform Action Upon Click
goto_button.onmouseup = goto_request;
search_button.onmouseup  = search_request;

// rec_button.onmouseup     = rec_request;

//Goto Button Functionality
function goto_request(){

    console.log('goto_request');
    var requester        = new XMLHttpRequest();
    requester.responseType= "json";
    var total_url = "http://localhost:" + 51060;

    if (!chapter.value && !verse.value) { // Print the entire Psalm
        total_url = total_url + "/book/";
        requester.open("GET", total_url, true);
    } 
    else if (chapter.value && !verse.value) { // Print a specific chapter
        total_url = total_url + "/chapter/" + chapter.value;
        requester.open("GET", total_url, true);
    } 
    else if (chapter.value && verse.value) { // Print a specific verse from a chapter
        total_url = total_url + "/verse/" + chapter.value + "_" + verse.value;
        requester.open("GET", total_url, true);
    }
    else {
        alert("Invalid Input Method.");
        return;
    }
    
    // set up onload
    console.log("before xh.onload() in goto_request");

    requester.onload = function(e) { // triggered when response is received
        var resp     = document.getElementById("answer-label");

        if (!chapter.value && !verse.value) { // Print the entire Psalm
            if (requester.response["result"] === "error") { // error occurs
                alert(requester.response["message"])
                return
            }

            var text = []
            var book_result = requester.response["book"]
            for (var i = 0; i < book_result.length; i++) { // Parse the text of the book
                if (i != 0) text.push(""); // add an extra line between paragraphs
                text.push("Chapter " + String(i+1))
                for (var j = 0; j < book_result[i].length; j++)
                    text.push("Ps. " + String(i+1) + ":" + String(j+1) + " | " + book_result[i][j])
            }
            resp.innerHTML = text.join("<br>")
        } 
        else if (chapter.value && !verse.value) { // Print a specific chapter
            if (requester.response["result"] === "success") {
                var text = []
                var chapter_result = requester.response["chapter"]
                for (var i = 0; i < chapter_result.length; i++)
                    text.push("Ps. " + String(chapter.value) + ":" + String(i+1) + " | " + chapter_result[i])
                resp.innerHTML = text.join("<br>")
            }
            else
                alert(requester.response["message"]) 
        } 
        else { // Print a specific verse from a chapter
            if (requester.response["result"] === "success")
                resp.innerHTML = "Ps. " + String(chapter.value) + ":" + String(verse.value) + " | " + requester.response['verse'];
            else
                alert(requester.response["message"]) 
        }
    

        console.log("entered on.load()");
    }//end of onload

    requester.onerror = function(e) {
        console.error(requester.statusText)
    }//end of onerror

    console.log("message off");
    requester.send(null); //this actually makes the network call

}

//Search Button Functionality
function search_request(){

    console.log('search_request');
    var requester        = new XMLHttpRequest();
    requester.responseType= "json";
    var total_url = "http://localhost:" + 51060;

    if (!keyword.value){ 
        console.log("no keyword input");
        return;
    }

    total_url = total_url + "/book/" + keyword.value;
    requester.open("GET", total_url, true);
    
    // set up onload
    console.log("before xh.onload() in search_request");

    requester.onload = function(e) { // triggered when response is received
        var resp     = document.getElementById("answer-label");

        if (requester.response["result"] === "success")
            resp.innerHTML = requester.response['search_result'].map(function(val){return "Ps. " + (val[0] + 1) + ":" + (val[1] + 1) + " | " + val[2]}).join("<br><br>")
        else
            alert(requester.response["message"]) 

        console.log("entered on.load()");
    }//end of onload

    requester.onerror = function(e) {
        console.error(requester.statusText)
    }//end of onerror

    console.log("message off");
    requester.send(null); //this actually makes the network call

}

