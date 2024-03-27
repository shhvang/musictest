from Core.io import IO
from Core.directories import dirr
from Core.git import git
from Core.assistants import Userbot
from IO.utils.misc import dbb, heroku, sudo

from Core.logging import LOGGER

dirr()
git()
dbb()
heroku()

app = IO()
userbot = Userbot()


from .platforms import *

Spotify = SpotifyAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()