__module_name__ = "ohayou"
__module_version__ = "1.0"
__module_description__ = "Automated ohayou script"

import hexchat
from datetime import datetime
from threading import Timer
from time import sleep

# Set context to #yukkuri on Rizon

context=hexchat.find_context(server="Rizon", channel="#yukkuri")
context.set()

# Helper Functions

def say(message, time=0):
	sleep(time)
	hexchat.command("msg #yukkuri " + message)

def prnt(message):
	hexchat.prnt(str(message));

def get_current_nick():
	return hexchat.get_info("nick")

# Daily Ohayou Timer

t = 0

def daily_ohayou():
	say(".ohayou")
	start_timer()

def start_timer():
	x=datetime.today()
	y=x.replace(day=x.day+1, hour=0, minute=1, second=0, microsecond=0)
	delta_t=y-x
	secs=delta_t.seconds+1
	global t
	t = Timer(secs, daily_ohayou)

	t.start()

def stop_ohayou(word, word_eol, userdata):
	t.cancel()
	prnt("ohayou timer cancelled")
	return hexchat.EAT_NONE

def start_ohayou(word, word_eol, userdata):
	start_timer()
	prnt("ohayou timer started")
	return hexchat.EAT_NONE

# Hooks and Callbacks

def whatabot_parser(word, word_eol, userdata):
	if hexchat.strip(word[0]) == "whatabot":
		nick = get_current_nick()
		split = word[1].split(' ')
		ohayous = split[len(split)-3] if len(split) > 2 else ""

		if word[1].find(nick) > -1 and ohayous.isdigit():
			ohayous = int(ohayous)

			while ohayous >= 10:
				if ohayous >= 650:
					say(".buy dragondildo", 1)
					ohayous -= 650
				elif ohayous >= 500:
					say(".buy catnip", 1)
					ohayous -= 500
				elif ohayous >= 300:
					say(".buy godzilla", 1)
					ohayous -= 300
				elif ohayous >= 100:
					say(".buy bag", 1)
					ohayous -= 100
				elif ohayous >= 45:
					say(".buy waifufig", 1)
					ohayous -= 45
				else:
					say(".buy cat", 1)
					ohayous -= 10

	return hexchat.EAT_NONE

hexchat.hook_print("Channel Message", whatabot_parser)
hexchat.hook_print("Channel Msg Hilight", whatabot_parser)
hexchat.hook_command("STOPOHAYOU", stop_ohayou)
hexchat.hook_command("STARTOHAYOU", start_ohayou)

start_timer()
prnt("Ohayou loaded")