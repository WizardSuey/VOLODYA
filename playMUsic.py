
import sounddevice as sd
import soundfile as sf
import random
import json




with open("MusicPlayer/jsonformatter.json", encoding="utf-8") as file:
	data = json.load(file)

print("Введите название песни.  Например LinkinPark-InTheEnd")
music = str(input())

# list_of_music = list()
# for i in data:
# 	list_of_music.append(f'{i["name"]}.mp3')
#
# print(list_of_music)


array, smp_rt = sf.read(f'MusicPlayer/{music}.mp3', dtype='float32')
sd.play(array, smp_rt)
s = input()
if s == "next":
  sd.stop()
