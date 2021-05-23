import requests
import json
from configparser import ConfigParser
import datetime

DEBUG = False
WEEKS_STR = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
maxBackDay = 7
warningTemperature = 37.5
recordDay = maxBackDay

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
        if DEBUG:
            try:
                print(resp)
                print(resp.text)
            except (UnicodeDecodeError, UnicodeDecodeError, UnicodeError):
                print('[Error] Unknow unicode error from response')
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

    def checkPosted(self, token, userId, date):
        resp = self.get_tempData(token, userId, date)
        if len(resp.text) == 0:
            if DEBUG:
                print('[Info] {userId}-{date} date not exist'.format(userId=userId, date=date))
            return False
        else:
            if DEBUG:
                print('[Info] {userId}-{date} date exist'.format(userId=userId, date=date))
            return True

    #-------------------------------------------------------------------------------------

    def get_departments(self, token):
        self.SESSION.headers.update({'authorization': 'Bearer %s' % token})
        resp = self.__request('get', 'departments')
        return resp

    def get_tempData(self, token, userId, date):
        self.SESSION.headers.update({'authorization': 'Bearer %s' % token})
        resp = self.__request('get', 'temperatureSurveys/{userId}-{date}'.format(userId=userId, date=date))
        return resp

    def post_tempData(self, token, userId, departmentId, departmentName, className, date,
        morningTemp=34, morningActivity='',
        noonTemp=34, noonActivity='',
        nightTemp=34, nightActivity='',
        method='post'):
        self.SESSION.headers.update({'authorization': 'Bearer %s' % token})
        data = {
            "id": userId + "-undefined",
            "saveDate": date,
            "morningTemp": morningTemp,
            "noonTemp": noonTemp,
            "nightTemp": nightTemp,
            "isValid": False,
            "morningManner": 0,
            "noonManner": 0,
            "nightManner": 0,
            "isMorningFever": None,
            "isNoonFever": False,
            "isNightFever": None,
            "morningActivity": morningActivity,
            "noonActivity": noonActivity,
            "nightActivity": nightActivity,
            "measureTime": "20:00",
            "userId": userId,
            "departmentId": departmentId,
            "className": className,
            "departmentName": departmentName,
            "type": "1"
        }
        resp = self.__request(method, 'temperatureSurveys', json=data)
        if resp.status_code == 200:
            respJson = json.loads(resp.text)
            respJson["messages"] = [
                "{userId} {date} 已填入正常體溫".format(userId=userId, date=date)
            ]
            print("[OK] {msg}".format(msg=respJson["messages"][0]))
            return respJson
        elif resp.status_code == 500:
            respJson = {
                "success": False,
                "messages": [
                    "{userId} {date} 當天資料已存在".format(userId=userId, date=date)
                ]
            }
            print("[Warning] {msg}".format(msg=respJson["messages"][0]))
            return respJson
        else:
            resp.raise_for_status()

if __name__ == "__main__":
    Lib = requestLib()

    user = ConfigParser()
    user.read('user.ini', encoding='utf-8-sig')

    envId = user['env']['departmentId']
    envName = user['env']['departmentName']
    className = user['env']['className']

    myAccount = user['user']['account']
    myPassword = user['user']['password']
    token = user['user']['token']
    if token:
        userToken = token
    else:
        if myAccount.find('(') == 0 or myPassword.find('(') == 0:
            print('請登入系統（預設帳號密碼同學生篇），或於 user.ini 檔案設置基本資料')
            myAccount = input('學號:')
            myPassword = input('密碼:')
        userToken = Lib.getToken(myAccount, myPassword)

    nowDate = datetime.date.today()
    nowWeek = nowDate.weekday()    #Output will is 0 = Monday ... 6 = Sunday

    template = ConfigParser()
    template.read('template.ini', encoding='utf-8-sig')
    morningDo = template[WEEKS_STR[nowWeek]]['morning']
    noonDo = template[WEEKS_STR[nowWeek]]['noon']
    nightDo = template[WEEKS_STR[nowWeek]]['night']

    res = Lib.post_tempData(userToken, myAccount, envId, envName, className, str(nowDate),
        morningActivity=morningDo, noonActivity=noonDo, nightActivity=nightDo)

    if recordDay > 0:
        for backIndex in range(recordDay):
            backDay = backIndex + 1
            backDate = nowDate - datetime.timedelta(days=backDay)
            backWeek = backDate.weekday()
            morningDo = template[WEEKS_STR[backWeek]]['morning']
            noonDo = template[WEEKS_STR[backWeek]]['noon']
            nightDo = template[WEEKS_STR[backWeek]]['night']
            res = Lib.post_tempData(userToken, myAccount, envId, envName, className, str(backDate),
                morningActivity=morningDo, noonActivity=noonDo, nightActivity=nightDo)
