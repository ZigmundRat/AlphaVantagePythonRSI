

class Watchlist:

	def __init__(self, location):
		self.location = location

	def GetWatchlist(self):
		with open(self.location) as f:
			lines = f.read().splitlines()	
		return lines		