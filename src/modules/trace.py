import tracemoepy
from pyrogram import filters
from telegram.ext.dispatcher import run_async
from telegram.ext import CommandHandler
from src import dispatcher
import os

tracemoe = tracemoepy.tracemoe.TraceMoe()

@run_async
def whatanime(_,message):
  reply = message.reply_to_message
  if reply and reply.media:
    path = reply.download()
    info = tracemoe.search(path, upload_file=True)
    data = f"Match: {info.result[0].anilist.title.romaji}\nSimilarity: {info.result[0].similarity*100}"
    info.result[0].save(f"{reply.from_user.id}.mp4", mute = False)
    reply.reply_document(f"{reply.from_user.id}.mp4" , caption=data)
    os.remove(f"{reply.from_user.id}.mp4")

__help__ = """
Find which anime a gif, video or image is from using trace.moe API.

/whatanime (on reply to media) - initiate search  
"""
__mod_name__ = "Trace.moe"

WHATANIME_HANDLER = CommandHandler("whatanime", whatanime)

dispatcher.add_handler(WHATANIME_HANDLER)
  
