from os import system
import curses
import locale
import struct
import json

class cell(object):
    def __init__(self,row=0,col=0):
        self.row = row
        self.col = col

class CursesWindow(object):
        
    def __init__(self):
        self.screen = curses.initscr()

        self.maxy,self.maxx = self.screen.getmaxyx()
        curses.start_color()
        curses.use_default_colors()
        curses.cbreak()
        self.colors = self.loadColors()
        #curses.COLORS
        for c in self.colors:
            r,g,b = c['curses']
            i = int(c['index'])
            curses.init_color(i,r,g,b)
            curses.init_pair(i,i,-1)

        self.screen.border(0)    

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
        
    def colorIndex(self,name):
        return self.colors[name]['index']
        
    def exit(self):
        self.screen.getch()
        curses.endwin()
        
 
if __name__=='__main__':

    
    window = CursesWindow()
    row = 1
    col = 3
    total = 0
    for c in window.colors:
        window.cprint(row, col, str(c['name']), int(c['index']))
        row += 1
        if row >= window.maxy-2:
            row = 1
            col += 25
        if col >= window.maxx-10:
            break
            
    window.exit()
