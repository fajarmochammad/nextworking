import requests

try:
    r = requests.get('https://fac ebook.com')
    print (r.status_code)
    if r.status_code == 200:
        print (r.text)
except Exception as e:
    print ('Errornya ', e)        