function enterMessage(textID)
{
    var textBox = document.getElementById(textID);
    var textHF = document.getElementById("textToSend");
    var currentTimeHF = document.getElementById("currentTime");
    var sendTextForm = document.getElementById("inputMessageForm");
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
    sendTextForm.submit();
}

function insertMessage(userID, message, containerID)
{
    var user = document.getElementById(userID).value;
    var mycontainer = document.getElementById(containerID);
    var newMessage = '';
    
    newMessage += '<div class="chatmessage">';
    newMessage += '<strong><span>' + user + ': </span>&nbsp;</strong>';
    newMessage += '<span>' + message + '</span>';
    newMessage += '</div>';
    
    mycontainer.innerHTML += newMessage;
}