from Core import LOGGER, IOS, dirr, git, assistant
from IO.utils.misc import dbb, heroku, sudo

dirr()
git()
dbb()
heroku()

app = IOS()
userbot = assistant()


from .platforms import *

Spotify = SpotifyAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()