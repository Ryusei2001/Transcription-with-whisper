from io import BytesIO
import numpy as np
import soundfile as sf
import speech_recognition as sr
import whisper
import queue
import threading
import time
from datetime import datetime

start_time = time.time()
q = queue.Queue()
r = sr.Recognizer()
now = datetime.now()
date_time = now.strftime("%Y/%m/%d %H:%M:%S")
#Load whisper model
print("Loading model...")
model = whisper.load_model("medium")
print("Load complete!")
#Write TimeStamp
with open('Result.txt', 'a') as f:
    f.write(date_time + '==========' + '\n')

def transcription():
    while True:
        time, audio = q.get(timeout=None)
        wav_bytes = audio.get_wav_data()
        wav_stream = BytesIO(wav_bytes)
        audio_array, _ = sf.read(wav_stream)
        audio_fp32 = audio_array.astype(np.float32)
        #Transcription in Japanese
        result = model.transcribe(audio_fp32, fp16=False, language="ja")
        #Print pre-result
        minutes, seconds = divmod(time, 60)
        print("{}:{}\t{}".format(int(minutes), int(seconds), result["text"]))
        #Write transcription results to file
        script_str = str(int(minutes)) + ":" + str(int(seconds)).zfill(2) + "\t" +  result["text"]
        with open('Result.txt', 'a') as f:
            f.write(script_str + '\n')


def timer():
    while True:
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(elapsed_time, 60)
        print("T+: {}m {}s".format(int(minutes), int(seconds)))
        time.sleep(1)


#Multiple threads for parallel processing
threads = []
for i in range(3):
    t = threading.Thread(target=transcription, daemon=True)
    threads.append(t)
    t.start()
thread_time = threading.Thread(target=timer, daemon=True)
thread_time.start()

while True:
    print(".")  #Start record your voice
    with sr.Microphone(sample_rate=16000) as source:
        audio = r.listen(source)
    q.put((time.time() - start_time, audio))
    print("..") #finish recording