import curses
from curses import wrapper
import time

from dataclasses import dataclass

FPS = 60

class MenuManager:
    def __init__(self, stdscr) -> None:
        self.stdscr = stdscr

        self.menu = {}
        self.menu["tag"] = "info"
        self.menu["toggled"] = False
        self.menu["data"] = None

        a = {}
        a["tag"] = "stuff"
        a["toggled"] = False
        a["data"] = None
        self.menu["data"] = a

    def render(self) -> None:
        #self.stdscr.addstr(self.menu["tag"])
        self.stdscr.addstr(a)

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)    # Do not wait for input when calling getch

    menuManager = MenuManager(stdscr)

    while True:
        stdscr.clear()

        menuManager.render()

        stdscr.refresh()

        data = stdscr.getch()    # [TODO] Change this so it is automatic polling instead

        if data in [ord("q"), ord("Q")]: return

        #if data == curses.KEY_RIGHT: menu.expand()
        #if data == curses.KEY_LEFT: menu.close()

        time.sleep(1.0 / FPS)

wrapper(main)
