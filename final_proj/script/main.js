console.log("page load - main.js");

var search_button   = document.getElementById("search-button");
var chapter         = document.getElementById("input-chapter-number");
var keyword         = document.getElementById("input-keyword");
var verse           = document.getElementById("input-verse");

//Perform Action Upon Click

search_button.onmouseup  = search_request;
// rec_button.onmouseup     = rec_request;

//Search Button Functionality
function search_request(){

    console.log('search_request');
    var requester        = new XMLHttpRequest();
    requester.responseType= "json";
    var total_url = "http://localhost:" + 51060;

    if (!chapter.value && !verse.value && !keyword.value) { // Print the entire Psalm
        total_url = total_url + "/book/";
        requester.open("GET", total_url, true);
    } 
    else if (chapter.value && !verse.value && !keyword.value) { // Print a specific chapter
        total_url = total_url + "/chapter/" + chapter.value;
        requester.open("GET", total_url, true);
    } 
    else if (chapter.value && verse.value && !keyword.value) { // Print a specific verse from a chapter
        total_url = total_url + "/verse/" + chapter.value + "_" + verse.value;
        requester.open("GET", total_url, true);
    }
    else if (!chapter.value && !verse.value && keyword.value){ 
        total_url = total_url + "/book/" + keyword.value;
        requester.open("GET", total_url, true);
    } else {
        alert("Invalid Input Method.")
    }
    
    // set up onload
    console.log("before xh.onload() in search_request");

    requester.onload = function(e) { // triggered when response is received
        var resp     = document.getElementById("answer-label");

        if (!chapter.value && !verse.value && !keyword.value) { // Print the entire Psalm
            if (requester.response["result"] === "error") { // error occurs
                alert(requester.response["message"])
                return
            }

            var text = []
            var book_result = requester.response["book"]
            for (var i = 0; i < book_result.length; i++) { // Parse the text of the book
                text.push("Chapter " + String(i+1))
                for (var j = 0; j < book_result[i].length; j++)
                    text.push("Ps. " + String(i+1) + ":" + String(j+1) + " | " + book_result[i][j])
            }
            resp.innerHTML = text.join("<br>")
        } 
        else if (chapter.value && !verse.value && !keyword.value) { // Print a specific chapter
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
        else if (chapter.value && verse.value && !keyword.value) { // Print a specific verse from a chapter
            if (requester.response["result"] === "success")
                resp.innerHTML = "Ps. " + String(chapter.value) + ":" + String(verse.value) + " | " + requester.response['verse'];
            else
                alert(requester.response["message"]) 
        }
        else if (!chapter.value && !verse.value && keyword.value){ 
            resp.innerHTML = requester.response['search_result'].map(function(val){return "Ps. " + (val[0] + 1) + ":" + (val[1] + 1) + " | " + val[2]}).join("<br><br>")
        }

        console.log("entered on.load()");
    }//end of onload

    requester.onerror = function(e) {
        console.error(requester.statusText)
    }//end of onerror

    console.log("message off");
    requester.send(null); //this actually makes the network call

}
//rec_request button
/*function rec_request(){
      console.log('recommedations');
      var req = new XMLHttpRequest();
      var total_url = "http://student00.cse.nd.edu:" + 51026 + "/recommendation/:";
      if (verse.value && chapter.value){
          total_url = total_url + verse.value;
          requester.open("GET", total_url, true);

      }
      // set up onload
      console.log("before xh.onload() in search_request");

      requester.onload = function(e) { // triggered when response is received
          var resp = document.getElementById("answer-label");

          //don't really get this
          resp.innerHTML  = requester.responseText



          console.log("entered on.load()");
          //console.log(requester.responseText + "reponse from ageApi");


      }//end of onload

      requester.onerror = function(e) {
          console.error(requester.statusText)
      }//end of onerror
      var message_textbox = document.getElementById("text-message-body");

      if (document.getElementById("checkbox-use-message").checked) {
          console.log("message on");
          console.log(message_textbox.value);
          requester.send(message_textbox.value); //this actually makes the network call
      }
      else {
          console.log("message off");
          requester.send(null); //this actually makes the network call
      }


}*/
