from random import randint
import webbrowser 
import time
from datetime import datetime, timedelta

def set_alarm():
	while True:
		time_input = raw_input("Please enter the time in YYYY/MM/DD HH:MM:SS format: ")
		user_time = datetime.strptime(time_input,"%Y/%m/%d  %H:%M:%S")

		if ( user_time < datetime.fromtimestamp(time.mktime(time.localtime()))):
				print "The specified time has passed, set a new alarm!"
		return user_time

def process():	
	#to count number of songs in text file
	num_songs = sum(1 for line in open('songs.txt')) 

	# choose a random song
	random_song = randint(0, num_songs) 
	line = open("songs.txt", "r").readlines()[random_song];

	# play the selected song 
	webbrowser.open_new_tab(line)


#main function	

user_time = set_alarm()
local = datetime.fromtimestamp(time.mktime(time.localtime()))
difference = timedelta.total_seconds(user_time - local)
time.sleep(difference)
print "Beep Beep!!"
process()
