# Simple time recorder Python script in Notepad++
# By Mikey Beck
# Note: Rounds to nearest 5 minutes

#TODO: Total for each day/client - done?
#TODO: Only have one *in progress* per file, don't need to be on same line to use it..maybe?


''' If user has selected text, simply calculate and print total time '''

selected = editor.getSelText()
if selected != "":
	totalHours = 0
	totalMinutes = 0
	
	lines = selected.split('\n')
	for line in lines:
		#Get duration i.e. (10:20)
		duration = (line[28:36]) #This is not strictly necessary..
		#Get hours
		hours = duration[duration.find("(")+1:duration.find(":")]
		minutes = duration[duration.find(":")+1:duration.find(")")]
		
		if hours.isdigit():
			totalHours += int(hours)
	
		if minutes.isdigit():
			totalMinutes += int(minutes)
	
	totalHours += (totalMinutes / 60)
	totalMinutes = (totalMinutes % 60)
	print "Total: (" + str(totalHours) + ":" + str(totalMinutes) + ")"
	
else:

	import time
	import datetime

	line = editor.getCurLine()

	date = time.strftime( '%d/%m/%Y' )
	time = datetime.datetime.now()

	''' Round to nearest 5 minutes '''
	time = time - datetime.timedelta(minutes=time.minute % 2.5,
								 seconds=time.second,
								 microseconds=time.microsecond)

	discard = datetime.timedelta(minutes=time.minute % 5,
								 seconds=time.second,
								 microseconds=time.microsecond)
	time -= discard
	if discard >= datetime.timedelta(minutes=2.5):
		time += datetime.timedelta(minutes=5)
	
	time = time.strftime('%I:%M%p')



	if '*In progress*' in line:
		currentLineNum  = editor.lineFromPosition(editor.getCurrentPos())
		
		#Get time difference between start & end times
		startTime = line[:18] #TODO: make this more robust
		startTime = datetime.datetime.strptime(startTime, '%d/%m/%Y %I:%M%p')
		endTime = date + " " + time
		endTime = datetime.datetime.strptime(endTime, '%d/%m/%Y %I:%M%p')
		timeDiff = endTime - startTime
		timeDiff = "(" + str(timeDiff)[:-3] + ")"
		
		line = line.replace("*In progress*", "- " + time + " " + timeDiff + " ");
		editor.replaceLine(currentLineNum, line)
		#Go to end of 'current' line	
		EOL = editor.getCurrentPos() + len(editor.getCurLine()) - 2 #This gets the caret to the end of the line, ready to type
		editor.gotoPos(EOL)
	else:
		editor.addText(date + " " + str(time) + " *In progress*")