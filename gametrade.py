import time
import random
import requests
import os

def get_text(file_name, line_number):
   with open(file_name) as f:
      for i, line in enumerate(f, 1):
         if i == line_number:
            return line.rstrip('\n')

get_line = sum([1 for _ in open('remember_token.txt')])

f = open('remember_token.txt', 'r', encoding='UTF-8')
data = f.read().splitlines()
f.close()


def favorite(proxies=None):
   headers = {
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
   }

   if proxies is None:
      response = requests.get(URL, headers=headers)
      
   session_id = response.cookies.get_dict()["_session_id"]
   authenticity_token = response.text.split('"csrf-token" content="')[1].split('"')[0]

   cookies = {
      '_session_id': session_id,
      'remember_token': remember_token,
   }

   headers = {
      'accept': '*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript',
      'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
      'x-csrf-token': authenticity_token,
      'x-requested-with': 'XMLHttpRequest',
   }

   data = {
      'utf8': '✓',
      'button': '',
   }

   ID = str(URL).split("/")[5]
   
   if proxies is None:
      response = requests.post('https://gametrade.jp/exhibits/' + ID + '/thinkings', cookies=cookies, headers=headers,
                           data=data, allow_redirects=False)
   if response.status_code == 200:
      print("Success")
      return "Success"
   else:
      print("Failed")
      return "Failed"
   
def unfavorite(proxies=None):

   headers = {
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
   }

   if proxies is None:
      response = requests.get(URL, headers=headers)

   session_id = response.cookies.get_dict()["_session_id"]
   authenticity_token = response.text.split('"csrf-token" content="')[1].split('"')[0]

   cookies = {
      '_session_id': session_id,
      'remember_token': remember_token,
   }

   headers = {
      'accept': '*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript',
      'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
      'x-csrf-token': authenticity_token,
      'x-requested-with': 'XMLHttpRequest',
   }

   data = {
      'utf8': '✓',
      '_method': 'delete',
      'button': '',
   }

   ID = str(URL).split("/")[5]

   if proxies is None:
      response = requests.post('https://gametrade.jp/exhibits/' + ID + '/thinkings', cookies=cookies, headers=headers,
                              data=data, allow_redirects=False)

   if response.status_code == 200:
      print("success")
      return "Success"
   else:
      print("failed")
      return "Failed"


print(f"""
   ___               _____            _     
  / __|__ _ _ __  __|_   _| _ __ _ __| |___ 
 | (_ / _` | '  \/ -_)| || '_/ _` / _` / -_)
 \___\__,_|_|_|_\___||_||_| \__,_\__,_\___|                              
""")

print("1: favorite\n2: unfavorite\n")
input_data = str(input("select: "))

if input_data =="1":
   URL = str(input("link: "))
   counter = int(input(f"{get_line}アカウントあります。\n何回実行しますか？: "))
   while counter > 0:
      time.sleep(random.uniform(0.25, 0.35))
      remember_token = str(get_text('remember_token.txt', counter))
      favorite()
      counter = counter - 1
   print("実行終了！")
   input()
if input_data =="2":
   URL = str(input("link: "))
   counter = int(input(f"{get_line}アカウントあります。\n何回実行しますか？: "))
   while counter > 0:
      time.sleep(random.uniform(0.25, 0.35))
      remember_token = str(get_text('remember_token.txt', counter))
      unfavorite()
      counter = counter - 1
   print("実行終了！")
   input()