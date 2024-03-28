from .userbot import *
from .call import *
from .dir import *
from .git import *
from .bot import *
from .logging import *
from .misc import dbb, heroku, sudo
from .mongo import *

dirr()
git()
dbb()
heroku()
sudo()

app = IOS()
assistant = Userbot()


from IO.platforms import *

Spotify = SpotifyAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
