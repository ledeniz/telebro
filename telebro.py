#!/usr/bin/env python3

# telebro v0.1
# author: https://github.com/ledeniz

import yaml
import urllib.request
import urllib.parse
import string
import datetime

class TelegramBot:
	endpoint = "https://api.telegram.org/"

	def __init__(self, id, chat_id):
		self.id = str(id)
		self.chat_id = str(chat_id)

	def filterMessage(self, message):
		printable = set(string.printable)
		message = ''.join(filter(lambda x: x in printable, message))

		return message

	def sendMessage(self, message):
		message = self.filterMessage(message)

		url = self.endpoint
		url += self.id
		url += "/"
		url += "sendMessage?chat_id="
		url += self.chat_id
		url += "&text="
		url += message

		urllib.parse.quote(url)

		self.response = urllib.request.urlopen(url).read()

		return self.response

class Host:
	def __init__(self, name, url):
		self.name = str(name)
		self.url = str(url)
		self.code = 9001

	def check(self):
		try:
			result = urllib.request.urlopen(self.url)

			self.code = result.getcode()
			success = True
		except:
			success = False

		if self.code >= 400:
			return False
		else:
			return True

class Telebro:
	def __init__(self):
		self.config_file = "config.yml"
		self.log_file = "error.log"

		self.init()

	def init(self):
		self.read_config()

		self.bot = TelegramBot(
			self.config["bot_id"],
			self.config["chat_id"]
		)

	def read_config(self):
		file = open(self.config_file, "r")
		contents = file.read()

		self.config = yaml.load(contents)

	def log(self, message):
		line = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S - ")
		line += message
		line += "\n"

		file = open(self.log_file, "a")
		file.write(line)

	def alert(self, message):
		self.bot.sendMessage(message)

	def checkHosts(self):
		for id in self.config["hosts"]:
			url = self.config["hosts"][id]

			host = Host(id, url)

			if not host.check():
				if host.code == 9001:
					code = "unknown"
				else:
					code = host.code

				message = host.name + " is not reachable! (code: " + str(code) + ") - " + host.url

				self.log(message)
				self.alert(message)

if __name__ == '__main__':
	Telebro().checkHosts()
