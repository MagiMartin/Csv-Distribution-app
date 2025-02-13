import time
import pandas as pd
import os
import glob
import math
import shutil
from datetime import datetime
from IPython.display import display
from Config_Var import *


class FunctionLoops:
	def __init__(self, win):
		self.win = win
		self.today = datetime.today()
		self.configvar = Config_Var()
		self.startMain = False
		self.startCaldera = False
		
	#Check folders, generate new files and move the old
	def mainLoop(self):
		if self.startMain:
			tidsStempel = time.strftime("%m-%d-%Y_%H-%M-%S")
			list = []
			csv_files = glob.glob(os.path.join(self.configvar.src_dir, "*.csv"))
			#Load Csv files from Navision	
			for f in csv_files:
				df = pd.read_csv(f, sep=';', names=['fil navn','antal','leverings dato','kunde','odrenr','materiale','efterbehandling'] , header = None, encoding = "ISO-8859-1")
				df.insert(0, 'job navn', tidsStempel)
				#Aply priority from Delivery date
				formatted_date = self.today.strftime('%d-%m-%y')
				tid_date = datetime.strptime(formatted_date,'%d-%m-%y')
				levering_date = datetime.strptime(df['leverings dato'].values[0], '%d-%m-%y')
				prioritet_var = (levering_date - tid_date).days
				#Add settings, priority and post treatment to dataframe
				df['konfiguration'] = self.configvar.Konfigurationsnavn
				df['prioritet'] = abs(prioritet_var)
				if math.isnan(df['efterbehandling']):
					df['efterbehandling'] = 1
				list.append(df)
			if len(list)== 0:
				print("empty")
			else:
				#Move files to Handled Files to "done" and cleanup folder
				for root, dirs, files in os.walk(self.configvar.src_dir):
					for f in files:
						if f.endswith('.csv'):
							os.makedirs(os.path.join(self.configvar.src_dir, "Done"), exist_ok = True)
							shutil.copy(os.path.join(root,f), self.configvar.src_dir + "\Done")
							os.remove(os.path.join(self.configvar.src_dir,f))
					break
				#Update Canvas and export new CSV file
				frame = pd.concat(list, axis=0, ignore_index=True)
				frame['fil navn'] = frame['fil navn'] + self.configvar.filtype
				file_name = "\\"+time.strftime("%m-%d-%Y_%H-%M-%S")+".csv"
				frame.to_csv(self.configvar.path_dir+file_name, index=None, sep = ';')
				display(frame)
		else:
			return
		list.clear()
		self.win.after(self.configvar.getUpdate_Timer(), self.mainLoop)
		
	
		
	#Caldera Clean loop
	def calderaLoop(self):
		if self.startCaldera:	
			for root, dirs, files in os.walk(self.configvar.caldera_dir):
				for name in files:
					source = os.path.join(root, name)
					if name.endswith((".eps")):
						try:
							shutil.copyfile(source, self.configvar.caldera_dir + "\\" + name)
						except shutil.SameFileError:
							pass
						except PermissionError:
							pass
					else:
						continue
				
			print(self.startCaldera)			
		else:
			return
			
		self.win.after(10000, self.calderaLoop)
