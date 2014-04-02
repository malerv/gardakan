var last_pull = new Date();

function pullMessage()
{
    var inputString = '{ "date":"' + last_pull.toJSON() + '",';
    inputString += '"event": "' + chatId + '"}';
    $.ajax({
        url : "/pull_message",
        type : "POST",
        dataType: "json",
        data : {
            client_response : inputString,
        },
        success : function(json) {
        console.log('Server response : ' + json.server_response);
        },
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + "****: " + xhr.responseText);
            console.log(errmsg);
        }
    });
}

function enterMessage(textID)
{
    var textBox = document.getElementById(textID);
    var sendTextForm = $('#inputMessageForm');
    var messageText = textBox.value;
    var uName = userName
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

    var inputString = '{ "userName": "' + uName +'", ';
        inputString += '"time":"' + today.toJSON() + '", ';
        inputString += '"text": "' + messageText + '", ';
        inputString += '"event": "' + chatId + '"}';
    console.log(inputString)
    $(document).ready(function(){
        $.ajax({
            url : "/input_message",
            type : "POST",
            dataType: "json",
            data : {
                client_response : inputString,
            },
            success : function(json) {
                console.log('Server response : ' + json.server_response);
            },
            error : function(xhr,errmsg,err) {
                console.log(xhr.status + "****: " + xhr.responseText);
                console.log(errmsg);
            }
        });
        return false;
    });
    pullMessage()
}

function insertMessage(userID, message, containerID)
{
    var user = userName
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

