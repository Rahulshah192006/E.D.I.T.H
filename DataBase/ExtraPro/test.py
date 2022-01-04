from pytube import YouTube
youtube_link = 'https://www.youtube.com/watch?v=Cv1CPGvYX48'
y = YouTube(youtube_link)
t = y.streams.filter(only_audio=True).all()
t[0].download(output_path="D:\\")