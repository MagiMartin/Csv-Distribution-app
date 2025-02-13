from tkinter import *
from tkinter import ttk
from RunController import *

import time

class TKleftpanel:
	def __init__(self, win, frame):
		self.win = win
		self.frame = frame
		self.runcontroller = RunController(self.win)
		
		#Left frame Headline
		Label(self.frame, text= "Start / Stop program", font= ('Aerial 17 bold italic')).pack(pady= (5,20))
		
		
		#Left Frame canvas & Buttons
		self.canvas_timer = Canvas(self.frame, bg="light steel blue", width=350, height=80)
		self.canvas_timer.pack(fill="both",pady=(80,15))
		self.var = self.canvas_timer.create_text(250, 40, text="Tryk start, for at starte mappe overvågningen", font=('Arial Bold', 12))

		ttk.Button(self.frame, text= "Start Overvågning", command=lambda: self.CanvasUpdate_TimerStart()).pack(pady=(15,15))
		ttk.Button(self.frame, text= "Stop Overvågning", command=lambda: self.CanvasUpdate_TimerStop()).pack(pady=(15,30))

	
	def CanvasUpdate_TimerStart(self):
		self.canvas_timer.itemconfig(self.var , text= "Startet opdatering om 10 sek")
		self.runcontroller.start_threads(self.canvas_timer, self.var)
	
	def CanvasUpdate_TimerStop(self):
		self.runcontroller.stop_surveil()
	
