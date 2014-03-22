function enterMessage(textID)
{
    var textBox = document.getElementById(textID);
    var messageText = textBox.value;
    textBox.value = "";
    
    console.log(messageText);
}