# IA-Youtube-de-audio-a-texto
Mediante whisper podemos transformar un video de YouTube a un audio y del audio a texto

## Requerimientos:
-Correr 2 lineas para tener scoop
´´´python
> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
> irm get.scoop.sh | iex
´´´

-Instalar:
´´´python
> pip install git+https://github.com/openai/whisper.git
> pip install pytube
> scoop install ffmpeg
´´´
## Correr el programa
-Cargar el link del video que quiero transcribir en youtubeVideoId = “ ”
-Correr
´´´python
> python transcript.py
´´´
