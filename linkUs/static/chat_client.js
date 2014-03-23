function enterMessage(textID)
{
    var textBox = document.getElementById(textID);
    var textHF = document.getElementById("textToSend");
    var currentTimeHF = document.getElementById("currentTime");
    var sendTextForm = $('#inputMessageForm');
    var messageText = textBox.value;
    var uName = document.getElementById("userName").value;
    textBox.value = "";
    var today = new Date();
    var hours=today.getHours();
    var minutes=today.getMinutes();
    
    if(messageText != null && messageText.trim() != "" && messageText.length <= 255)
    {
        console.log("Sending message : " + messageText);
        insertMessage('userName', messageText,'chatMessagesdiv_1'); 
    }
    else {
        return;
    }
    
    textHF.value = messageText;
    currentTimeHF.value = new Date().getTime() / 1000;
    
    var inputString = "{ userName:'" + uName +"',";
        inputString += "time:'" + hours + "h" + minutes + "',";
        inputString += "text:'" + messageText + "'}";
    
    $(document).ready(function(){
        $.ajax({
            url : "/input_message",
            type : "POST",
            dataType: "json",
            data : {
                client_response : inputString,
                csrfmiddlewaretoken: '{{ csrf_token }}',
            },
            success : function(json) {
                console.log('Server response : ' + json.server_response);
            },
            error : function(xhr,errmsg,err) {
                console.log("Error sending message");
            }
        });
        return false;
    });
}

function insertMessage(userID, message, containerID)
{
    var user = document.getElementById(userID).value;
    var mycontainer = document.getElementById(containerID);
    var newMessage = '';
    var today = new Date();
    var hours=today.getHours();
    var minutes=today.getMinutes();
    
    newMessage += '<p class="left">';
    newMessage += '<strong><span>' + user + ': </span>&nbsp;</strong>';
    newMessage += '(' + hours + 'h' + minutes + '):&nbsp;';
    newMessage += '<span>' + message + '</span></p>';
    
    mycontainer.innerHTML += newMessage;
}
