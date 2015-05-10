# notepad-plus-plus-time-recorder

###How to use:

I'm assuming you have the Notepad++ Python script plugin installed and know how to use it.

Install this script and assign a key to it (I like to use F5).

####The 'timer'

To start the 'timer', open a blank text file (or any file really) and press F5.  You should see something similar to the following:
<pre>
10/05/2015 08:15PM *In progress* 
</pre>
To stop the 'timer', ensure the same line is selected, then press F5 again.  You should see something like this:

10/05/2015 08:15PM - 08:35PM (0:20) 

####Calculating total time spent

Highlight the lines created by the script and press F5 again.  The total should be printed at the cursor position.

#####For example:

Highlight the following three lines:
07/05/2015 08:15PM - 08:35PM (0:20)
09/05/2015 08:40PM - 08:45PM (0:05) 
10/05/2015 08:40AM - 08:45PM (12:05)

And press F5:
07/05/2015 08:15PM - 08:35PM (0:20)
09/05/2015 08:40PM - 08:45PM (0:05) 
10/05/2015 08:40AM - 08:45PM (12:05)

Total: (12:30)


####Note:
You can record time periods longer than 23:59, resulting in something like the following:

08/05/2015 08:45PM - 08:50PM (2 days, 0:05) 

but the total calculator won't work.  If you want to calculate periods > 24 hours at a time, you'll need to add this functionality yourself.

