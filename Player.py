from copy import copy
from CardGameRef import Data
from algorithm_JKL import *
import sys
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
		self.data.selfPoints=req["state"]["your_points"]
		self.data.opponentPoints=req["state"]["their_points"]
		if len(req["state"]["hand"]) == 5 and self.data.selfHand[0]==0:
			self.data.gameStart(req["state"]["hand"])
			
		if not req["state"].has_key("card"):
			
			if req["state"]["can_challenge"] == True and issueChallenge(self.data,False):
				self.response = copy(self.req_chal)
				self.response["request_id"] = req["request_id"]
				self.response["response"]["type"] = "offer_challenge"
			else:
				self.response = copy(self.req_card)
				self.response["request_id"] = req["request_id"]
				print "play card prep"
				cardval=playCard(self.data,False)
				print "cardval: "+str(cardval)
				self.lastcard=cardval
				self.response["response"]["card"]= cardval
				self.data.updateHand(cardval)
		#second hand
		else:
			if req["state"]["can_challenge"] == True and issueChallenge(self.data,True,req["state"]["card"]):
				self.response = copy(self.req_chal)
				self.response["request_id"] = req["request_id"]
				self.response["response"]["type"] = "offer_challenge"
			else:
				self.response = copy(self.req_card)
				self.response["request_id"] = req["request_id"]
				cardval=playCard(self.data,True, req["state"]["card"])
				self.response["response"]["card"]= cardval
				self.data.updateHand(cardval)
				self.lastcard=cardval

	def challenge(self,req):

		self.response = copy(self.req_chal)
		if len(req["state"]["hand"]) == 5 and self.data.selfHand[0]==0:
			self.data.gameStart(req["state"]["hand"])
		if responseToChallenge(self.data, req["state"]["player_number"]):
			self.response["response"]["type"] = "accept_challenge"
		else:
			self.response["response"]["type"] = "reject_challenge"
			# print "decknum - * * 2"
			# self.data.decknum-=len(self.data.selfHand)*2
			# for i in range(len(self.data.selfHand)):
			# 	self.data.decksum-=self.data.selfHand[i]
			# self.data.decksum-=(self.data.decksum/self.data.decknum)*len(self.data.selfHand)

			# if(self.data.decknum<10):
			# 	self.data.shuffle()
			self.data.gameEnd()
		self.response["request_id"] = req["request_id"]

	def result(self, req):
		if req["result"].has_key("type") and req["result"]["type"] == "trick_won":
			cardval = req["result"]["card"]
			self.data.cardExposed(cardval)
			if(req["result"]["by"]==req["your_player_num"]):
				self.data.selfTricks+=1
			else:
				self.data.opponentTricks+=1

		if req["result"].has_key("type") and req["result"]["type"] == "hand_done":
			self.data.updateCoefficientsGame(True if req["result"].has_key("by") and req["result"]["by"] == req["your_player_num"] else False)
			self.data.gameEnd()
			
			if(self.data.decknum<10):
				self.data.shuffle()
		if req["result"].has_key("type") and req["result"]["type"] == "trick_tied":
			self.data.cardExposed(self.lastcard)
		if req["result"].has_key("type") and req["result"]["type"] == "game_won":
			pass

	def return_response(self):
		print("Going out:\n %s \n" % self.response)
		return self.response


