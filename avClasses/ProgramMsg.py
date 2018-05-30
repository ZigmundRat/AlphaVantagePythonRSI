from colorama import Fore, Back, Style
from colorama import init

class ProgramMsg(object):

	def __init__(self, title, RunIntervalsec, RSIthreshold):
		self.title = title
		self.RunIntervalsec = RunIntervalsec
		self.RSIthreshold = RSIthreshold
		
	def display(self):
		print(Back.BLUE + '******************************')
		print(Back.BLUE + self.title)
		print(Back.BLUE + 'Checks watchlist every ', self.RunIntervalsec, ' seconds')
		print(Back.BLUE + 'RSI Threshold = ', self.RSIthreshold)
		print(Back.BLUE + 'RSI Time Frame = 15 minute'.ljust(30))
		print(Back.BLUE + '******************************')
		print(Style.RESET_ALL)
		return ''
	
		
