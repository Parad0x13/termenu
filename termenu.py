# [TODO] Consider using dataclasses for init stuff instead...

import curses
from curses import wrapper
import time

from dataclasses import dataclass

FPS = 60

# Menus can be branches or leaves and can folded however you want
# Indenting and all that stuff will be included
# You can also have as many menus as you want too
# Each menu/child-menu can be animated in any way it wants as well
# So 'technically' each menu entry is a single line each
# [TODO] Find out how to do line wrapping... if I even need it
class Menu:
    def __init__(self, stdscr, text = "Default Menu Text") -> None:
        self.stdscr = stdscr

        self.expanded = False
        self.submenus = []

        self.text = text

    def addSubmenu(self, menu):
        self.submenus.append(menu)

    def expand(self):
        self.expanded = True

    def close(self):
        self.expanded = False

    """
    def scroll(self, dir):
        if dir == -1:
            self.selection -= 1
        elif dir == 1:
            self.selection += 1

        if self.selection < 0: self.selection = len(self.entries) - 1
        if self.selection > len(self.entries) - 1: self.selection = 0
    """

    def render(self, xOffset = 0, yOffset = 0):
        rows, cols = self.stdscr.getmaxyx()

        # [TODO] Move this elsewhere
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

        prefix = "? "
        if len(self.submenus) == 0: prefix = ""
        if len(self.submenus) != 0 and not self.expanded: prefix = "+ "
        if len(self.submenus) != 0 and self.expanded: prefix = "- "

        if not self.expanded: color = curses.color_pair(1)
        if self.expanded: color = curses.color_pair(2)
        self.stdscr.addstr(yOffset, xOffset, prefix, color)
        self.stdscr.addstr(self.text)

        if self.expanded:
            for menu in self.submenus:
                menu.render(xOffset = xOffset + 2, yOffset = yOffset + 1)

    def tick(self):
        pass

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)    # Do not wait for input when calling getch

    menu = Menu(stdscr, "Layer1")
    menu2 = Menu(stdscr, "Layer2")
    menu3 = Menu(stdscr, "Layer3")
    menu.addSubmenu(menu2)
    menu2.addSubmenu(menu3)

    while True:
        stdscr.clear()

        menu.render()

        stdscr.refresh()

        data = stdscr.getch()    # [TODO] Change this so it is automatic polling instead

        if data in [ord("q"), ord("Q")]: return

        if data == curses.KEY_RIGHT: menu.expand()
        if data == curses.KEY_LEFT: menu.close()

        time.sleep(1.0 / FPS)

wrapper(main)
