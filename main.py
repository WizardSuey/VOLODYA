import queue
import sounddevice as sd  # Получение доступа к микрофону
import vosk
import json
import values
import words
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import voice
from skills import *
import skills
import datetime
import os
# Создаём экземпляр класса,
q = queue.Queue()

model = vosk.Model('model_small')  # голосовую модель vosk нужно поместить в папку с файлами проекта

device = sd.default.device  # <--- по умолчанию
# или -> sd.default.device = 1, 3, python -m sounddevice просмотр
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])  # получаем частоту микрофона


def callback(indata, frames, time, status):
	'''
	    Добавляет в очередь семплы из потока.
	    вызывается каждый раз при наполнении blocksize
	    в sd.RawInputStream'''
	#how create contantu in python

	q.put(bytes(indata))


def recognize(data, vectorizer, clf):
	'''
	    Анализ распознанной речи
	    '''
	global trg
	# проверяем есть ли имя бота в data, если нет, то return
	trg = words.TRIGGERS.intersection(data.split())
	if not trg:
		return
	# удаляем имя бота из текста
	data.replace(list(trg)[0], '')
	# print(len(data.replace(list(trg)[0], '')))
	# print(data.replace(list(trg)[0], ''))
	if len(data.replace(list(trg)[0], '')) <= 0:
		voice.speaker('че')
	else:
		text_vector = vectorizer.transform([data]).toarray()[0]
		answer = clf.predict([text_vector])[0]
		# получение имени функции из ответа из data_set
		func_name = answer.split()[0]
		# озвучка ответа из модели data_set
		voice.speaker(answer.replace(func_name, ''))
		# запуск функции из skills
		exec(func_name + '()')
	
	

def main():
	'''
	    Обучаем матрицу ИИ
	    и постоянно слушаем микрофон
	    '''
	
	os.system('cls')
	voice.speaker('Здравствуйте! Как вас зовут?')

	def user_check():

		while True:
			values.user_name = str(input())
			voice.speaker(f'{values.user_name}, верно?')
			user_answer = str(input().lower())
			
			if user_answer == 'да':
				voice.speaker(f'Приятно познакомится, {values.user_name}')
				voice.speaker('Я начал работать')
				vectorizer = CountVectorizer()
				vectors = vectorizer.fit_transform(list(words.data_set.keys()))
				clf = LogisticRegression()
				clf.fit(vectors, list(words.data_set.values()))
				del words.data_set
				# постоянная прослушка микрофона
				with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype="int16", channels=1, callback=callback):
					# Запускается экземпляр vosk
					rec = vosk.KaldiRecognizer(model, samplerate)
					while True:
						data = q.get()
						if rec.AcceptWaveform(data):
							data = json.loads(rec.Result())['text']
							recognize(data, vectorizer, clf)
							# print(data)
			elif user_answer == 'нет':
				voice.speaker('Как вас зовут?')
				user_check()
	user_check()
if __name__ == "__main__":
	main()
