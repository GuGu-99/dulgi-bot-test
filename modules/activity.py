import datetime, discord, asyncio
from discord.ext import commands
from discord.ui import View, Button
from config import *
from modules.util import load_data, save_data, ensure_user, logical_date_str_from_now

data_store = load_data()

def add_activity_logic(data, uid, date_str, channel_id):
    ensure_user(data, uid)
    conf = CHANNEL_POINTS.get(channel_id)
    if not conf: return False
    pts, ch_max = conf["points"], conf["daily_max"]
    u = data["users"][uid]
    if date_str not in u["activity"]:
        u["activity"][date_str] = {"total": 0, "by_channel": {}}
    today = u["activity"][date_str]
    prev = today["by_channel"].get(str(channel_id), 0)
    if prev + pts > ch_max: return False
    today["by_channel"][str(channel_id)] = prev + pts
    today["total"] += pts
    return True

def setup_activity(bot: commands.Bot):
    @bot.command(name="출근")
    async def check_in(ctx):
        uid = str(ctx.author.id)
        today = logical_date_str_from_now()
        ensure_user(data_store, uid)
        u = data_store["users"][uid]

        if today in u["attendance"]:
            v = View(); v.add_item(Button(label="서버로 돌아가기 🏠", url=SERVER_URL))
            return await ctx.author.send("이미 출근 완료 🕐\n매일 오전 6시에 초기화됩니다.", view=v)

        u["attendance"].append(today)
        add_activity_logic(data_store, uid, today, 1423359791287242782)
        save_data(data_store)
        await ctx.author.send("✅ 출근 완료! (+4점) 오늘도 힘내요!")

    @bot.event
    async def on_message(msg):
        if msg.author.bot:
            return
        cid, uid = msg.channel.id, str(msg.author.id)
        conf = CHANNEL_POINTS.get(cid)
        if not conf:
            await bot.process_commands(msg)
            return

        countable = True
        if conf.get("image_only"):
            countable = any(a.content_type and a.content_type.startswith("image/") for a in msg.attachments)
        if cid == 1423171509752434790:
            link = any(x in msg.content for x in ["http://", "https://"])
            attach = len(msg.attachments) > 0
            countable = link or attach
        if not countable:
            await bot.process_commands(msg)
            return

        added = add_activity_logic(data_store, uid, logical_date_str_from_now(), cid)
        if added:
            save_data(data_store)
        await bot.process_commands(msg)
