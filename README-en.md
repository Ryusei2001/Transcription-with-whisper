# Transcribe and take minutes using whisper

## Overview
Using a PC's built-in microphone, etc., whisper records voice data and automatically transcribes and records the data.
Normally, whisper transcribes text from video files and other fixed-length video files. However, this program does not need to record audio data in advance, as it detects conversation breaks and transcribes each conversation.

In addition, transcription is performed by playing back pre-recorded data from a recorder or other device near the microphone, making it possible to perform transcription even when it is difficult to move the data.

## Transcription results
Transcription results are saved in a text file (Result.txt).
If you cannot find the file, please look in the same directory as mojiokoshi.py.

The format of Result.txt is as follows.
```
<Start time>==========
<Elapsed time since running>    <Text after transcription>.
```

## Execution environment
The environment at the time of testing is as follows
```
python 3.9.10
openai-whisper 20230308
soundfile 0.12.1
SpeechRecognition 3.9.0
```

## Language switching
This program is set up to transcribe from a Japanese conversation.
To change to another language, modify the program in the transcription function as follows

Transcription from Japanese (default)
````python
result = model.transcribe(audio_fp32, fp16=False, language="ja")
````
Transcribe from English
````python
result = model.transcribe(audio_fp32, fp16=False, language="en")
````
Or you can change it to transcribe regardless of language.
````python
result = model.transcribe(audio_fp32, fp16=False)
````

## Parallel processing of transcription
The program uses threads to parallelize the transcription process (default is 3 threads), to change the number of threads, modify the following part of the program: 

```python
for i in range(3): t = threading.
    Thread(target=transcription, daemon=True)
    threads.append(t)
    t.start()
```