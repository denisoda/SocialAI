import requests


class login:
    login=""
    password=""

    def __init__(self, login, password):
        self.login = login
        self.password = password
        login.login = login
        login.password = password
        

class api(login):
    url = 'https://badoo.com/api.phtml?SERVER_LOGIN_BY_PASSWORD'
    r = requests
    

    headers = '''POST /api.phtml?SERVER_LOGIN_BY_PASSWORD HTTP/1.1
    Host: badoo.com
    Connection: keep-alive
    Content-Length: 201
    Origin: https://badoo.com
    User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/62.0.3202.94 Chrome/62.0.3202.94 Safari/537.36
    Content-Type: json'''

    body = '''
    {"version":1,"message_type":15,"message_id":2,"body":[{"message_type":15,"server_login_by_password":{"remember_me":true,"user":"''' + str(login) + '''","password":"''' + str(password) +'''"}}],"is_background":false}
    '''


s = login(123,123)

print(api.body)



    
    


