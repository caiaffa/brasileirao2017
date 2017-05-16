from urllib.request import urlopen
from bs4 import BeautifulSoup

get_html = urlopen("http://www.cbf.com.br/competicoes/brasileiro-serie-a/equipes/2017#.WRWm5O1Bu01")
html = BeautifulSoup(get_html.read(), 'html.parser')

teamList = html.findAll('div', class_="cell")

for team in teamList:
	links = team.findAll('a')
	for link in links:
		get_html = urlopen(link['href'])
		html = BeautifulSoup(get_html.read(), 'html.parser')
		jogoList = html.findAll('div', class_="tabela-jogos")

		print ("=========================BEGIN================================")
		print (link['title'])

		for jogo in jogoList:
			date = jogo.find('h4', class_="blue blue2").text.strip()
			hour = jogo.find('div', class_="full-game-time").text.strip()
			team1 = jogo.find('div', class_="game-team-1").text.strip()
			team2 = jogo.find('div', class_="game-team-2").text.strip()
			location = jogo.find('div', class_="full-game-location-changes").text.strip() 
			location = location[10:].strip()
			print(date, hour, team1,team2, location)
		
		print ("===========================END================================")


'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
from threading import Thread

get_html = urlopen("http://www.cbf.com.br/competicoes/brasileiro-serie-a/equipes/2017#.WRWm5O1Bu01")
html = BeautifulSoup(get_html.read(), 'html.parser')

teamList = html.findAll('div', class_="cell")

def set_url(url):
	get_html = urlopen(url)
	html = BeautifulSoup(get_html.read(), 'html.parser')
	jogoList = html.findAll('div', class_="tabela-jogos")

	print ("=========================BEGIN================================")
	print (link['title'])

	for jogo in jogoList:
		date = jogo.find('h4', class_="blue blue2").text.strip()
		hour = jogo.find('div', class_="full-game-time").text.strip()
		team1 = jogo.find('div', class_="game-team-1").text.strip()
		team2 = jogo.find('div', class_="game-team-2").text.strip()
		location = jogo.find('div', class_="full-game-location-changes").text.strip() 
		location = location[10:].strip()
		print(date, hour, team1,team2, location)
	
	print ("===========================END================================")


for team in teamList:
	links = team.findAll('a')
	for link in links:
		url = link['href']
		t = Thread(target=set_url, args=(url,))
		t.start()
'''