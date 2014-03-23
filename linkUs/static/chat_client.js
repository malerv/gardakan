function enterMessage(textID)
{
    var textBox = document.getElementById(textID);
    var textHF = document.getElementById("textToSend");
    var currentTimeHF = document.getElementById("currentTime");
    var sendTextForm = $('#inputMessageForm');
    var messageText = textBox.value;
    textBox.value = "";
    
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
    
    sendTextForm.submit(function(event){
        event.preventDefault();
        
        $.ajax({
            type: "POST",
            url: "/input_chat_message.html",
            data: sendTextForm.serialize(),
            success: function(response){
                console.log(response);
            }
        });
        console.log("fail");
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
