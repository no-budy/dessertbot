import simplematrixbotlib as botlib
import yaml
import youtubeMessageResponse


with open('config.yml', "r") as file:
 botConfigFile = yaml.safe_load(file)

#Setup the bot config
config = botlib.Config()
config.encryption_enabled = botConfigFile['config']['EncryptionEnabled']
config.emoji_verify = botConfigFile['config']['EmojiVerify']
config.ignore_unverified_devices = botConfigFile['config']['ignore_unverified_devices']
config.store_path = "./crypto_store"
config.session_stored_file="session.txt"

#maybe i'll add commands later
PREFIX = botConfigFile['config']['PREFIX']



creds = botlib.Creds(homeserver=botConfigFile['config']['homeserver'],
                     username=botConfigFile['config']['username'],
                     password=botConfigFile['config']['password'])

bot = botlib.Bot(creds, config)


@bot.listener.on_message_event
async def youtubeLinks(room, message):
    match = botlib.MessageMatch(room, message, bot)
    #using the match is a great way to avoid using bs4 to parse every message or send something that
    #doesn't even contain a link
    if match.is_not_from_this_bot and (match.contains("youtube.com") or match.contains("youtu.be")):
       await youtubeMessageResponse.youtubeResponse(room, bot, message)


#Finally start bot
bot.run()
