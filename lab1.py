import requests  # εισαγωγή της βιβλιοθήκης
import datetime

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

#nurl = 'http://python.org/'  # προσδιορισμός του url

 #with requests.get(url) as response:  # το αντικείμενο response
 #   html = response.text
#  more(html)


url=input("Give url:\t")

if not url.startswith('https://'):
    url='https://'+ url
print(url)

with requests.get(url) as response:
    headers = response.headers
    for key in headers:
        print(f"Name:{key}:{headers[key]}")


print(f"Server:{response.headers.get('Server')}")

print(f"Has cookies:{'Set-Cookie' in response.headers}")

if "set-cookie" in headers.keys():
        cookies = response.cookies
        for cookie in cookies:
            print(f"\nThe site uses cookie.\nName: {cookie.name}\nValue: {cookie.value}\nExpiration Date: {datetime.datetime.fromtimestamp(float(cookie.expires)) if cookie.expires is not None else 'Does Not Expire'}")        
else:
    print('\nThe site does not use cookies')
