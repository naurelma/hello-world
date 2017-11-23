import tkinter as tk
import time
import os
from winsound import Beep
hostname = "8.8.8.8" #example


last = False
def ping():
	global last
	response = os.system("ping -n 1 " + hostname)

	#and then check the response...
	if response == 0:
		last = True
		return hostname
	else:
		if last:
			Beep(333,3000)
			last = False
		return """  WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW """


class App():
	def __init__(self):
		self.root = tk.Tk()
		self.label = tk.Label(text="")
		self.label.pack()
		self.update_ping()
		self.root.mainloop()

	def update_ping(self):
		time = 5
		txt = ping()
		self.label.configure(text=txt)
		self.root.after(time*1000, self.update_ping)

app=App()