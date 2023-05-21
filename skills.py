import datetime
import os, webbrowser, sys, requests, subprocess, pyttsx3, voice, time, random
from bs4 import BeautifulSoup as BS
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import sounddevice as sd  # Получение доступа к микрофону
import vosk
import queue
from translate import Translator
from main import main, recognize, callback
import pyglet
import sounddevice as sd
import soundfile as sf
from main import recognize
import json
import values
from main import *
import queue
import sounddevice as sd  # Получение доступа к микрофону
import vosk
import json
import values
import words
import os

# Иницилизация голосового "движка" при страрте программы
engine = pyttsx3.init()
engine.setProperty('rate', 180)


def browser():
	'''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''

	webbrowser.open('https://www.youtube.com', new=2)

def music():
	webbrowser.open('https://music.yandex.ru/users/dorogino@gmail.com/playlists/3', new=2)

def nowTime():

	now = datetime.datetime.now()
	now_time = now.strftime("%H:%M")

	voice.speaker(f"сейчас время {now_time}")

def game():
	'''Нужно разместить путь к exe файлу любого вашего приложения'''
	try:
		subprocess.Popen('F:\SteamLibrary\steamapps\common\War Thunder\launcher.exe')
	except:
		voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')


def offpc():
	# Эта команда отключает ПК под управлением Windows

	os.system('shutdown \s')
	print('пк был бы выключен, но в коде мешает #;)))')

def joke():
		try:
			headers = {
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
				"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0 (Edition Yx GX)"
				}
			page_count = 10
			for page in range(1, page_count + 1):
				#time.sleep(3)

				url = f"https://www.anekdot.ru/author-best/years/?years=anekdot&page={page}"
				req = requests.get(url=url, headers=headers)
				soup = BS(req.text, "lxml")

				data = soup.find_all("div", class_="topicbox")

				list_of_jokes = list()
				for jock in data:
					anekdot = jock.find_next("div", class_="text").text
					list_of_jokes.append(anekdot)

			random.shuffle(list_of_jokes)
			voice.speaker(list_of_jokes[0])

		except:
			voice.speaker("Не удалось выполнить запрос, проверьте работоспособность команды")

def weather():
	try:
		url = "https://pogoda.ngs.ru"
		headers = {
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
			"user - agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 111.0.0.0 Safari / 537.36 OPR / 97.0 .0 .0(Edition Yx GX)"
		}


		req = requests.get(url=url, headers=headers)
		soup = BS(req.text, "lxml")
		# with open("index.html", "w", encoding="utf-8") as file:
		#    file.write(req.text)
		# print(soup)
		temp = soup.find("span", class_="value__main")
		temp_continue = soup.find("span", class_="value-description")

		voice.speaker("сейчас " + temp.text + " градуса " + temp_continue.text)

	except:
		voice.speaker("Не удалось выполнить запрос, проверьте работоспособность команды")

	# print('погода')
def openVk():
	try:
		webbrowser.open('https://vk.com', new=2)
	except:
		voice.speaker("Не удалось выполнить запрос, проверьте работоспособность команды")

def openBrowser():
	try:
		class MainWindow(QMainWindow):
			'''Нафигация в браузере'''

			def __init__(self, *args, **kwargs):
				super(MainWindow, self).__init__(*args, **kwargs)
				self.browser = QWebEngineView()
				self.browser.setUrl(QUrl("http://google.com"))

				self.setCentralWidget(self.browser)  # Чтобы браузер открывался в центре

				navtb = QToolBar()
				self.addToolBar(navtb)

				# Кнопка назад
				back_btn = QAction("Назад", self)
				back_btn.triggered.connect(self.browser.back)
				navtb.addAction(back_btn)
				# Кнопка вперёд
				next_btn = QAction("Вперед", self)
				next_btn.triggered.connect(self.browser.forward)
				navtb.addAction(next_btn)
				# Кнопка перезагрузки
				reload_btn = QAction("Перезагрузить", self)
				reload_btn.triggered.connect(self.browser.reload)
				navtb.addAction(reload_btn)
				# Строка редактирования
				self.urlbar = QLineEdit()
				self.urlbar.returnPressed.connect(self.navigate_to_url)
				navtb.addWidget(self.urlbar)
				self.show()

				self.browser.urlChanged.connect(self.update_urlbar)
				self.browser.loadFinished.connect(self.update_title)

			# Способ обновления окна
			def update_title(self):
				title = self.browser.page().title()
				self.setWindowTitle("% s - Браузер от MaxShowPro" % title)

			# Строковое редактирование при нажатие кнопки назад
			def navigate_to_url(self):
				q = QUrl(self.urlbar.text())
				if q.scheme() == "":
					q.setScheme("https")
				self.browser.setUrl(q)

			# Способ обновления url
			def update_urlbar(self, q):
				self.urlbar.setText(q.toString())
				self.urlbar.setCursorPosition(0)
		#

		app = QApplication(sys.argv)
		window = MainWindow()
		app.exec_()
	except:
		voice.speaker("Не удалось выполнить запрос, проверьте работоспособность команды")

def openPinterest():
	try:
		webbrowser.open('https://ru.pinterest.com', new=2)
	except:
		voice.speaker("Не удалось выполнить запрос, проверьте работоспособность команды")

def dota():
	try:
		subprocess.Popen('G:\Steam\steam.exe')
	except:
		voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')

def enTranslator():
	try:
		while True:
			translator = Translator(from_lang="ru", to_lang="en")
			text = str(input())
			if text == "off":
				callback()
				recognize()
				main()
			else:
				end_text = translator.translate(text)
				print(end_text)

	except:
		voice.speaker("переводчик выключен, продолжаю работать")

def kzTranslator():
	try:
		while True:
			translator = Translator(from_lang="ru", to_lang="kk")
			text = str(input())
			if text == "off":
				callback()
				recognize()
				main()
			else:
				end_text = translator.translate(text)
				print(end_text)
	except:
		voice.speaker("переводчик выключен, продолжаю работать")


'''МУЗЫКА'''
with open("MusicPlayer/jsonformatter.json", encoding="utf-8") as file:
	data = json.load(file)
list_of_music = list()


def playMusic():
	try:
		
		for i in data:
			list_of_music.append(f'{i["name"]}.mp3')
		random.shuffle(list_of_music)
		rand_mus = f'MusicPlayer/Musics/{list_of_music[0]}'
		array, smp_rt = sf.read(rand_mus, dtype='float32')
		del list_of_music[0]
		print(list_of_music)
		sd.play(array, smp_rt)
		pass
	except:
		voice.speaker("Не удалось выполнить запрос, проверьте работоспособность команды")

def nextMusic():
	try:
		
		rand_mus = f'MusicPlayer/Musics/{list_of_music[0]}'
		array, smp_rt = sf.read(rand_mus, dtype='float32')
		del list_of_music[0]
		print(list_of_music)
		sd.play(array, smp_rt)
		pass
		if len(list_of_music) == 0:
			voice.speaker("Это последняя песня")
			pass
	except:
		voice.speaker("Не удалось выполнить запрос, проверьте работоспособность команды")

def playSong():
	print("Пример написания песни LinkinPark-InTheEnd")
	music = str(input())
	array, smp_rt = sf.read(f'MusicPlayer/Musics/{music}.mp3', dtype='float32')
	sd.play(array, smp_rt)
	pass

def name():
	try:
		voice.speaker(f'Вас зовут {values.user_name}')
	except:
		voice.speaker("Не удалось выполнить запрос, проверьте работоспособность команды")
	
def stopMusic():
	sd.stop()
''''''
def kontinue():
	pass


def offBot():
	sys.exit()


def passive():
	pass
