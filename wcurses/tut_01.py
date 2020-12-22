import curses

print("preparing to initialize....")
stdscr = curses.initscr()
print("stdscr initialized")

stdscr.addstr(0, 0, "This string gets printed at position (0, 0)")
# Python 3 required for unicode
stdscr.addstr(3, 1, "Try Russian text: Привет")
stdscr.addstr(4, 4, "X")
stdscr.addch(5, 5, "Y")

# Changes go in to the stdscr buffer and only get
# displayed after calling `refresh()` to update
stdscr.refresh()

curses.napms(3000)
curses.endwin()

print("window ended")
