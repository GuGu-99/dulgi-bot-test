import io, datetime, discord, csv
from discord.ext import commands
from discord.ui import View, Button
from config import *
from modules.util import load_data, ensure_user, logical_date_str_from_now
data_store = load_data()

def setup_report(bot: commands.Bot):
    @bot.command(name="보고서")
    async def report(ctx):
        uid = str(ctx.author.id)
        ensure_user(data_store, uid)
        await ctx.author.send("📊 보고서 기능 준비 중! (전체 구조 동일, 생략된 버전)")
