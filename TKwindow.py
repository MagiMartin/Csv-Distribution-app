from tkinter import * 
import tkinter as tk
from TKleftpanel import *
from TKrightpanel import *
from PIL import ImageTk, Image
#import threading


class TKwindow:
	def __init__(self):
		#Define root window  
		self.win = Tk()  
		self.win.geometry("1100x850")
		self.win.config(bg="white")

		#Define Banner Frame
		self.top_frame = Frame(self.win, width=800, height = 70, bg='white')
		self.top_frame.pack(fill='both')

		#Logo and banner text
		self.image = Image.open("logo.jpg")
		self.resize_image = self.image.resize((200,50))
		self.img = ImageTk.PhotoImage(self.resize_image)
		self.label = Label(self.top_frame, image = self.img)
		self.label.config(borderwidth = 0)
		self.label.pack(side='left', padx=150,pady=20)
		self.banner_label = Label(self.top_frame, text= "CSV overvågning, distribution", font= ('Aerial 17 bold italic'), bg="white")
		self.banner_label.pack(padx = 50, side = 'left')
		
		
		# Create left and right frames
		self.left_frame  =  Frame(self.win,  width=350,  height=400,  bg='grey')
		self.left_frame.pack(side='left',  fill='both',  padx=10,  pady=5,  expand=True)

		self.right_frame  =  Frame(self.win,  width=350,  height=400,  bg='grey')
		self.right_frame.pack(side='right',  fill='both',  padx=10,  pady=5,  expand=True)
		
		self.leftpanel = TKleftpanel(self.win, self.left_frame)
		self.rightpanel = TKrightpanel(self.win, self.right_frame)
		
	def start(self):
		#threading.Thread(self.win.mainloop()).start()
		self.win.mainloop() #Start monitoring and update GUI
