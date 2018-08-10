from youtube_dl import YoutubeDL
# Download 1 video
# dl = YoutubeDL()
# dl.download(["https://www.youtube.com/watch?v=bqy4XFraBlk"])
# Download multiple videos
# dl.download(["https://www.youtube.com/watch?v=MjwXXFjV35w","https://www.youtube.com/watch?v=-aMdBA00Ijc"])
# Download audio
# option = {
#     "format": "bestaudio/audio"
# }
# dl = YoutubeDL(option)
# dl.download(["https://www.youtube.com/watch?v=WcAmV-4Ybwg"])
options = {
    "default_search": "ytsearch",
    "max_downloads": 1,
    "format": "bestaudio/audio"
}
dl = YoutubeDL(options)
dl.download(["Shopping Penguin Parry Gripp Song Of The Week"])