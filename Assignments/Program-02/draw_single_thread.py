#!/usr/bin/env python

"""
This is a bare bones print a thread example.

"""

from os import system
import curses
import locale
import time
import threading
import random
import heapq

screenLock = threading.Lock()

class cell(object):
    def __init__(self,row=0,col=0):
        self.row = row
        self.col = col

class CursesWindow(object):
        
    def __init__(self):
        self.screen = curses.initscr()

        curses.start_color()
        curses.use_default_colors()
        curses.cbreak()
        for i in range(0, curses.COLORS/2):
            curses.init_pair(i + 1, i, -1)
            curses.init_pair(i + 1 + curses.COLORS/2, i, i)
        

        self.screen.border(0)    
    
    def cprint(self,row,col,string,color=0):
        self.screen.addstr(row, col, string,curses.color_pair(color))
        self.screen.refresh()

    
    def randomColor(self):
        """visibile colors"""
        return random.randint(21,232)
        
    def exit(self):
        self.screen.getch()
        curses.endwin()

"""=========================================================="""


class myThread(threading.Thread):
    global screenLock
    
    def __init__(self, cell,window,priority=None,name=None):
        # Call parent constructor (thread)
        threading.Thread.__init__(self)
        
        self.cell = cell                        # Where to print output
        self.window = window                    # Window object to draw with
        self.color = self.window.randomColor()  # Color to draw with
        self.priority = priority                # Threads priority if needed
        if not name == None:                    # If we pass in a name, use it
            self.name = name                    

    """
    String Representation of the thread object
    """
    def __str__(self):
        return "(Name:%s , Priority:%s , Color:%s)" % (self.name , self.priority, self.color)
    """
    Calls __str__
    """
    def __repr__(self):
        return self.__str__()


    def run(self):

        # This prints out the threads name on the left of our "progress bar"
        with screenLock:
            self.window.cprint(self.cell.row, self.cell.col, str(self.name),self.color)
        self.cell.col += 20

        # This prints out a "70" character long progress bar to the right of the threads name
        for i in range(70):
            with screenLock:
                self.window.cprint(self.cell.row, self.cell.col+i, "#" ,self.color+curses.COLORS/2)
            time.sleep(.01)
    
    """
    This overloads the "==" operation so that threads can be "sorted" in a list structure.
    The comparison is between two threads priorities. 
    """
    def __cmp__(self,rhs):
        return cmp(self.priority,rhs.priority)
        
    def __lt__(self,rhs):
        return self.priority < rhs.priority


        
if __name__=='__main__':

    
    window = CursesWindow()
    
    thread = myThread(cell(10,10),window)

    thread.start()
        
    thread.join()      

    window.exit()
    
