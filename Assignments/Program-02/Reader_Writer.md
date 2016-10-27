## Reader Writer Problem

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
a rudimentary reader/writer system using the starter code [here](./starter_code.py). 
