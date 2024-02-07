# Stop Watch

Simple stopwatch timer implemented in python.
Specifically, I designed this to time and store rubik's cube solves.

It supports minutes, seconds, and milliseconds.
It will loop and restart the timer until the user quits using 'q'.
Each iteration will generate a suggested scramble before the user starts the timer.
My `genScramble()` function is better than random, but still probably pretty bad.

Starting and stopping is achieved by waiting for user to press enter using `input()`.

It will write the times to file in the format

>0m 0s 0ms

Must have a file 'times.txt' in its directory to function properly.