import requests
import os
import sys
import dns
import dns.resolver
import colorama
import time
import eventlet
eventlet.monkey_patch()
from colorama import Fore, Style
from requests.exceptions import ConnectionError
from requests.packages.urllib3.exceptions import InsecureRequestWarning

print(Style.BRIGHT + Fore.RED + '''

	    ___  ______  _____
	   /   |/_  __/ /__  /
	  / /| | / /      / / 
	 / ___ |/ /      / /  
	/_/  |_/_/_____ /_/   
	         /_____/
''')
print(Fore.YELLOW + '''              CODED BY : A.Tarek
''')
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def process():
	try:
		filepath = sys.argv[1]
		with open (filepath,'r') as file:
			for line in file:
				with eventlet.Timeout(2):
					try:
						r = requests.get(line.strip(),verify=False)
						print (Fore.GREEN + "Domain: {} => Status Code: {}".format(line.strip(),r.status_code))
						finall=open('http.txt','a')
						finall.write('{}'.format(line))
					except:
						print(Fore.RED+"Domain: {} => Status Code: 408".format(line.strip()))
	except:
		print ("Please enter exist subdomains file\n"+Fore.GREEN+"Usage: python status_code subdomains.txt")
		sys.exit(1)
process()
print(Fore.YELLOW + "Saved in http.txt....\n")

def cname():
	un = os.system("cat http.txt | unfurl domains > none.txt")
	print (Fore.RED + 'PREPARING FOR BEGIN SCRIPT')
	for i in range(5,0,-1):
	    time.sleep(1)
	    print(str(i) + i * " . ")
	my_resolver = dns.resolver.Resolver()
	my_resolver.nameservers = ['8.8.8.8']
	subfile=open("none.txt", 'r')
	for sub in subfile:
		try:
			subd=sub.strip()		
			answer=my_resolver.query(sub.strip(), 'CNAME')
			for data in answer:
				print(Fore.WHITE + (subd))
				print(Fore.GREEN +'C_NAME is :'+ Fore.YELLOW + str(data))
				f = open('cnames.txt','a')
				f.write('{} => {}\n\n'.format(subd,data))
		except :    
	   		print(Fore.WHITE + (sub) + Fore.RED + (' has no cname'))
	subfile.close()
cname()
print(Fore.RED + "Saved in cnames.txt....")