from ast import AsyncFunctionDef
import time
from datetime import date, datetime
import requests 
from main.client import asst
from pyrogram import filters
from pyrogram.types import Message


@asst.on_message(filters.command("ping") & filters.all)
async def ping(msg: Message):
    start_time = datetime.now()
    end_time = datetime.now()
    uptime = ((end_time - start_time).microseconds / 1000)
    await asst.send_message(msg.chat.id, f"**P O N G!!**\nMy MS {uptime}")