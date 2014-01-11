from copy import copy

class PlayerT:
	"""docstring for player"""
	def __init__(self):
		self.req_card = {"type": "move", "request_id": None, "response": {"type": "play_card", "card": None}}
		self.req_chal = {"type": "move", "request_id": None, "response": {"type": None}}
		self.in_challange = False
		self.response = None

	def requests(self, req):
		if req["player_number"] == 0:
			if req["state"]["can_challenge"] == "true":
				self.response = copy(self.req_chal)
				self.response["request_id"] = req["request_id"]
				self.response["response"]["type"] = "offer_challenge"
			else:
				
		else:
			self.response = copy(self.req_card)
			self.response["request_id"] = req["request_id"]
			self.response["response"] = 

	def challenge(self,req):
		self.response = copy(self.req_chal)
		self.response["response"]["type"] = "reject_challenge"
		self.response["request_id"] = req["request_id"]

	def result(self, req):
		pass

	def response(self):
		return self.response


