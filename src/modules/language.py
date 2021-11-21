import os
import telegram
import importlib
import re

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, User, CallbackQuery
from telegram import Message, Chat, Update, Bot
from telegram.error import BadRequest
from telegram.ext import CommandHandler, run_async, DispatcherHandlerStop, MessageHandler, Filters, CallbackQueryHandler
from src import dispatcher, LOGGER
from src.modules.disable import DisableAbleCommandHandler
from src.modules.helper_funcs.chat_status import user_admin_no_reply, user_admin

from src.modules.sql import languages_sql as sql

LOADED_LANGS_ID = []
LANGS_TEXT = {}
FUNC_LANG = {}

for x in os.listdir('src/modules/langs'):
	if os.path.isdir('emilia/modules/langs/'+x):
		continue
	x = x.replace('.py', '')
	LOADED_LANGS_ID.append(x)
	imported_langs = importlib.import_module("emilia.modules.langs." + x)
	FUNC_LANG[x] = imported_langs
	LANGS_TEXT[x] = imported_langs.__lang__

LOGGER.info("{} languages loaded: {}".format(len(LOADED_LANGS_ID), LOADED_LANGS_ID))

def tl(message, text):
	if type(message) == int or type(message) == str and message[1:].isdigit():
		getlang = sql.get_lang(message)
		if getlang == 'None' or not getlang:
			getlang = 'en'
	else:
		getlang = sql.get_lang(message.chat.id)
		if getlang == 'None' or not getlang:
			if message.from_user.language_code:
				if message.from_user.language_code in LOADED_LANGS_ID:
					sql.set_lang(message.chat.id, message.from_user.language_code)
					getlang = message.from_user.language_code
				else:
					sql.set_lang(message.chat.id, 'en')
					getlang = 'en'
			else:
				sql.set_lang(message.chat.id, 'en')
				getlang = 'en'

	getlangid = {}
	for x in LOADED_LANGS_ID:
		getlangid[x] = x

	if str(getlang) == 'id':
		get = getattr(FUNC_LANG['id'], 'id')
		if text in tuple(get):
			return get.get(text)
		if text in ("RUN_STRINGS", "SLAP_TEMPLATES", "ITEMS", "THROW", "HIT", "RAMALAN_STRINGS", "RAMALAN_FIRST"):
			runstr = getattr(FUNC_LANG['id'], text)
			return runstr
		return text
	elif str(getlang) in LOADED_LANGS_ID:
		func = getattr(FUNC_LANG[getlang], getlang)
		if text in ("RUN_STRINGS", "SLAP_TEMPLATES", "ITEMS", "THROW", "HIT", "RAMALAN_STRINGS", "RAMALAN_FIRST"):
			runstr = getattr(FUNC_LANG[getlang], text)
			return runstr
		langtxt = func.get(text)
		if not langtxt:
			LOGGER.warning("Can't get translated string for lang '{}' ('{}')".format(str(getlang), text))
			langtxt = text
		return langtxt
	else:
		sql.set_lang(message.chat.id, 'en')
		get = getattr(FUNC_LANG['en'], 'en')
		if text in tuple(get):
			return get.get(text)
		if text in ("RUN_STRINGS", "SLAP_TEMPLATES", "ITEMS", "THROW", "HIT", "RAMALAN_STRINGS", "RAMALAN_FIRST"):
			runstr = getattr(FUNC_LANG['en'], text)
			return runstr
		return text
