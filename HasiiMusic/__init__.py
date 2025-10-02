from HasiiMusic.core.bot import JARVIS
from HasiiMusic.core.dir import dirr
from HasiiMusic.core.git import git
from HasiiMusic.core.userbot import Userbot
from HasiiMusic.misc import dbb, heroku
from HasiiMusic.logging import LOGGER

dirr()
git()
dbb()
heroku()

app = JARVIS()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
