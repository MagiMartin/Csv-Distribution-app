import configparser

class Config_Var:
	def __init__(self):
		
		#Import Config File
		self.config_obj = configparser.ConfigParser()
		self.config_obj.read("config.ini")
		self.SRvar = self.config_obj["variable"]
		self.SRdir = self.config_obj["directories"]

		#Standard Paths
		self.src_dir = self.SRdir["src"]
		self.path_dir = self.SRdir["path"]
		self.caldera_dir = self.SRdir["caldera"]
		
		#Gloabl variables
		self.update_timer = int(self.SRvar["update"])
		self.Konfigurationsnavn = self.SRvar["konfiguration"]
		self.filtype = self.SRvar["filtype"]
		
	
	def getUpdate_Timer(self):
		return self.update_timer
	
	def setUpdate_Timer(self, varupdatetimer):
		self.update_timer = int(varupdatetimer)*60*1000
		self.SRvar["update"] = str(self.update_timer)
		with open('config.ini', 'w') as configfile:
			self.config_obj.write(configfile)	
	
	def getKonfiguration(self):
		return self.Konfigurationsnavn
		
	def setKonfiguration(self, varupdatekonf):
		self.Konfigurationsnavn = str(varupdatekonf)
		self.SRvar["konfiguration"] = str(self.Konfigurationsnavn)
		with open('config.ini', 'w') as configfile:
			self.config_obj.write(configfile)
		
	def getSRCdir(self):
		return self.src_dir
	
	def setSRCdir(self, varSRC):
		self.src_dir_temp = varSRC
		if (len(self.src_dir_temp) != 0):
			self.SRdir["src"] = self.src_dir_temp
			with open('config.ini', 'w') as configfile:
				self.config_obj.write(configfile)
		return self.src_dir_temp
	
	def getPathdir(self):
		return self.path_dir
		
	def setPathdir(self, varPath):
		self.path_dir_temp = varPath
		if (len(self.path_dir_temp) != 0):
			self.SRdir["path"] = self.path_dir_temp
			with open('config.ini', 'w') as configfile:
				self.config_obj.write(configfile)
		return self.path_dir_temp
	
	def getFiletype(self):
		return self.filtype
		
