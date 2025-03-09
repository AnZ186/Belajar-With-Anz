import youtube_dl

url = input("Enter the URL of the video: \n")

with youtube_dl.YoutubeDL() as ydl:
    ydl.download([url])