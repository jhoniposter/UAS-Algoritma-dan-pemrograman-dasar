""" Program python - Website Blocker
----------------------------------------
"""
import time
from datetime import datetime as dt
 
#r adalah raw untuk string
hosts_path = r"C://Windows//System32//drivers//etc"  
hosts_temp = "hosts"
redirect = "127.0.0.1"
#User dapat memilih website yang akan di blok
web_sites_list = ["www.facebook.com", "facebook.com"]    
while True:
   if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,22):
       print("Waktu kerja")
       with open(hosts_path, "r+") as file:
           content = file.read()
           for website in web_sites_list:
               if website in content:
                   pass
               else:
                   file.write(redirect+" "+website+"\n")
   else:
       print("Fun time")
       with open(hosts_path, "r+") as file:
           content = file.readlines()
           file.seek(0)   # reset pointer ke bagian atas file text
           for line in content:
            # overwrite seluruh file
               if not any(website in line for website in web_sites_list):
                   file.write(line)
                
           file.truncate() # Baris ini di gunakan untuk menghapus baris (termasuk DNS)
   time.sleep(5)
