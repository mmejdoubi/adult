import requests

#param url 
AWB_SIGNIN_URL = 'https://attijarinet.attijariwafa.com/particulier/security_check'
AWB_SUCCESS_URL = 'https://attijarinet.attijariwafa.com/particulier/home'
AWB_BALANCE_URL = 'https://attijarinet.attijariwafa.com/particulier/consultation/compte/balancetempsreel'

login_payload = {'j_username':'yyyyyyyyyy', 'j_password':'xxxxxxxxx'}

login_request = requests.post(AWB_SIGNIN_URL,data=login_payload, allow_redirects=True)
print("Sending login info... \n","="*80)
print("status_code => {}", format(login_request.status_code))

jsessionid0 = login_request.history[0].cookies["JSESSIONID"]

print("Storing JSESSIONID {}", format(jsessionid0))

if login_request.url == AWB_SUCCESS_URL:
    print("Current URL OK !...Cheers !")


# Requete pour recuperer info solde
import time
ts = str(int(time.time()*1000))
print("BALANCE RETRIEVE @TS \n",'='*80)
print(ts)

balance_headers = {
'content-type':'application/json; charset=utf-8',
'accept':'application/json, text/javascript, */*; q=0.01',
'referer': 'https://attijarinet.attijariwafa.com/particulier/home',
'x-requested-with':'XMLHttpRequest',
'pragma':'no-cache',
'DNT':'1',
'cache-control':'no-cache',
'connection':'keep-alive',
'accept-encoding':'gzip, deflate',
'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
'accept-language':'en,fr;q=0.9'
}

balance_request = requests.get(url=AWB_BALANCE_URL, headers=balance_headers, cookies={"JSESSIONID": jsessionid0})
print('Balance Request status code =>', balance_request.status_code)
print('Balance Request JSON output =>', balance_request.content)

#decoder le content en json


