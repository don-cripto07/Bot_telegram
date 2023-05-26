import requests, time
from requests import Session
from bs4 import BeautifulSoup



def main ():

	
	with requests.Session() as session:
		r1 = requests.get('https://trocador.app/pt/affiliate/')
		site1 = BeautifulSoup (r1.content, 'html.parser')
		estado1 = site1.find('input', attrs={"name":"csrfmiddlewaretoken"})
		estado1_csrftoken = estado1 ['value']
		print (estado1_csrftoken)
	
		login_data = {
		"csrfmiddlewaretoken": estado1_csrftoken,
		"username": "sdmr007",  
		"password": "XXXXX", 
		"next": "/pt/affiliate/",
		}
		token_head = session.cookies
		print (token_head)
		head={
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
			"Accept-Encoding": "gzip, deflate, br",
			"Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6,es;q=0.5",
			"Cache-Control": "max-age=0",
			"Connection": "keep-alive",
			"Content-Length": "151",
			"Content-Type": "application/x-www-form-urlencoded",
			"Cookie": "csrftoken=''",
			"Host": "trocador.app",
			"Origin": "https://trocador.app",
			"Referer": "https://trocador.app/pt/affiliate/",
			"Sec-Fetch-Dest": "document",
			"Sec-Fetch-Mode": "navigate",
			"Sec-Fetch-Site": "same-origin",
			"Sec-Fetch-User": "?1",
			"Upgrade-Insecure-Requests": "1",
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",

		}
		url = 'https://trocador.app/pt/affiliate/'
		res = session.post (url, data=login_data , headers=head)
		
		print (res)

	r2 = requests.get('https://trocador.app/pt/affiliate/')
	time.sleep (1)
	print(r2.status_code)
	time.sleep (1)
	site2 = BeautifulSoup (r2.content, 'html.parser')
	estado2 = site2.find('div', attrs={'class': 'form trade-form'})
	print (estado2)
	r3 = requests.get('https://trocador.app/pt/dashboard/')
	print(r3.status_code)
if __name__ == "__main__":
    main()





''' "sec-ch-ua": "'Google Chrome';v='113', 'Chromium';v='113', 'Not-A.Brand';v='24'",
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",'''





