import os
import time
import keyboard
import sys
import termios
import atexit


def enable_echo(enable):
    fd = sys.stdin.fileno()
    new = termios.tcgetattr(fd)
    if enable:
        new[3] |= termios.ECHO
    else:
        new[3] &= ~termios.ECHO

    termios.tcsetattr(fd, termios.TCSANOW, new)


atexit.register(enable_echo, True)
enable_echo(False)


class Screen:
    def __init__(self, X, Y) -> None:
        self.X = X
        self.Y = Y
        self.O = (X - 2, Y)
        self.A = (1, Y)
        self.init_screen()

    def draw(self):
        self.clear()
        for row in self.screen:
            print("".join(row), flush=True)

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

        def init_screen(self):
        self.screen = (
                [["*" for _ in range(self.X)]]
                + [["*"] + [" " for _ in range(self.X - 2)] + ["*"] for _ in range(self.Y)]
                + [["*" for _ in range(self.X)]]
        )

        if self.O is not None:
            self.screen[self.O[1]][self.O[0]] = "O"

        if self.A is not None:
            self.screen[self.A[1]][self.A[0]] = "A"


s = Screen(50, 5)


def onKeyUp():
    for y in range(s.Y):
        s.A = (1, s.Y - y)
        time.sleep(0.2)

    for y in range(s.Y):
        s.A = (1, y + 1)
        time.sleep(0.2)


keyboard.add_hotkey("space", onKeyUp)

while True:
    s.O = (((s.O[0] - 1) % (s.X - 2)), s.O[1])
    s.init_screen()
    s.draw()
    time.sleep(0.2)
