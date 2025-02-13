from tkinter import *
from tkinter import ttk
import tkinter as tk
from Config_Var import * 
from tkinter import filedialog

class TKrightpanel:
	def __init__(self, win, frame):
		self.win = win
		self.frame = frame
		self.configvar = Config_Var()
		
		
		#Right frame Headline
		Label(self.frame, text= "Indstillinger", font= ('Aerial 17 bold italic')).pack(pady= (5,10))


		#Right Frame Canvas & Buttons (Update Interval)
		self.canvas_update = Canvas(self.frame, bg="skyblue3", width=350, height=40)
		self.canvas_update.pack(fill="both", pady=10)
		self.canvas_var = self.canvas_update.create_text(250, 20, text="Opdateres hver " + str(self.configvar.getUpdate_Timer()/1000/60) +  " Minutter", font=('', 12))

		self.inputtxt = tk.Entry(self.frame)
		self.inputtxt.insert(0, float(self.configvar.getUpdate_Timer()/1000/60))
		self.inputtxt.bind("<Return>", lambda x: [self.configvar.setUpdate_Timer(self.inputtxt.get()), self.CanvasUpdate_Timer(str(self.configvar.getUpdate_Timer()/1000/60))])
		self.inputtxt.pack(pady=5)

		self.printButton = tk.Button(self.frame, text = "Opdater Interval i Minutter", command = lambda: [self.configvar.setUpdate_Timer(str(self.inputtxt.get())), self.CanvasUpdate_Timer(str(self.configvar.getUpdate_Timer()/1000/60))])
		self.printButton.pack(pady=(5,10))
		

		#Right Frame Canvas & Buttons (Konfiguration)
		self.canvas_konf = Canvas(self.frame, bg="skyblue3", width=350, height=40)
		self.canvas_konf.pack(fill="both", pady=10)
		self.konf_var = self.canvas_konf.create_text(250, 20, text="Konfigurationsnavn: " + str(self.configvar.getKonfiguration()), font=('', 8), width=500)

		self.input_konf = tk.Entry(self.frame)
		self.input_konf.insert(0, self.configvar.getKonfiguration())
		#input_konf.bind("<Return>", update_konf)
		self.input_konf.pack(pady=5)

		self.konf_Button = tk.Button(self.frame, text = "Opdater Konfiguration", command = lambda: [self.configvar.setKonfiguration(str(self.input_konf.get())), self.CanvasUpdate_Konf(configvar.getKonfiguration())])
		self.konf_Button.pack(pady=(5,10))

		#Right Frame Canvas & Buttons (Change Paths)
		self.canvas_src = Canvas(self.frame, bg="skyblue3", width=350, height=40)
		self.canvas_src.pack(fill="both", pady=10)
		self.src_var = self.canvas_src.create_text(250, 20, text="Nav Directory: " + str(self.configvar.getSRCdir()), font=('', 8), width=500)

		self.srcButton = tk.Button(self.frame, text = "Sæt Nav Dir", command = lambda: self.CanvasUpdate_SRC())
		self.srcButton.pack(pady=(5,10))

		self.canvas_path = Canvas(self.frame, bg="skyblue3", width=350, height=40)
		self.canvas_path.pack(fill="both", pady=(10,10))
		self.path_var = self.canvas_path.create_text(250, 20, text="Dir: " + str(self.configvar.getPathdir()), font=('', 8), width=500)

		self.pathButton = tk.Button(self.frame, text = "Sæt Dir", command = lambda: self.CanvasUpdate_Path())
		self.pathButton.pack(pady=(5,10))

		#Right Frame File-Extension
		self.canvas_file = Canvas(self.frame, bg="skyblue3", width=350, height=40)
		self.canvas_file.pack(fill="both", pady=(10,10))
		self.file_var = self.canvas_file.create_text(250, 20, text="Filtype: " + str(self.configvar.getFiletype()), font=('', 8), width=500)

		#pdfButton = tk.Button(right_frame, text = ".Pdf", command = lambda: update_fileextension(".pdf"))
		#pdfButton.pack(pady=(5,10))

		#ardButton = tk.Button(right_frame, text = ".Ard", command = lambda: update_fileextension(".ard"))
		#ardButton.pack(pady=(5,10))
		
	
	def CanvasUpdate_Timer(self, intervalvar):
		self.canvas_update.itemconfig(self.canvas_var, text="Opdateres hver " + intervalvar + " Minutter")
	def CanvasUpdate_Konf(self, konfvar):
		self.canvas_konf.itemconfig(self.konf_var, text= konfvar)
	def CanvasUpdate_SRC(self):
		self.update_SRC = self.configvar.setSRCdir(filedialog.askdirectory())
		self.canvas_src.itemconfig(self.src_var, text=self.update_SRC)
	def CanvasUpdate_Path(self):
		self.update_PATH = self.configvar.setPathdir(filedialog.askdirectory())
		self.canvas_path.itemconfig(self.path_var, text=self.update_PATH)
