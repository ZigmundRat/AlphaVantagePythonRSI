from colorama import Fore, Back, Style
from colorama import init
import json
import requests 

class RSI:

	def __init__(self, rsiThreshold):
		self.rsiThreshold = rsiThreshold
		
	def sayhi(self):
		print('Hello')

	def getRSIdata(self, symbol):
		try:
			avUrl = "https://www.alphavantage.co/query?function=RSI&symbol="+self.symbol+"&interval=15min&time_period=10&series_type=close&apikey=OD3IMFWZFKS4HG8O"
			method = 'GET'
			response = requests.request(method,avUrl)
			rsi = json.loads(response.text)
		except:
			print(Back.RED + "Error getting: ", self.symbol)
			return ''		
		
		#with open('C:\\Python\\myscripts\\exjson\\'+self.symbol+'.json') as f:
		#	rsi = json.load(f)
		
		try:
			parseRSI = str(rsi['Technical Analysis: RSI'])
			rsiValue = parseRSI[30:37]
		except:
			print(Back.RED + "Error getting: ", self.symbol)
			return self.symbol.ljust(10)
		
		if float(rsiValue) <= self.rsiThreshold:
			return self.symbol.ljust(10) + rsiValue.ljust(10) 
		else:
			return  ''
			
			