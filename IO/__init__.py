from Core.io import IO
from Core.dir import dirr
from Core.git import git
from Core.assistant import assistant
from IO.utils.misc import dbb, heroku, sudo

from Core.logging import LOGGER

dirr()
git()
dbb()
heroku()

app = IO()
userbot = assistant()


from .platforms import *

Spotify = SpotifyAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()