chrome.runtime.onMessage.addListener((request, sender, senderResponse) => {
	  switch (request.message) {
		case 'send_b64_image': {
			var captcha_b64 = request.captcha_b64;
			
			var xhttp = new XMLHttpRequest();
			var url = 'http://mahieyin.pythonanywhere.com/';
			xhttp.open('POST', url);
			xhttp.setRequestHeader("Content-Type", "application/json");
			var data = JSON.stringify({"base64": captcha_b64});
			xhttp.send(data);

			xhttp.onreadystatechange = () => {
				if (xhttp.readyState === 4 && xhttp.status === 200) {
					var json = JSON.parse(xhttp.responseText);
					var captcha_text = json.captcha_text;

					chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
						chrome.tabs.sendMessage(tabs[0].id, {"captcha_text": captcha_text});  
					});
				}
			};
			break;
		}
		default:
	  }
	}
);