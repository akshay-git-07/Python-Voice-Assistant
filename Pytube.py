from pytube import YouTube

path = 'G:\Python'
link = 'https://www.youtube.com/watch?v=LXb3EKWsInQ'
yt = YouTube(link)
videos = yt.streams.filter(file_extension='mp4').all()

i = 1
for stream in videos:
    # print(str(i) + ' ' + str(stream))
    print(stream.default_filename)
    print(stream.mime_type, stream.resolution, stream.fps, stream.filesize, stream.includes_video_track, stream.includes_audio_track)
    i += 1
index = int(input('Select Quality: '))
video = videos[index - 1]
# video.download(path)
# print('Downloaded')
