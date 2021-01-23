imgElement = document.getElementsByTagName('img')[2];

var canvas =  document.createElement('canvas');
var ctx = canvas.getContext('2d');
canvas.width = imgElement.width;
canvas.height = imgElement.height;
ctx.drawImage(imgElement, 0, 0);

var captcha_b64 = canvas.toDataURL();
captcha_b64 = captcha_b64.slice(22);

chrome.runtime.sendMessage({ message: 'send_b64_image', captcha_b64 });

chrome.runtime.onMessage.addListener((request, sender, senderResponse) => {
    var captcha_textbox = document.getElementsByName('captcha');
    captcha_textbox[0].autocomplete = 'on';
    captcha_textbox[0].value = request.captcha_text;
});

