import time
from datetime import datetime as dt

temp_hosts= r"E:\PYHTON-PROJECT\webblocker\hosts"
hosts_path ="C:\Windows\System32\drivers\etc\hosts"
redirect ="127.0.0.1"
#website_lists you want to block
web_list=["https://www.facebook.com/","wwww.facebook.com","facebook.com","instagram.com","www.instagram.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,20) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,22):
        print("Working Hours")
        with open(hosts_path,'r+') as file:
            content= file.read()
            for website in web_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content= file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in web_list):
                    file.write(line)
                file.truncate()
        print("Gaming time")
    time.sleep(5)
