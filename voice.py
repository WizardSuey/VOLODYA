import pyttsx3






#Инициализация голосового "движка" при старте программы
engine = pyttsx3.init()
#Голос берется из системы, первый попавшийся
engine.setProperty('rate', 10000)#скорость речи
voice_id = 'ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_IRINA_11.0'
engine.setProperty('voice', voice_id)


def speaker(text):

	'''Озвучка текста'''
	print(text)
	engine.say(text)
	engine.runAndWait()