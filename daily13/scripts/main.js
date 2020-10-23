console.log('page load - entered main.js for js-other api');

var submitButton = document.getElementById('bsr-submit-button');
submitButton.onmouseup = getFormInfo;

function getFormInfo(){
    console.log('entered getFormInfo!');
    // call displayinfo
    var name = document.getElementById("name-text").value;
    console.log('Number you entered is ' + name);
    makeNetworkCallToAgeApi(name);

} // end of get form info

function makeNetworkCallToAgeApi(name){
    console.log('entered make nw call to ageApi' + name);
    // set up url
    var xhr = new XMLHttpRequest(); // 1 - creating request object
    var url = "https://api.agify.io/?name=" + name;
    xhr.open("GET", url, true); // 2 - associates request attributes with xhr

    // set up onload
    console.log("before xh.onload() in makeNetworkCallToAgeApi");
    xhr.onload = function(e) { // triggered when response is received
        // must be written before send


        console.log("entered on.load()");
        console.log(xhr.responseText + "reponse from ageApi");
        // do something
        updateAgeWithResponse(name, xhr.responseText);

    }//end of onload

    xhr.onerror = function(e) {
      console.error(xhr.statusText)
    }//end of onerror


    xhr.send(null); //this actually makes the network call
  }//end of makeNetworkCallToAgeApi

    function makeNetworkCallToCatApi(age){
        console.log('entered make nw call');
        // set up url
        var xhr = new XMLHttpRequest(); // 1 - creating request object
        var url = "https://cat-fact.herokuapp.com/facts";
        xhr.open("GET", url, true); // 2 - associates request attributes with xhr

        // set up onload
        xhr.onload = function(e) { // triggered when response is received
            // must be written before send
            console.log(xhr.responseText + "is responseText");
            // do something
          updateCatwithResponse(age, xhr.responseText)
        }


    // set up onerror
    xhr.onerror = function(e) { // triggered when error response is received and must be before send

        console.error(xhr.statusText + "is error status");
    }

    // actually make the network call
    xhr.send(null) // last step - this actually makes the request

} // end of make nw call

function updateAgeWithResponse(name, response_text){
    console.log("entered updateAge" + name);
    var response_json = JSON.parse(response_text);
    // update a label
    var label1 = document.getElementById("response-line1");

    if(response_json['age'] == null){
        label1.innerHTML = 'Apologies, we could not find your name.'
    } else{
        label1.innerHTML = 'hey '+ name + '! ,  here is your random cat fact! number: ' + response_json['age'];
        var age = parseInt(response_json['age']);
        makeNetworkCallToCatApi(age)
    }
} // end of updateAgeWithResponse


/*function makeNetworkCallToNumbers(age){
    console.log('entered make nw call' + age);
    // set up url
    var xhr = new XMLHttpRequest(); // 1 - creating request object
    var url = "http://numbersapi.com/" + age;
    xhr.open("GET", url, true) // 2 - associates request attributes with xhr

    // set up onload
    xhr.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhr.responseText);
        // do something
        updateCatwithResponse(age, xhr.responseText);
    }*/

    // set up onerror
    /*xhr.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhr.statusText);
    }

    // actually make the network call
    xhr.send(null) // last step - this actually makes the request

} // end of make nw call*/

function updateCatwithResponse(age, response_text){
    // update a label
    var label2 = document.getElementById("response-line2");
    //label2.innerHTML = response_text;

    // dynamically adding label
    label_item = document.createElement("label"); // "label" is a classname
    label_item.setAttribute("id", "dynamic-label" ); // setAttribute(property_name, value) so here id is property name of button object


    //Parse response_text

    var parsed_data = JSON.parse(response_text);
    var text = parsed_data["all"][age]["text"];
    console.log(text);

//document.getElementById("").innerHTML = obj.text


    var item_text = document.createTextNode(text); // creating new text
    label_item.appendChild(item_text); // adding something to button with appendChild()

    // option 1: directly add to document
    // adding label to document
    //document.body.appendChild(label_item);

    // option 2:
    // adding label as sibling to paragraphs
    var response_div = document.getElementById("response-div");
    response_div.appendChild(label_item);

    //makeNetworkCallToCatApi(age)

} // end of updateCatwithResponse
