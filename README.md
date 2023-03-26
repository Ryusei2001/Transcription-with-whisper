# whisperを利用した文字起こしと議事録作成

## 概要
PC内蔵マイクなどを使い、音声データを録音・自動で文字起こし・記録を行います。
通常whisperは動画ファイルなど固定長の動画ファイルから文字起こしをしますが、このプログラムでは会話の区切りを判別し会話ごとに文字起こしを行うため、事前に音声データを録音する必要性はありません。

また、レコーダなどで事前に録音したデータをマイク近くで再生することで文字起こしを行うため、データ移動が困難な場合でも文字起こしを行うことができます。

## 文字起こし結果
文字起こし結果はテキストファイル(Result.txt)に保存されます。
ファイルが見つからない場合はmojiokoshi.pyと同じディレクトリを探して下さい。

Result.txtの形式は以下のとおりです。
```
<開始時刻>==========
<動作してからの経過時間>	<文字起こし後の文章>
```

## 実行環境
テスト時の環境は以下のとおりです
```
python  3.9.10
openai-whisper  20230308
soundfile   0.12.1
SpeechRecognition   3.9.0
```

## 言語切り替え
このプログラムは日本語の会話から文字起こしを行うように設定しています。
他の言語に変更するにはtranscription関数内のプログラムを以下のように修正して下さい。

日本語からの文字起こし(デフォルト)
```python
result = model.transcribe(audio_fp32, fp16=False, language="ja")
```
英語からの文字起こし
```python
result = model.transcribe(audio_fp32, fp16=False, language="en")
```
もしくは言語に関係なく文字起こしを行うように変更することも可能です。
```python
result = model.transcribe(audio_fp32, fp16=False)
```

## 文字起こしの並列処理
プログラムではthreadを利用し文字起こし処理を並列処理しています(デフォルトでは3スレッド)、スレッド数を変更するにはプログラム内の以下の箇所を修正して下さい。

```python
for i in range(3):
    t = threading.Thread(target=transcription, daemon=True)
    threads.append(t)
    t.start()
```
