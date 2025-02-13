from threading import Thread
import threading
from FunctionLoops import *
from Config_Var import *


class RunController:
	def __init__(self, win):
		self.win = win
		self.functions = FunctionLoops(self.win)
		self.config_var = Config_Var()
		self.timer_runs = False
		
	#Start Surveil
	def start_surveil(self):
		self.functions.startMain = True
		self.win.after(10000, self.functions.mainLoop)	


	#Start Caldera Loop
	def start_surveil_caldera(self):
		self.functions.startCaldera = True
		self.win.after(10000, self.functions.calderaLoop)

		
	#Stop Surveil
	def stop_surveil(self):
		print("Stopping Threads")
		self.timer_runs = False
		self.functions.startMain = False
		self.functions.startCaldera = False
		
		
	#Start Threads For loops
	def start_threads(self,canvas_timer, canvas_var):
		print("starting Threads")
		self.thread_caldera = Thread(target=self.start_surveil_caldera)
		self.thread_caldera.start()
		self.thread_main = Thread(target=self.start_surveil)
		self.thread_main.start()
		self.thread_countdown = Thread(target=lambda: self.countdown(int(self.config_var.getUpdate_Timer()/1000), canvas_timer, canvas_var))
		self.timer_runs = True
		self.thread_countdown.start()
		return
	
	#Countdown timer for loops on the canvas
	def countdown(self, t, canvas_timer, canvas_var):	
		time.sleep(10)
		while t:
			if t > 1 and self.timer_runs == True:
				canvas_timer.itemconfig(canvas_var, text="Startet, tid til opdatering:  " + str(t) + " sek")
				time.sleep(1)
				t -= 1
			elif t <= 1 and self.timer_runs == True:
				t += int(self.config_var.getUpdate_Timer()/1000) 
			elif self.timer_runs == False:
				canvas_timer.itemconfig(canvas_var, text="Stoppet")
				return
				
			
		
		
		
