import simplematrixbotlib as botlib
import requests
import shutil
from urlextract import URLExtract
from bs4 import BeautifulSoup

#searches messages for yt links and returns them if in message
#otherwise returns null or whatever python does here idk
def containsYoutubeLink(message):
   #
   #return
   extractor = URLExtract()
   link = extractor.find_urls(message.body)
   return link[0]


#Sends the thumbnail from a link in a room
async def postThumbnail(room, bot, soup):
    #data = requests.get("http://img.youtube.com/vi/" + videoId + "/hqdefault.jpg", stream = True)
    #this needs to become soup
    #write file
    #

    data = requests.get(soup.find("meta", property="og:image")["content"], stream = True)
    with open("thumbnail.jpg", "wb") as f:
        shutil.copyfileobj(data.raw, f)

    await bot.api.send_image_message(room.room_id, 'thumbnail.jpg')

    return

#Sends the title from a link in a room
async def postTitle(room, bot, soup):

    #title = YouTube("https://www.youtube.com/watch?v=" + videoId).title
    #r = requests.get("https://www.youtube.com/watch?v=" + videoId)
    #s = BeautifulSoup(r.text, "html.parser")
    #title = s.find("meta", itemprop="name")["content"]
    #
    title = soup.find("meta", itemprop="name")["content"]
    await bot.api.send_text_message(room_id=room.room_id, message=title, msgtype='m.text')

    return

def getSoup(videoLink):
    r = requests.get(videoLink)
    s = BeautifulSoup(r.text, "html.parser")
    return s



#The new input for a youtube message
async def youtubeResponse(room, bot, message):
   videoLink = containsYoutubeLink(message)
   #now get the soup object to get info from
   #
   if videoLink:
      soup = getSoup(videoLink)

      #use soup to send what you want about the video
      await postThumbnail(room, bot, soup)
      await postTitle(room, bot, soup)
   return
