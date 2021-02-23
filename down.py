import pytube
from pytube.__main__ import YouTube

url = input("Enther your URL: ")
playlist = pytube.Playlist(url)

print("No of Videos: %s" % len(playlist.video_urls))

for url in playlist.video_urls:
    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    video.download(r'C:\Users\Arnaav\Desktop\Instrumental')
print("Thanks for using this video downloader made by Arnaav Singh")