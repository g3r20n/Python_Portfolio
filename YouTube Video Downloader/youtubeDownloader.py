#pytube let's you interact with YouTube and all the information you need from YouTube
from pytube import YouTube

#Asking the User to input any YouTube link from youtube to download
youtTubeUrl = input("Please put your YouTube link here:" " ")

#Linking the Users responds to a variable and to the YouTube website to find a match
youTubeVideo = YouTube(youtTubeUrl)

#This prints the information from the video, the title to double check that this is the correct video
print(youTubeVideo.title)

#This get's you the video's thumbnail, for artwork purposes or whatever the User needs it for
print(youTubeVideo.thumbnail_url)

#This gets the highest resolution available from the video
youTubeVideo = youTubeVideo.streams.get_highest_resolution()

#This function calls the video from YouTube and downloads it into the same folder that your python file lives in or you can copy and paste a path inside the ()
youTubeVideo.download()