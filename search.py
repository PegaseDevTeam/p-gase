#!/usr/local/bin/python3
# coding: utf-8 
#https://osintframework.com/
from requests import get
from fuzzywuzzy import fuzz
from googlesearch import search
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init
import os 
from pegase import *
""" requirements : 
requests
beautifulsoup4
colorama
google
fuzzywuzzy
python-Levenshtein
"""
# colorama
init(autoreset=True)
clearScr()
# Logo

logo()	
query   = input(Back.BLACK + Fore.YELLOW + pegasePrompt + Back.RESET + Fore.GREEN)
results = 100

print(Fore.GREEN + '[~] Searching ' + query)
for url in search(query, stop = results):
	print('\n' + Fore.CYAN + '[+] Url detected: ' + url)
	try:
		text = get(url, timeout = 1).text
	except:
		continue
	soup = BeautifulSoup(text, "html.parser")
	links_detected = []
	try:
		print(Fore.MAGENTA + '[?] Title: ' + soup.title.text.replace('\n', ''))
	except:
		print(Fore.RED + '[?] Title: null')
	# Find by <a> tags
	try:
		for link in soup.findAll('a'):
			href = link['href']
			if not href in links_detected:
				if href.startswith('http'):
					# Filter
					if url.split('/')[2] in href:
						links_detected.append(href)
					# If requested data found in url
					elif query.lower() in href.lower():
						print(Fore.GREEN + '--- Requested data found at link : ' + href)
						links_detected.append(href)
					# If text in link and link location is similar
					elif fuzz.ratio(link.text, href) >= 60:
						print(Fore.GREEN + '--- Text and link are similar : ' + href)
						links_detected.append(href)
	except:
		continue
	if links_detected == []:
		print(Fore.RED + '--- No data found')


