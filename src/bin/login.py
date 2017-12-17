import requests


class login:
    login=""
    password=""

    def __init__(self, login, password):
        self.login = login
        self.password = password

class api:
    url = 'https://badoo.com/api.phtml?SERVER_LOGIN_BY_PASSWORD'
    r = requests

    headers = "POST /api.phtml?SERVER_LOGIN_BY_PASSWORD HTTP/1.1
Host: badoo.com
Connection: keep-alive
Content-Length: 201
Origin: https://badoo.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/62.0.3202.94 Chrome/62.0.3202.94 Safari/537.36
Content-Type: json
"


s = login(123,123)



    
    


