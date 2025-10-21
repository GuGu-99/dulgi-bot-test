# -*- coding: utf-8 -*-
# 둘기봇 v5.6 — 모듈화 안정버전 (Render Starter 호환)
# 기능: 출근 / 점수 / 보고서 / 자동백업 / Flask KeepAlive

import os
import discord
from discord.ext import commands

from modules.activity import setup_activity
from modules.report import setup_report
from modules.backup import setup_backup
from modules.util import keep_alive

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ 로그인 완료: {bot.user}")
    keep_alive()
    await setup_backup(bot)

# 기능별 모듈 등록
setup_activity(bot)
setup_report(bot)

if __name__ == "__main__":
    TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("❌ DISCORD_BOT_TOKEN 환경변수가 설정되지 않았습니다.")
