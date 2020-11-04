console.log("page load - main.js");

var search_button   = document.getElementById("search-button");
var clear_button    = document.getElementById("clear-button");
var favorite_button = document.getElementById("favorite-button");
var rec_button      = document.getElementById("rec-button");
var add_button      = document.getElementById("add-button");
var chapter         = document.getElementById("input-chapter-number");
var keyword         = document.getElementById("input-keyword");
var verse           = document.getElementById("input-verse");

//Perform Action Upon Click

 search_button.onmouseup  = search_request;
// rec_button.onmouseup     = rec_request;

//Search Button Functionality
function search_request(){

    console.log('search_request');
    var requester        = new XMLHttpRequest(); // 1 - creating request object // the thing that does the requesting
    requester.responseType= "json";
    var total_url = "http://student04.cse.nd.edu:" + 51026;
    //Print whole entire Psalm
    if(!chapter.value && !verse.value && !keyword.value){// and search is clicked
        //alert("inside book");
        total_url = total_url + "/book/";
        requester.open("GET", total_url, true);
    }

    //Print a specific chapter
    if (chapter.value && !verse.value){
        if((chapter.value > 150) || (chapter.value < 0)){
          alert("Invalid Chapter Number: Enter a chapter number in the range 1 - 176")
          return;
        }

        total_url = total_url + "/chapter/" + chapter.value;
        requester.open("GET", total_url, true);

    }
    //Print all verses associated with a keyword
    if (keyword.value){
        total_url = total_url + "/book/" + keyword.value;

        requester.open("GET", total_url, true); // 2 - associates request attributes with requester

    }
    //Print a specific verse from a chapter
    if (verse.value && chapter.value){
      if((chapter.value > 150) || (verse.value > 176 ) || (verse.value < 0 ) ||  (chapter.value < 0 )){
        alert("Invalid Chapter Number or Verse Number. Please check the specified ranges. ")
        return;

      }

        total_url = total_url + "/verse/" + chapter.value + "_" + verse.value;
        requester.open("GET", total_url, true);

    }
    if(verse.value && !chapter.value && !keyword.value){
      alert("Must specifiy a chapter number")
      return;
    }
    // set up onload
    console.log("before xh.onload() in search_request");

    requester.onload = function(e) { // triggered when response is received
        var resp     = document.getElementById("answer-label");

        //don't really get this

        if (chapter.value && !verse.value){
            resp.innerHTML  = requester.response['chapter'].join("<br>")

        }
        if(!chapter.value && !verse.value && !keyword.value){
          resp.innerHTML = requester.response['book']

        }

        if (verse.value && chapter.value){

            resp.innerHTML = requester.response['verse'];

        }
        if (keyword.value){
          resp.innerHTML = requester.response['search_result'].map(function(val){return "Ps. " + (val[0] + 1) + ":" + (val[1] + 1) + " | " + val[2]}).join("<br><br>")

        }


        console.log("entered on.load()");


    }//end of onload

    requester.onerror = function(e) {
        console.error(requester.statusText)
    }//end of onerror

    //If nothing is entered and the user just hits "search_button"

    //Should this be in an elseif?
    /*requester.open("GET", total_url, true);
    total_url = total_url + "/book/";*/


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
