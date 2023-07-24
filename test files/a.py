import requests
import certifi

requests.packages.urllib3.disable_warnings()

url = 'https://api.system.talentely.com/api/user/v1/login'

payload = {
  "username": "20cs008@kcgcollege.com",
  "password": "vidhai",
  "deviceInfo": {
    "name": "Chrome",
    "version": "115.0.0.0",
    "layout": "Blink",
    "os": {
      "architecture": 64,
      "family": "Windows",
      "version": "10"
    },
    "product": None,
    "isMobile": False
  }
}

payload2 = {
  "username": "20cs008@kcgcollege.com",
  "password": "vidhai"  
}

headers = {
    'Content-Type' : 'application/json',
    'Authorization' : 'bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjA2NzFlOTQ4LWE2OTktNGI4Yi1iNTU3LTA2OTQ1MjExNTQ5ZCIsIm5hbWUiOiIyMENTMDA4QGtjZ2NvbGxlZ2UuY29tIiwidXNlclR5cGUiOjMsInVzZXJUeXBlTmFtZSI6IlN0dWRlbnQiLCJjcmVhdGVkT24iOjE2Nzk0OTkwNjksImVtYWlsIjoiMjBDUzAwOEBrY2djb2xsZWdlLmNvbSIsImlhdCI6MTY5MDIwMjkyNiwiZXhwIjoxNjkzMjAyOTI2fQ._pU9qAU8KHHRKhe6hJBUCZnx6GZ1cE-SFBA9UtIZqNw'
}

with requests.Session() as session:
    session.verify = certifi.where()
    response = session.post(url,headers = headers, json = payload2)

    print(response.satus_code, response.url)

    with open('a.html', 'wb') as file:
        file.write(response.content)
