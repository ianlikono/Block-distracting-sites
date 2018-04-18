import time
from datetime import datetime as dt

windows_hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
linux_hosts_path = "/etc/hosts"
temp_host = "hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com",
                "youtube.com", "www.youtube.com", "https://mail.google.com/", "twitter.com", "www.twitter.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours...")
        with open(temp_host, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" " + website+"\n")
    else:
        with open(temp_host, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
