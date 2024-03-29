from .userbot import *
from .dir import *
from .git import *
from .bot import *
from .logging import *
from .misc import dbb, heroku, sudo

dirr()
git()
dbb()
heroku()

app = IOST()
userbot = Userbot()

from .platforms import *

Spotify = SpotifyAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
Carbon = CarbonAPI()