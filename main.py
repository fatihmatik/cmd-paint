import curses
from curses import wrapper

# NAVBAR_VARS
N_COLORS = "1:RED 2:BLUE 3:GREEN 4:YELLOW 5:PURPLE 6:CYAN 9:BLACK 0:ERASER"
N_QUIT = "Press 'Q' to quit."
N_ABOUT = "About"
N_BRUSH = "Use O and P for brush size"

NAVBAR_COLOR = 111
BLACK = 1
RED = 2
BLUE = 3
GREEN = 4
YELLOW = 5
PURPLE = 6
CYAN = 7
WHITE = 8

COLOR_PALETTE = {
    NAVBAR_COLOR: (curses.COLOR_WHITE, curses.COLOR_BLACK),
    WHITE: (curses.COLOR_WHITE, curses.COLOR_WHITE),
    BLACK: (curses.COLOR_BLACK, curses.COLOR_WHITE),
    RED: (curses.COLOR_RED, curses.COLOR_WHITE),
    BLUE: (curses.COLOR_BLUE, curses.COLOR_WHITE),
    GREEN: (curses.COLOR_GREEN, curses.COLOR_WHITE),
    YELLOW: (curses.COLOR_YELLOW, curses.COLOR_WHITE),
    PURPLE: (curses.COLOR_MAGENTA, curses.COLOR_WHITE),
    CYAN: (curses.COLOR_CYAN, curses.COLOR_WHITE),
}

BRUSH_X = 3
BRUSH_Y = 2

def setup_colors():
    curses.start_color()
    for color, (fg, bg) in COLOR_PALETTE.items():
        curses.init_pair(color, fg, bg)

def setup(stdscr, color):
    color = BLACK  # Default color

    stdscr.clear()
    setup_colors()
    stdscr.bkgd(' ', curses.color_pair(1))
    
    curses.curs_set(0)
    
    # Enable mouse events
    curses.mousemask(curses.BUTTON1_PRESSED | curses.BUTTON1_RELEASED | curses.BUTTON1_CLICKED)
    
    # Clear the screen and set up the palette
    stdscr.clear()
    stdscr.addstr(0, 0, N_COLORS + "    Current color:" + (" " * (curses.COLS - len(N_COLORS))), curses.color_pair(111))
    stdscr.addstr(0, 24 + len(N_COLORS + "Current color:"), "█████" , curses.color_pair(color))
    stdscr.addstr(1, 0, "    " + N_ABOUT + (" "*(curses.COLS - len(N_ABOUT))), curses.color_pair(111))
    stdscr.addstr(2, 0, N_QUIT + (" "*(curses.COLS - len(N_QUIT))), curses.color_pair(111))
    stdscr.addstr(3, 0, N_BRUSH + (" "*(curses.COLS - len(N_BRUSH))), curses.color_pair(111))

def render_about_page(stdscr, color):
    stdscr.clear()
    stdscr.bkgd(' ', curses.color_pair(1))
    stdscr.addstr(0,10,"Press X to go back" )
    stdscr.addstr(3,10,"Fatih Tezcan")
    stdscr.addstr(4,10,"I'm an aspiring Software Engineer.")
    stdscr.addstr(5,10,"This project was all written in windows-curses library and vanilla Python 3.12")

    stdscr.addstr(7,10,     "      __       _   _ _                     _   _ _     ")
    stdscr.addstr(8,10,     "     / _| __ _| |_(_) |__  _ __ ___   __ _| |_(_) | __ ")
    stdscr.addstr(9,10,     "    | |_ / _` | __| | '_ \| '_ ` _ \ / _` | __| | |/ / ")
    stdscr.addstr(10,10,    "    |  _| (_| | |_| | | | | | | | | | (_| | |_| |   <  ")
    stdscr.addstr(11,10,    "    |_|  \__,_|\__|_|_| |_|_| |_| |_|\__,_|\__|_|_|\_\ ")
    
    stdscr.addstr(13,10,"https://github.com/fatihmatik")

    while True:
        ch = stdscr.getch()
        if ch == ord('x') or ch == ord('X'):
            setup(stdscr, color)
            break

def main(stdscr):
    global BRUSH_Y, BRUSH_X
    color = BLACK  # Default color

    setup(stdscr, color)

    while True:
        ch = stdscr.getch()

        if ch == ord('0'):
            color = WHITE
        elif ch == ord('1'):
            color = RED
        elif ch == ord('2'):
            color = BLUE
        elif ch == ord('3'):
            color = GREEN
        elif ch == ord('4'):
            color = YELLOW
        elif ch == ord('5'):
            color = PURPLE
        elif ch == ord('6'):
            color = CYAN
        elif ch == ord('9'):
            color = BLACK
        elif ch == ord('o') or ch == ord('O'):
            if BRUSH_X < 8:
                BRUSH_X += 1
                BRUSH_Y += 1
        elif ch == ord('p') or ch == ord('P'):
            if BRUSH_X > 2:
                BRUSH_X -= 1
                BRUSH_Y -= 1
        elif ch == curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.getmouse()
            if my >= 5 and my <= curses.LINES-(BRUSH_Y+1) and mx <= curses.COLS-(BRUSH_X+1) and mx>=1:
                for itr in range(0,BRUSH_Y,1):
                    stdscr.addstr(my+itr, mx, "█" * BRUSH_X, curses.color_pair(color))
            elif my == 1 and mx >= 3 and mx <= 10:
                render_about_page(stdscr, color)

        elif ch == ord('x') or ch == ord('X'):
            setup(stdscr, color)
        elif ch == ord('a') or ch == ord('a'):
            render_about_page(stdscr, color)
        elif ch == ord('q') or ch == ord('Q'):
            break

        stdscr.addstr(0, 5 + len(N_COLORS + "Current color:"), "█████" , curses.color_pair(color))

wrapper(main)
