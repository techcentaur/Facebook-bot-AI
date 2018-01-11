import requests
import json
import os

from flask import Flask, request

bot = Flask(__name__)

page_access_token='EAAMWpBkxQbIBAAsLLfDZCgooTDx7ifR6lTpLzaBtJmOZB7MWjf5K9zEhHDASbsWEfwO6YeFZCS1DhP6piZAJrX2aFVtqGbCiMbaRXZCuTZCQr3FSHEwfMm26EgRQqwKBPv8xbWjeQe8hZBxM7Xbq0kGIzlHwNozZCxZBmcO7aPUVQZBAZDZD'
VERIFY_TOKEN = 'verifythistokenotherwiseillbeatyourshitup'

@bot.route('/', methods=['GET'])
def hub_challenge_verification():
	if request.args.get("hub.mode")=="subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.VERIFY_TOKEN") == VERIFY_TOKEN:
			return "Verification Invalid", 403
		return request.args.get('hub.challenge','')


@bot.route('/', methods=['POST'])
def webhook():
	data = json.loads(request.data)
	messaging_events = data["entry"][0]["messaging"]
	for event in messaging_events:
		sender = event['sender']['id']
		receiver = event['recipient']['id']
		message = event['message']['text']
		send_message(sender, "Hi")


def send_message(person_who_will_receive, message):

	# reply_object = Reply(message)
	# message_data = reply_object.get_reply()

	params = {"access_token": page_access_token}
	headers = {"Content-Type": "application/json"}
	data = json.dumps({
		"recipient":{"id": person_who_will_receive},
		"message": {"text": message}
		})
	r=requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    # if r.status_code!=requests.codes.ok:
    # 	print(r.text)