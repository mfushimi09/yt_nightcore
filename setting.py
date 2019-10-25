import os 
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# YT_DEVELOPPER_KEY = os.environ.get('YT_DEVELOPPER_KEY')
# YT_CHANNEL_ID = os.environ.get('YT_CHANNEL_ID')
# DISCORD_TOKEN =os.environ.get('DISCORD_TOKEN') 
# DISCORD_CHANNEL_ID = os.environ.get('DISCORD_CHANNEL_ID') 
# DATABASE_URL = os.environ.get('DATABASE_URL')
