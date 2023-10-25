const btnJS= document.getElementById("btnJS")
const jsmessage=document.getElementById("javascript_message")
//const ename=document.getElementById("firstname")


btnJS.addEventListener("click", buttonClickHandler);

function buttonClickHandler(){

    //fname= ename.value
    //alert("hello jscript")

    jsmessage.textContent="hello from javascript, how are you "
    //alert("Hi Javascript function")
}


//btnJS.addEventListener("click", function() {
//    alert("Blah blah...");
//}, false);


