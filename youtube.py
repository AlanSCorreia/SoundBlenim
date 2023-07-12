from pytube import YouTube

text = 'https://www.youtube.com/watch?v=CUr3UVRBO5I&t=294s'
yt = YouTube(text)
stream = yt.streams.filter(only_audio=True).first()
stream.download()
