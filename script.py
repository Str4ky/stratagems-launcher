from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from flask import Flask, request
import threading
import keyboard
import json
import time

app = Flask("Stratagems Launcher")

file = "assets/json/config.json"

with open(file) as f:
    data = json.load(f)
    url = data["url"]
    ip = url.replace("http://", "").replace("https://", "")
    server_port = data["server_port"]
    web_port = data["web_port"]


@app.route('/keypress/<key>', methods=['GET'])
def keypress(key):
    try:
        keyboard.press(key)
        time.sleep(0.1)
        keyboard.release(key)
        return f"Key '{key}' pressed", 200
    except Exception as e:
        return f"Error: {e}", 400

def run_flask():
    app.run(host=ip, port=server_port)

def run_web_server():
    handler = SimpleHTTPRequestHandler
    with TCPServer((ip, web_port), handler) as httpd:
        print("Serving website on " + url + ":" + str(web_port))
        httpd.serve_forever()

flask_thread = threading.Thread(target=run_flask, daemon=True)
web_server_thread = threading.Thread(target=run_web_server, daemon=True)

flask_thread.start()
web_server_thread.start()

print("Servers are running...")
flask_thread.join()
web_server_thread.join()