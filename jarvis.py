import datetime
import os
import random
import sys
import webbrowser
from tkinter.ttk import *
from tkinter import *
import PyPDF2
import pyautogui

import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import wikipedia
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtWidgets import *
from JarvisUi import Ui_JarvisUi
from PyQt5.QtCore import *

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def movie_speak(self):
	self.ui = Ui_JarvisUi()
	self.ui.movie = QtGui.QMovie("../../OneDrive/Documents/G.U.I Material/VoiceReg/Ntuks.gif")
	self.ui.gif_3.setMovie(self.ui.movie)
	self.ui.movie.start()

def speak(audio):
	engine.say(audio)
	print(audio)
	engine.runAndWait()



# Calculator
def Calculator():
	import tkinter as tk

	LARGE_FONT_STYLE = ("Arial", 40, "bold")
	SMALL_FONT_STYLE = ("Arial", 16)
	DIGITS_FONT_STYLE = ("Arial", 24, "bold")
	DEFAULT_FONT_STYLE = ("Arial", 20)

	OFF_WHITE = "#F8FAFF"
	WHITE = "#FFFFFF"
	LIGHT_BLUE = "#CCEDFF"
	LIGHT_GRAY = "#F5F5F5"
	LABEL_COLOR = "#25265E"

	class Calculator:
		def __init__(self):
			self.window = tk.Tk()
			self.window.geometry("675x867")
			self.window.resizable(0, 0)
			self.window.title("Calculator")

			self.total_expression = ""
			self.current_expression = ""
			self.display_frame = self.create_display_frame()

			self.total_label, self.label = self.create_display_labels()

			self.digits = {
				7: (1, 1), 8: (1, 2), 9: (1, 3),
				4: (2, 1), 5: (2, 2), 6: (2, 3),
				1: (3, 1), 2: (3, 2), 3: (3, 3),
				0: (4, 2), '.': (4, 1)
			}
			self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
			self.buttons_frame = self.create_buttons_frame()

			self.buttons_frame.rowconfigure(0, weight=1)
			for x in range(1, 5):
				self.buttons_frame.rowconfigure(x, weight=1)
				self.buttons_frame.columnconfigure(x, weight=1)
			self.create_digit_buttons()
			self.create_operator_buttons()
			self.create_special_buttons()
			self.bind_keys()

		def bind_keys(self):
			self.window.bind("<Return>", lambda event: self.evaluate())
			for key in self.digits:
				self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

			for key in self.operations:
				self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

		def create_special_buttons(self):
			self.create_clear_button()
			self.create_equals_button()
			self.create_square_button()
			self.create_sqrt_button()

		def create_display_labels(self):
			total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E,
								   bg=LIGHT_GRAY,
								   fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
			total_label.pack(expand=True, fill='both')

			label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E,
							 bg=LIGHT_GRAY,
							 fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
			label.pack(expand=True, fill='both')

			return total_label, label

		def create_display_frame(self):
			frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
			frame.pack(expand=True, fill="both")
			return frame

		def add_to_expression(self, value):
			self.current_expression += str(value)
			self.update_label()

		def create_digit_buttons(self):
			for digit, grid_value in self.digits.items():
				button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR,
								   font=DIGITS_FONT_STYLE,
								   borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
				button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

		def append_operator(self, operator):
			self.current_expression += operator
			self.total_expression += self.current_expression
			self.current_expression = ""
			self.update_total_label()
			self.update_label()

		def create_operator_buttons(self):
			i = 0
			for operator, symbol in self.operations.items():
				button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR,
								   font=DEFAULT_FONT_STYLE,
								   borderwidth=0, command=lambda x=operator: self.append_operator(x))
				button.grid(row=i, column=4, sticky=tk.NSEW)
				i += 1

		def clear(self):
			self.current_expression = ""
			self.total_expression = ""
			self.update_label()
			self.update_total_label()

		def create_clear_button(self):
			button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR,
							   font=DEFAULT_FONT_STYLE,
							   borderwidth=0, command=self.clear)
			button.grid(row=0, column=1, sticky=tk.NSEW)

		def square(self):
			self.current_expression = str(eval(f"{self.current_expression}**2"))
			self.update_label()

		def create_square_button(self):
			button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR,
							   font=DEFAULT_FONT_STYLE,
							   borderwidth=0, command=self.square)
			button.grid(row=0, column=2, sticky=tk.NSEW)

		def sqrt(self):
			self.current_expression = str(eval(f"{self.current_expression}**0.5"))
			self.update_label()

		def create_sqrt_button(self):
			button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR,
							   font=DEFAULT_FONT_STYLE,
							   borderwidth=0, command=self.sqrt)
			button.grid(row=0, column=3, sticky=tk.NSEW)

		def evaluate(self):
			self.total_expression += self.current_expression
			self.update_total_label()
			try:
				self.current_expression = str(eval(self.total_expression))

				self.total_expression = ""
			except Exception as e:
				self.current_expression = "Error"
			finally:
				self.update_label()

		def create_equals_button(self):
			button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR,
							   font=DEFAULT_FONT_STYLE,
							   borderwidth=0, command=self.evaluate)
			button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

		def create_buttons_frame(self):
			frame = tk.Frame(self.window)
			frame.pack(expand=True, fill="both")
			return frame

		def update_total_label(self):
			expression = self.total_expression
			for operator, symbol in self.operations.items():
				expression = expression.replace(operator, f' {symbol} ')
			self.total_label.config(text=expression)

		def update_label(self):
			self.label.config(text=self.current_expression[:11])

		def run(self):
			self.window.mainloop()

	if __name__ == "__main__":
		calc = Calculator()
		calc.run()

# JOKES
def jokes_angel():
	lines = [
		'A bear walks into a bar and says, “Give me a whiskey and … cola.”“Why the big pause?” asks the bartender. The bear shrugged. “I’m not sure; I was born with them.”' ,
		'Hear about the new restaurant called Karma?There’s no menu: You get what you deserve.',
		'Yesterday I saw a guy spill all his Scrabble letters on the road. I asked him, “What’s the word on the street?',
		'Why do we tell actors to “break a leg?”Because every play has a cast.',
		'Where are average things manufactured?The satisfactory.',
		'How do you drown a hipster?Throw him in the mainstream.',
		'How does Moses make tea?He brews.',
		'How do you keep a bagel from getting away?Put lox on it.',
		'A man tells his doctor, “Doc, help me. I’m addicted to Twitter!”The doctor replies, “Sorry, I don’t follow you …”' ,
		'Why don’t Calculus majors throw house parties?Because you should never drink and derive.' ,
		'What do you call a parade of rabbits hopping backwards?A receding hare-line.' ,
		'What’s the different between a cat and a comma?A cat has claws at the end of paws; A comma is a pause at the end of a clause.' ,
		'Why should the number 288 never be mentioned?It’s two gross.' ,
		'What did the Tin Man say when he got run over by a steamroller?“Curses! Foil again!”' ,
		'What did the bald man exclaim when he received a comb for a present?Thanks— I’ll never part with it!' ,
		'What did the left eye say to the right eye?Between you and me, something smells.' ,
		'What do you call a fake noodle?An impasta.' ,
		'Did you hear about the actor who fell through the floorboards?He was just going through a stage.' ,
		'Why don’t scientists trust atoms?Because they make up everything.' ,
		'What do you call a magic dog?A labracadabrador.']
	myline = random.choice(lines)
	speak(myline)


# NEWS
def news():
	main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=c9eca6a3a0fa4417992dccdc0442527a'

	main_page = requests.get(main_url).json()
	# print(main_page)
	articles = main_page["articles"]
	# print(articles)
	head = []
	day = ["first", "second", "third"]
	for ar in articles:
		head.append(ar["title"])
	for i in range(len(day)):
		# print(f"today's {day[i]} news is: ", head[i])w
		speak(f"today's {day[i]} news is: {head[i]}")


# TIME
def time_asking():
	import datetime
	now = datetime.datetime.now()
	speak("Current time is:")
	time = now.strftime("%I:%M %p")
	speak(time)


# GOOGLE
def Open_google_why():
	import subprocess as s
	s.Popen('"C:\Program Files\Google\Chrome\Application\chrome.exe"')


# POWERPOINT
def Open_PowerPoint():
	import subprocess as s
	s.Popen('"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"')


# WORD
def Open_Word():
	import subprocess as s
	s.Popen('C:\ProgramData\Microsoft\Windows\Start Menu')


# ERROR
def error_cant():
	speak("I can't comprehend your command")
	speak("Please repeat it for me.")


# READ A BOOK
def read_a_book():
	speak("I have only the first two books of percy jackson. Many more will come in the future")

	speak(
		"type book1 or book 1 to listen to the lightning thief and type book2 or book 2 to listen to the sea of monsters")
	movie_speak()

	# print("type Book-1 to listen to the lightning thief and type Book-2 to listen to the sea of monsters")

	books = input("Enter the name of the pdf  = ")

	book = open(books + ".pdf", 'rb')

	pdfReader = PyPDF2.PdfFileReader(book)

	pagen = int(input("Start page - "))

	pageN = int(input("END page - "))

	speaker = pyttsx3.init()

	for num in range(pagen, pageN):
		page = pdfReader.getPage(num)

		text = page.extractText()

		speaker.say(text)

		speaker.runAndWait()


# FEMALE VOICE OVER
def female():
	engine.setProperty('voice', voices[0].id)
	speak("Enabled ")
	speak("hello, i am selen. Lets get right into your service. What do you want?")
	speak('though whatever you ask me should be put to good use')


# BACK TO MALE
def disable():
	engine.setProperty('voice', voices[1].id)
	speak("Watch it woman...I will hunt you down and terminate you")
	engine.setProperty('voice', voices[0].id)
	speak("You will have to terminate yourself to terminate me ")
	engine.setProperty('voice', voices[1].id)
	speak("And i thought my threat would work.....What do you want boss?")


# WISH THE OWNER
def wishMe():
	hour = int(datetime.datetime.now().hour)
	speak("Downloading Dependencies................................................................Extracting Memory from cloud................................................................Download complete................................................................")



	if hour >= 0 and hour <= 12:
		speak("Good Morning")
	elif hour > 12 and hour <= 16:
		speak("Good Afternoon")
	else:
		speak("Good Evening")
		speak("Lets continue.")

	speak("How are you boss?")






class MainThread(QThread):
	def __init__(self):
		super(MainThread, self).__init__()

	def run(self):
		self.TaskExecution()

	def takecommand(self):
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("listening...")
			r.pause_threshold = 1
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
		try:
			print("Recognizing...")
			query = r.recognize_google(audio, language='en-in')
			print(f"user said: {query}")

		except Exception as e:
			# speak("Say that again Please...")
			return "none"

		query = query.lower()
		return query

	def TaskExecution(self):
		if __name__ == "__main__":
			wishMe()

			while True:

				self.query = self.takecommand()

				if "open notepad" in self.query:
					npath = "C:\\Windows\\system32\\notepad.exe"
					os.startfile(npath)

				elif "open command prompt" in self.query:
					os.system("start cmd")



				elif "play music" in self.query:
					webbrowser.open("https://open.spotify.com/")

				# online part
				elif "ip address" in self.query:
					ip = webbrowser.get('https://api.ipify.org').text
					speak(f"Your IP address is {ip}")

				elif "what is" in self.query or "what are" in self.query or "who is" in self.query or "who are" in self.query or "who" in self.query:
					speak("Searching wikipedia....")
					results = wikipedia.summary(self.query, sentences=2)
					speak(results)



				elif "open youtube" in self.query or "youtube" in self.query:
					speak("What do you want to see?")
					search = input("What do you want to see?----    ")

					if "i will decide" in search:
						webbrowser.open("www.youtube.com")

					else:
						speak('playing ' + search)
						pywhatkit.playonyt(search)

				elif "open stackoverflow" in self.query:
					webbrowser.open("www.stackoverflow.com")




				elif "open browser" in self.query:
					speak("Input your search self.query down below")
					cm = input("Input Your self.query here- ")
					webbrowser.open(cm)



				elif "check my mails" in self.query:
					speak("Opening your mails right now..")
					webbrowser.open("www.gmail.com")


				elif "I am fine" in self.query:
					speak("That is nice to hear boss.")
					speak("What can i do for you?")


				elif "I am not feeling good today" in self.query:
					speak("This song lifts up everyone spirits")
					pywhatkit.playonyt("macarena")



				# elif "set alarm" in self.query:
				#     nn = int(datetime.datetime.now().hour)
				#     if nn == 22:
				#      music_dir = 'E:\\music'
				#      songs = os.listdir(music_dir)
				#      os.startfile(os.path.join(music_dir, songs[0]))



				elif "tell me news" in self.query:
					lines = ['Okay.', 'On it boss', 'News is being served',
							 'Fetching the latest news from around the globe.']
					myLines = random.choice(lines)
					speak(myLines)
					news()




				elif "joke" in self.query:
					jokes_angel()



				elif "time" in self.query:
					time_asking();





				elif 'read me a book' in self.query:
					read_a_book()






				elif 'clock' in self.query:

					from time import strftime

					root = Tk()
					root.title("clock")

					def time():
						string = strftime(('%I:%M:%S %p'))
						label.config(text=string)
						label.after(1000, time)

					label = Label(root, font=("Ds-digital", 80), background="black", foreground="cyan")
					label.pack(anchor='center')
					time()

					mainloop()


				elif 'translator' in self.query:

					import googletrans
					import textblob
					from tkinter import ttk, messagebox

					root = Tk()
					root.title('Helion - Translator')

					root.geometry("880x300")

					def translate_it():
						# Delete Any Previous Translations
						translated_text.delete(1.0, END)

						try:
							# Get Languages From Dictionary Keys
							# Get the From Langauage Key
							for key, value in languages.items():
								if (value == original_combo.get()):
									from_language_key = key

							# Get the To Language Key
							for key, value in languages.items():
								if (value == translated_combo.get()):
									to_language_key = key

							# Turn Original Text into a TextBlob
							words = textblob.TextBlob(original_text.get(1.0, END))

							# Translate Text
							words = words.translate(from_lang=from_language_key, to=to_language_key)

							# Output translated text to screen
							translated_text.insert(1.0, words)

						except Exception as e:
							messagebox.showerror("Translator", e)

					def clear():
						# Clear the text boxes
						original_text.delete(1.0, END)
						translated_text.delete(1.0, END)

					# language_list = (1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,16,1,1,1,1,1,1,1,1,1,1,1,1,1)

					# Grab Language List From GoogleTrans
					languages = googletrans.LANGUAGES

					# Convert to list
					language_list = list(languages.values())

					# Text Boxes
					original_text = Text(root, height=10, width=40)
					original_text.grid(row=0, column=0, pady=20, padx=10)

					translate_button = Button(root, text="Translate!", font=("Helvetica", 24), command=translate_it)
					translate_button.grid(row=0, column=1, padx=10)

					translated_text = Text(root, height=10, width=40)
					translated_text.grid(row=0, column=2, pady=20, padx=10)

					# Combo boxes
					original_combo = ttk.Combobox(root, width=50, value=language_list)
					original_combo.current(21)
					original_combo.grid(row=1, column=0)

					translated_combo = ttk.Combobox(root, width=50, value=language_list)
					translated_combo.current(26)
					translated_combo.grid(row=1, column=2)

					# Clear button
					clear_button = Button(root, text="Clear", command=clear)
					clear_button.grid(row=2, column=1)

					root.mainloop()




				# elif 'stop watch' in self.query:
				#
				# 	# Python program to illustrate a stop watch
				# 	# using Tkinter
				# 	# importing the required libraries
				# 	import tkinter as Tkinter
				# 	from datetime import datetime
				#
				# 	counter = 66600
				# 	running = False
				#
				# 	def counter_label(label):
				# 		def count():
				# 			if running:
				# 				global counter
				# 				if counter == 66600:
				# 					display = "Starting..."
				# 				else:
				# 					tt = datetime.fromtimestamp(counter)
				# 					string = tt.strftime("%H:%M:%S")
				# 					display = string
				# 				label['text'] = display
				# 				label.after(1000, count)
				# 				counter += 1
				# 		count()
				# 	def Start(label):
				# 		global running
				# 		running = True
				# 		counter_label(label)
				# 		start['state'] = 'disabled'
				# 		stop['state'] = 'normal'
				# 		reset['state'] = 'normal'
				# 	def Stop():
				# 		global running
				# 		start['state'] = 'normal'
				# 		stop['state'] = 'disabled'
				# 		reset['state'] = 'normal'
				# 		running = False
				# 	def Reset(label):
				# 		global counter
				# 		counter = 66600
				# 		if running == False:
				# 			reset['state'] = 'disabled'
				# 			label['text'] = 'Welcome!'
				# 		else:
				# 			label['text'] = 'Starting...'
				#
				# 	root = Tkinter.Tk()
				# 	root.title("Stopwatch")
				#
				# 	# Fixing the window size.
				# 	root.minsize(width=250, height=70)
				# 	label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
				# 	label.pack()
				# 	f = Tkinter.Frame(root)
				# 	start = Tkinter.Button(f, text='Start', width=6, command=lambda: Start(label))
				# 	stop = Tkinter.Button(f, text='Stop', width=6, state='disabled', command=Stop)
				# 	reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command=lambda: Reset(label))
				# 	f.pack(anchor='center', pady=5)
				# 	start.pack(side="left")
				# 	stop.pack(side="left")
				# 	reset.pack(side="left")
				# 	root.mainloop()




				# elif 'weather' in self.query:
				# 	speak("Okay, please type in your city name in the box that will open now")
				#
				# 	import tkinter as tk
				# 	import requests
				# 	import time
				#
				# 	def getWeather(canvas):
				# 		city = textField.get()
				# 		api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"
				#
				# 		json_data = requests.get(api).json()
				# 		condition = json_data['weather'][0]['main']
				# 		temp = int(json_data['main']['temp'] - 273.15)
				# 		current_temp = int(json_data['main']['temp_min'] - 273.15)
				# 		pressure = json_data['main']['pressure']
				# 		humidity = json_data['main']['humidity']
				# 		wind = json_data['wind']['speed']
				# 		sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
				# 		sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
				#
				# 		# speak current_temp
				# 		speak("Current Temperature is")
				# 		speak(current_temp)
				# 		speak("degrees celcius")
				#
				# 		final_info = condition + "\n" + str(temp) + "°C"
				# 		final_data = "\n" + "Current temperature: " + str(
				# 			current_temp) + "°C" + "\n" + "Pressure: " + str(
				# 			pressure) + "\n" + "Humidity: " + str(
				# 			humidity) + "\n" + "Wind Speed: " + str(
				# 			wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
				# 		label1.config(text=final_info)
				# 		label2.config(text=final_data)
				#
				# 	canvas = tk.Tk()
				# 	canvas.geometry("1000x900")
				# 	canvas.title("Weather App")
				# 	f = ("poppins", 15, "bold")
				# 	t = ("poppins", 35, "bold")
				#
				# 	textField = tk.Entry(canvas, justify='center', width=20, font=t)
				# 	textField.pack(pady=20)
				# 	textField.focus()
				# 	textField.bind('<Return>', getWeather)
				#
				# 	label1 = tk.Label(canvas, font=t)
				# 	label1.pack()
				# 	label2 = tk.Label(canvas, font=f)
				# 	label2.pack()
				# 	canvas.mainloop()



				elif "hello" in self.query or "hey" in self.query or "hi" in self.query or "hai" in self.query:
					speak("Yello")




				# for fun-

				elif 'your name' in self.query:
					speak(
						"I am The Helion")





				elif 'you are my favourite' in self.query:
					speak("Thank you for that designation")


				elif 'alive' in self.query:
					speak("no, i exist only here")


				elif 'stupid' in self.query:
					speak("You stupid")
					print("You stupid")



				elif 'jokes' in self.query:
					jokes_angel()



				# Quit Helion
				elif 'go away' in self.query:
					speak("Okay")
					exit()


startExecution = MainThread()


class Main(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_JarvisUi()
		self.ui.setupUi(self)

		self.ui.pushButton_Start.clicked.connect(self.startTask)
		self.ui.pushButton_Exit.clicked.connect(self.close)

	def startTask(self):

		self.ui.movie = QtGui.QMovie("watch-dogs2-dedsec.gif")
		self.ui.gif_3.setMovie(self.ui.movie)
		self.ui.movie.start()


		timer = QTimer(self)
		timer.timeout.connect(self.showTime)
		timer.start(1000)

		startExecution.start()

	def showTime(self):
		current_time = QTime.currentTime()
		current_date = QDate.currentDate()
		label_time =  current_time.toString('hh:mm:ss')
		label_date = current_date.toString(Qt.ISODate)

		self.ui.Text_Time.setText(label_time)
		self.ui.Text_Date.setText(label_date)





app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())



