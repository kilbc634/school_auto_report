import requests
import json

class requestLib():
    def __init__(self):
        self.URL = 'https://epidemicapi.ncut.edu.tw/api/'
        self.SESSION = requests.Session()
        self.SESSION.headers.clear()
        self.SESSION.headers.update({
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://epidemic.ncut.edu.tw',
            'referer': 'https://epidemic.ncut.edu.tw/bodyTemp'
        })

    def __request(self, method, node='', **kwargs):
        resp = self.SESSION.request(method, self.URL + node, **kwargs)
        try:
            print(resp)
            print(resp.text)
        except (UnicodeDecodeError, UnicodeDecodeError, UnicodeError):
            print('[WARNING] Unknow unicode error from response')
        return resp

    #------------------------------------------------------------------------------------
    # Function Zone
    #------------------------------------------------------------------------------------

    def login(self, account, password , remember=False):
        '''
        Note: 拿取新的token，也不會因此讓舊token失效
        '''
        data = {
            'userId': account,
            'password': password,
            'remember': remember
        }
        self.SESSION.headers.update({'referer': 'https://epidemic.ncut.edu.tw/login'})
        resp = self.__request('post', 'login', json=data)
        respJson = json.loads(resp.text)
        return respJson

    def getToken(self, account, password):
        resp = self.login(account, password)
        token = resp['token']
        return token

    def get_departments(self, token):
        self.SESSION.headers.update({'authorization': 'Bearer %s' % token})
        resp = self.__request('get', 'departments')
        return resp



if __name__ == "__main__":
    Lib = requestLib()
    print('請登入系統（預設帳號密碼同學生篇），或於 user.cfg 檔案設置基本資料\n')
    myAccount = input('學號:')
    myPassword = input('密碼:')
    userToken = Lib.getToken(myAccount, myPassword)
    departments = json.loads(Lib.get_departments(userToken).text)
    print(departments)
