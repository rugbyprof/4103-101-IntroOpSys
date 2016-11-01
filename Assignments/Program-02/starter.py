import threading
import os
from os import system
import curses
import locale
import time
import threading
import random
import json
import struct

screenLock = threading.Lock()

"""
Location object to help the Curses Window class
"""
class Cell(object):
    def __init__(self,row=0,col=0):
        self.row = row
        self.col = col

"""
Curses Window wrapper to help with printing to the screen
"""
class CursesWindow(object):
        
    def __init__(self):
        self.screen = curses.initscr()

        self.maxy,self.maxx = self.screen.getmaxyx()
        curses.start_color()
        curses.use_default_colors()
        curses.cbreak()
        self.colors = self.loadColors()

        for c in self.colors:
            r,g,b = c['curses']
            i = int(c['index'])
            curses.init_color(i,r,g,b)
            curses.init_pair(i,i,-1)

        self.screen.border(0)    

    """
    Loads the possible colors from colors.csv
    """
    def loadColors(self):
        f = open("colors.csv","r")

        colors = []

        for line in f:
            temp = line.strip()
            temp = temp.split(',')
            rgb = struct.unpack('BBB',temp[2].strip('#').decode('hex'))
            curses = (int(rgb[0]/255.0*1000.0),int(rgb[1]/255.0*1000.0),int(rgb[2]/255.0*1000.0))
            colors.append({'index':temp[0],'name':temp[1].strip(),'hex':temp[2].strip(),'curses':curses,'rgb':rgb})

        f.close()
        
        return colors
    
    def getColorNames(self):
        names = []
        for c in self.colors:
            names.append(c['name'])
        return names

    
    def cprint(self,row,col,string,color=0):
        try: 

            self.screen.addstr(row, col, string, curses.color_pair(color))
            self.screen.addch(row, col-2, '#',curses.color_pair(color))      
        except:
            print("Unexpected error:", row, col, string, color)
            
            raise
        self.screen.refresh()
    
    def randomColor(self):
        """visibile colors"""
        return random.randint(1,len(self.colors))
        
    def getColor(self,key,val):
        
        for c in self.colors:
            if c[key] == val:
                return c
        
        return None
        
    def exit(self):
        self.screen.getch()
        curses.endwin()
        

"""=========================================================="""

# Layout of the table (P = philosopher, f = fork):
#          P0
#       f3    f0
#     P3        P1
#       f2    f1
#          P2

# Number of philosophers at the table. 
# There'll be the same number of forks.
numPhilosophers = 4

# Lists to hold the philosophers and the forks.
# Philosophers are threads while forks are locks.
philosophers = []
forks = []

screenLock = threading.Lock()

class Philosopher(threading.Thread):
    def __init__(self, index,window,cell):
        threading.Thread.__init__(self)
        self.index = index
        self.window = window
        self.cell = cell
        self.color = self.window.randomColor()  # Color to draw with
        

    def run(self):
        # Assign left and right fork
        leftForkIndex = self.index
        rightForkIndex = (self.index - 1) % numPhilosophers
        forkPair = ForkPair(leftForkIndex, rightForkIndex)
        
        # This prints out the threads name on the left of our "progress bar"
        with screenLock:
            self.window.cprint(self.cell.row, self.cell.col, str(self.index),self.color)
        self.cell.col += 5

        # Eat forever
        while True:
            forkPair.pickUp()
            with screenLock:
                self.window.cprint(self.cell.row, self.cell.col, "#" ,self.color)
                self.cell.col += 1
                if self.cell.col >= self.window.maxx-2:
                    self.cell.col = 10
                    for i in range(10,self.window.maxx-2):
                        self.window.cprint(self.cell.row, i, "#",16)
                time.sleep(.05)
            time.sleep(.01)
            forkPair.putDown()

class ForkPair:
    def __init__(self, leftForkIndex, rightForkIndex):
        # Order forks by index to prevent deadlock
        if leftForkIndex > rightForkIndex:
            leftForkIndex, rightForkIndex = rightForkIndex, leftForkIndex
        self.firstFork = forks[leftForkIndex]
        self.secondFork = forks[rightForkIndex]
    

    def pickUp(self):
        # Acquire by starting with the lower index
        self.firstFork.acquire()
        self.secondFork.acquire()

    def putDown(self):
        # The order does not matter here
        self.firstFork.release()
        self.secondFork.release()

if __name__ == "__main__":

    screenLock = threading.Lock()
    window = CursesWindow()
    row = 5
    
    # Create philosophers and forks
    for i in range(0, numPhilosophers):
        philosophers.append(Philosopher(i,window,Cell(5+row,5)))
        forks.append(threading.Lock())
        row += 1

    # All philosophers start eating
    for philosopher in philosophers:
        philosopher.start()

    # Allow CTRL + C to exit the program
    try:
        while True: time.sleep(021)
    except (KeyboardInterrupt, SystemExit):
        os._exit(0)
