from vosk import Model, KaldiRecognizer
import os
import pyaudio

model = Model(r"C:\Users\user\Desktop\VOLODYA\model_small") # полный путь к модели
rec = KaldiRecognizer(model, 8000)
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=8000,
    input=True,
    frames_per_buffer=8000
)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break

    print(rec.Result())

print(rec.FinalResult())
