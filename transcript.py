import pytube
import whisper

#para que funcione correr python transcript.py

youtubeVideoId = "https://www.youtube.com/watch?v=cz-DaqClllQ"
model = whisper.load_model('small')

youtubeVideo = pytube.YouTube(youtubeVideoId)
audio = youtubeVideo.streams.get_audio_only()
audio.download(filename='tmp.mp3')

result = model.transcribe('tmp.mp3')

print(result["text"])