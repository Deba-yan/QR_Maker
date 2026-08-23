from flask import Flask, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route("/")
def home():
    return open("index.html", encoding="utf-8").read()

@app.route("/style.css")
def style():
    return open("style.css", encoding="utf-8").read(), 200, {
        "Content-Type": "text/css"
    }

@app.route("/generate", methods=["POST"])
def generate():
    text = request.form["link"]

    qr = qrcode.make(text)

    buffer = io.BytesIO()
    qr.save(buffer, "PNG")
    buffer.seek(0)

    return send_file(buffer, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
