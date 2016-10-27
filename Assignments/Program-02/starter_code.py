#!/usr/bin/env python

from os import system
import curses
import locale

locale.setlocale(locale.LC_ALL,"")

import time
import threading
import random
from random import shuffle
import heapq



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

class PriorityQueue(object):
    def __init__(self,threads=[],resource_count=1):
        self.heap = []
        self.heap.extend(threads)
        self.semLock = threading.Semaphore(resource_count)
        self.current = 0
    
    def push(self,item):
        self.heap.append(item)
    
    def heapify(self):
        heapq.heapify(self.heap)
                
        
    def sort(self):
        self.heap.sort()
        
    def __str__(self):
        string = ""
        for i in self.heap:
            string += i.__str__()
            
        return string
        
    def __repr__(self):
        return self.__str__()
        
    def __iter__(self):
        return self

    def next(self): # Python 3: def __next__(self)
        if self.current > len(self.heap)-1:
            raise StopIteration
        else:
            self.current += 1
            return self.heap[self.current - 1]



class Reader(threading.Thread):
    global screenLock
    global queue
    global database
    
    def __init__(self, cell,window,priority,name=None):
        # Call parent constructor (thread)
        threading.Thread.__init__(self)
        
        self.cell = cell
        self.window = window
        self.color = self.window.randomColor()
        self.priority = priority
        self.color = self.priority
        self.name = name
    
    def __str__(self):
        return "(Name:%s , Priority:%s , Color:%s)" % (self.name , self.priority, self.color)
        
    def __repr__(self):
        return self.__str__()
        
    def run(self):
        with queue.semLock:
            with screenLock:
                self.window.cprint(self.cell.row, self.cell.col, str(self.priority),self.color)
            self.cell.col += 20

            for i in range(70):
                with screenLock:
                    self.window.cprint(self.cell.row, self.cell.col+i, "#" ,self.color+curses.COLORS/2)
                time.sleep(.01)
                
    def __cmp__(self,rhs):
        return cmp(self.priority,rhs.priority)
        
    def __lt__(self,rhs):
        return self.priority < rhs.priority

    
        
if __name__=='__main__':

    screenLock = threading.Lock()          # Write lock for screen
    database = []                          # what everyone wants
    queue = PriorityQueue(resource_count=3)
    
    window = CursesWindow()
    
    
    row = 10
    
    priorities = [10,20,30]

    
    for i in range(20):
        shuffle(priorities)
        queue.push(Reader(cell(row+i,10),window,priorities[0],name=i))
        
    queue.sort()

        
    for thread in queue:
        thread.start()
        
    for thread in queue:
        thread.join()
        

    window.exit()
    
    
    
    
    
    
    
    
    
