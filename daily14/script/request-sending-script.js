console.log("page load- entered request-sending-script.js");

var select      = document.getElementById("select-server-address");
var send_button = document.getElementById("send-button");

send_button.onmouseup = send_request;


function send_request(){

    console.log('send_request');
    // set up url
    var requester        = new XMLHttpRequest(); // 1 - creating request object // the thing that does the requesting
    var url              = select.value;
    var port             = document.getElementById("input-port-number");
    var key_checkbox     = document.getElementById("checkbox-use-key");
    var message_checkbox = document.getElementById("checkbox-use-message");
    var get              = document.getElementById("radio-get");
    var put              = document.getElementById("radio-put");
    var post             = document.getElementById("radio-post");
    var delete_item      = document.getElementById("radio-delete");


    var total_url = url + ":" + port.value + "/movies/";
    var key = document.getElementById("input-key")
    if (key_checkbox.checked){
        total_url = total_url + key.value
    }

    if (get.checked){
        requester.open("GET", total_url, true); // 2 - associates request attributes with requester

    } else if (put.checked){
        requester.open("PUT", total_url, true); // 2 - associates request attributes with requester

    } else if (post.checked){
        requester.open("POST", total_url, true); // 2 - associates request attributes with requester

    } else { 
        requester.open("DELETE", total_url, true); // 2 - associates request attributes with requester

    }

    // set up onload
    console.log("before xh.onload() in send_request");

    requester.onload = function(e) { // triggered when response is received
        var resp = document.getElementById("answer-label");

        // must be written before send
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
}
