import requests
from exceptions import EmailNotSentException



class MailService():
	def __init__(self,sender=None,recievers=None,html=None):
		self.sender = sender
		self.recievers = recievers
		self.html = html

	def send(self):
		r = requests.post(
				 "https://api.mailgun.net/v3/sandboxb10a6d740929436394df541e080ce2c3.mailgun.org/messages",
				 auth=("api","key-a6e264dd1c10ef1b3db0416a789f3f63"),
				 data={
				 	"from":"Excited User <postmaster@sandboxb10a6d740929436394df541e080ce2c3.mailgun.org>",
				 	"to":self.recievers,
				 	"subject":"hello",
				 	"html":self.html
				 }
				)
		if r.status_code is not 200:
			raise EmailNotSentException

