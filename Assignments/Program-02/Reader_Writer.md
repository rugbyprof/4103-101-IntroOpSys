# Not Done
## Reader Writer Problem
Due: Monday November 7th by classtime.

### Overview

Many readers one writer is usually the game plan when it comes to accessing alterable resources. There are some problems 
with this strategy depending on who you give priority to. For example:

- Reader Priority = Possoble Writer Starvation
- Writer Priority = Possible Reader Starvation

Then there are ways to implement who has what access:

- If anyone is writing, then no one can read
- If anyone is writing, then readers can still access resource
- If someone is reading, writers must wait.
- If someone is writing, and a reader comes, stop writing so they can read.
- Etc.

Ultimately we create order using locks. Who gets a lock is based on priority. I would like us to create 
a rudimentary reader/writer system using the starter code [here](./starter_code.py). It gives us the ability to visualize threads using ncurses. 

I want your version of the code to do the following:

- Let readers read up to N at a time, where N is a value given to a semaphore lock
- Let 1 writer write at a time.
- Start your program with 100 readers and 5 writers.
- Start all your threads at the same time, but 

