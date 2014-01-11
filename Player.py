from copy import copy
from CardGameRef import Data
from algorithm_JKL import *
class PlayerT:
	"""docstring for player"""
	def __init__(self):
		self.req_card = {"type": "move", "request_id": None, "response": {"type": "play_card", "card": None}}
		self.req_chal = {"type": "move", "request_id": None, "response": {"type": None}}
		self.in_challange = False
		self.response = None
		self.data=Data()
		data.shuffle()

	def requests(self, req):
		#first hand
		if req["player_number"] == 0:
			if req["state"]["can_challenge"] == "true" and issueChallenge(self.data,False):
				self.response = copy(self.req_chal)
				self.response["request_id"] = req["request_id"]
				self.response["response"]["type"] = "offer_challenge"
			else:
				self.response = copy(self.req_card)
				self.response["request_id"] = req["request_id"]
				cardval=playCard(self.data,False)
				self.response["response"]["card"]= cardval
				self.data.updateHand(cardval)
		#second hand
		else:
			if req["state"]["can_challenge"] == "true" and issueChallenge(self.data,True,self.reg["state"]["card"]):
				self.response = copy(self.req_chal)
				self.response["request_id"] = req["request_id"]
				self.response["response"]["type"] = "offer_challenge"
			else:
				self.response = copy(self.req_card)
				self.response["request_id"] = req["request_id"]
				cardval=playCard(self.data,False)
				self.response["response"]["card"]= cardval
				self.data.updateHand(cardval)

	def challenge(self,req):
		self.response = copy(self.req_chal)

		if responseToChallenge(self.data, req["state"]["player_number"])
			self.response["response"]["type"] = "accept_challenge"
		else
			self.response["response"]["type"] = "reject_challenge"
		self.response["request_id"] = req["request_id"]

	def result(self, req):
		if req["result"].has_key("type") and req["result"]["type"] == "trick_won":
			cardval = req["result"]["card"]
			self.data.cardExposed(cardval)
		if req["result"].has_key("type") and req["result"]["type"] == "hand_done":
			self.data.gameEnd()
		
	def return_response(self):
		return self.response


