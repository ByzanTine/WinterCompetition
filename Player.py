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
		self.data.shuffle()

	def requests(self, req):
		#first hand
		if len(req["state"]["hand"]) == 5:
			self.data.gameStart(req["state"]["hand"])
		if req["player_number"] == 0:
			if req["state"]["can_challenge"] == "true" and issueChallenge(self.data,False):
				self.response = copy(self.req_chal)
				self.response["request_id"] = req["request_id"]
				self.response["response"]["type"] = "offer_challenge"
			else:
				self.response = copy(self.req_card)
				self.response["request_id"] = req["request_id"]
				cardval=playCard(self.data,False)
				self.lastcard=cardval
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
				self.lastcard=cardval

	def challenge(self,req):
		self.response = copy(self.req_chal)

		if responseToChallenge(self.data, req["state"]["player_number"]):
			self.response["response"]["type"] = "accept_challenge"
		else:
			self.response["response"]["type"] = "reject_challenge"
			self.data.decknum-=len(self.data.selfHand)*2
			for i in rang(len(self.data.selfHand)):
				self.data.decksum-=self.data.selfHand[i]
			self.data.decksum-=(self.data.decksum/self.data.decknum)*len(self.data.selfHand)

			if(self.data.decknum<10):
				self.data.shuffle()
			self.data.gameEnd()
		self.response["request_id"] = req["request_id"]

	def result(self, req):
		if req["result"].has_key("type") and req["result"]["type"] == "trick_won":
			cardval = req["result"]["card"]
			self.data.cardExposed(cardval)
			self.data.selfTricks+=1

		if req["result"].has_key("type") and req["result"]["type"] == "hand_done":
			self.data.updateCoefficientsGame(True if req["result"].has_key("by") and req["result"] == req["result"]["your_player_num"] else False)
			self.data.gameEnd()
			
			if(self.data.decknum<10):
				self.data.shuffle()
		if req["result"].has_key("type") and req["result"]["type"] == "trick_tied":
			self.data.cardExposed(self.lastcard)
		if req["result"].has_key("type") and req["result"]["type"] == "game_won":
			pass
	def return_response(self):
		return self.response


