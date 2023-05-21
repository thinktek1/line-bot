from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.exceptions import(
    InvalidSignatureError
)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import json

app = Flask(__name__)
line_bot_api = LineBotApi("JO83I2aU+E2hNCuoftPDI4Mcmvp8ugsNVUPufoTYZo5paFr/7tfZpBsjlRdMnIQLo8u1SYSj5tb5zzwEdCojMDsGfqt/d8GQBMIw0ubroY24KlAqX7is7cCeBjRWvHT3CrzwWcfui8z14PSfgOKiaAdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("a512ec07066d617e863804ef6654ff02")

@app.route("/callback",methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    json_str = json.dumps(json_data, indent=4)
    print(json_str)
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    json_data = json.loads(str(event))
    json_str = json.dumps(json_data, indent=4)
    print(json_str)
    
@app.route("/push")
def push_msg():
    try:
        line_bot_api.push_message("USER_ID", TextSendMessage("Hi"))
        return "push ok"
    except:
        return "push error"
if __name__ == "__main__":
    app.run(port=9595)
