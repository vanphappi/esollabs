from flask import Flask, redirect, url_for,request, render_template
import requests
import json
import string
import random
import hashlib
from datetime import datetime

app = Flask(__name__)

token_create_time = {}
token_verify = {}

token_verify_telegram ={}
token_verify_discord ={}

def check_valid_token(token):
    try:
        token_time_create = datetime.strptime(str(token_create_time[str(token)]), "%Y-%m-%d %H:%M:%S.%f")
        current_time = datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f")

        time_interval = str(current_time - token_time_create).split(":")

        time_interval_second = float(time_interval[len(time_interval)-1]) + float(time_interval[len(time_interval)-2])*60

        if(time_interval_second > 180 ):
            return "0"
        else:
            return "1"
    except:
        return "0"

def id_generator(size=15, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@app.route('/dotmeme.ai/user_verify_discord/userid=<userid>')
def check_verify_user_discord(userid):
    try:
        return f"{token_verify_discord[userid]}"
    except:
        return "0"

@app.route('/dotmeme.ai/verify/token=<token>/telegram/address=<address>')
def check_verify_user_telegram(token,address):
    try:
        return f"{token_verify_telegram[address]}"
    except:
        return "0"

@app.route('/dotmeme.ai/verify/token=<token>/address=<address>')
def verify_user(token,address):
    try:
        if(check_valid_token(token) == "0"):
            return render_template("error_page.html")
        else:
            url = "https://dns-stag.dotmeme.ai/v1/api/user/profile?owner="+str(address)
            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            result = json.loads(response.text)

            id = token_verify[str(token)]
            print(result["data"]["domains"])
            if len(result["data"]["domains"]) > 0:
                token_verify_discord[id] = [str(address)]
                token_verify_telegram[str(address)] = id
                return "1"
            else:
                return "0"
    except:
        return render_template("error_page.html")

@app.route('/dotmeme.ai/verify/token=<token>')
def page_verify(token):
    if check_valid_token(token) == "1" :
        return render_template("verify_page.html")
    else:
        return render_template("error_page.html")

@app.route('/dotmeme.ai/id=<id>')
def create_link_verify(id):
    now = datetime.now()
    now = hashlib.md5(str(now).encode())

    id_endcode = hashlib.md5(str(id).encode())

    code = id_generator()
    code = hashlib.md5(str(code).encode())

    token = str(now.hexdigest()) + str(id_endcode.hexdigest()) + str(code.hexdigest())

    token = hashlib.md5(str(token).encode())

    token = token.hexdigest()

    token_create_time[str(token)] = str(datetime.now())
    token_verify[str(token)] = str(id)

    return f"http://127.0.0.1:5000/dotmeme.ai/verify/token={token}"

if __name__ == '__main__':
   app.run(debug = True)