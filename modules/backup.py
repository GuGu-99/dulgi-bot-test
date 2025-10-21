import asyncio, datetime, io, aiohttp, discord, os
from discord.ext import commands
from modules.util import load_data, save_data, DATA_FILE, BACKUP_FILE
from config import BACKUP_CHANNEL_ID, KST

def backup_now():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = f.read()
        with open(BACKUP_FILE, "w", encoding="utf-8") as f:
            f.write(data)
        return True
    return False

async def schedule_daily_backup_loop(bot):
    while True:
        now = datetime.datetime.now(KST)
        nxt = now.replace(hour=6, minute=0, second=0, microsecond=0)
        if nxt < now: nxt += datetime.timedelta(days=1)
        await asyncio.sleep((nxt - now).total_seconds())
        if backup_now():
            ch = bot.get_channel(BACKUP_CHANNEL_ID)
            if ch:
                await ch.send(f"☀️ [{datetime.datetime.now(KST)}] 오전 6시 자동 백업 완료!",
                              file=discord.File(BACKUP_FILE))

async def setup_backup(bot):
    bot.loop.create_task(schedule_daily_backup_loop(bot))
