    # Credit @LazyDeveloper.
    # Please Don't remove credit.
    # Born to make history @LazyDeveloper !

    # Thank you LazyDeveloper for helping us in this Journey
    # 🥰  Thank you for giving me credit @LazyDeveloperr  🥰

    # for any error please contact me -> telegram@LazyDeveloperr or insta @LazyDeveloperr 

from pyrogram import Client
from info import *

LazyPrincessBot = Client(
    name=SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "plugins"},
    sleep_threshold=SLEEP_THRESHOLD,
    workers=WORKERS
)

multi_clients = {}
work_loads = {}
