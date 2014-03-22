function enterMessage(textID)
{
    var textBox = document.getElementById(textID);
    var messageText = textBox.value;
    textBox.value = "";
    
    if(messageText != null && messageText.trim() != "")
    {
        console.log("Sending message : " + messageText);
        insertMessage('userName', messageText,'chatMessagesdiv_1'); 
    }
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