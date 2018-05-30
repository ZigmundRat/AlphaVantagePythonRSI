# https://www.alphavantage.co/query?function=RSI&symbol=MSFT&interval=15min&time_period=10&series_type=close&apikey=
# Required Python Libraries
# pip3 install requests
# pip3 install colorama
# pip3 install pyinstaller

import json
import requests 
import threading
import time
import datetime
from colorama import Fore, Back, Style
from colorama import init
from avClasses.ProgramMsg import ProgramMsg
from avClasses.Watchlist import Watchlist
from avClasses.RSI import RSI

init()

RSIthreshold = 40		# Below or equal to RSI value
RunIntervalsec = 900		# 900s = 15 minutes
TimeBetweenApiRequests = 15	# Run every N secods

def main():
	newMsg = ProgramMsg('Setup Checker', RunIntervalsec, RSIthreshold)
	newMsg.display()
	
	wlist = Watchlist('watchlist.txt')
	print('Watchlist:', wlist.GetWatchlist())
 
def checkSetup(lines):
	threading.Timer(RunIntervalsec, checkSetup, [lines]).start() 
	print(Back.MAGENTA + '*Starting Next Interval*')
	
	gRsi = RSI(RSIthreshold)
	
	for sym in lines:
		gRsi.symbol = sym
		print(Back.YELLOW + 'Checking:  ', sym.ljust(7), end='\r')
		rsiVal = gRsi.getRSIdata(sym)
		if rsiVal != '':
			now = datetime.datetime.now()
			print(Back.GREEN + rsiVal, str(now.strftime("%Y-%m-%d %H:%M")).ljust(20))
		time.sleep(TimeBetweenApiRequests)
  
if __name__== "__main__":
	main()

	wlist = Watchlist('watchlist.txt')
	
	try:
		while True:
			checkSetup(wlist.GetWatchlist())
	except KeyboardInterrupt:
		pass	
	
	
	




	
	
	

	
	
	
	

	
