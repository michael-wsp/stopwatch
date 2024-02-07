#Stop Watch

Simple stopwatch timer implemented in python.
It supports minutes, seconds, and milliseconds, but could easily be modified to support hours.
It will loop and restart the timer until the user quits using 'q'.

Starting and stopping is achieved by waiting for user to press enter (python input()).

It will write the times to file in the format

>0m 0s 0ms

Must have a file 'times.txt' in its directory to function properly.

Specifically, I designed this to time and store rubik's cube solves.

Might add a shuffle generator later on.