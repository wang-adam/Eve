
import time
from word2number import w2n

import psutil
import win32gui
import win32process
w=win32gui
i = 1
dict={}

def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        pid = win32process.GetWindowThreadProcessId(hwnd)
        name = psutil.Process(pid[-1]).name()
        if name in dict:
            curr_processes = dict[name]
            curr_processes.add(hwnd)
        else:
            dict[name] = {hwnd}
        # print (hwnd, pid[-1], psutil.Process(pid[-1]).name())



# w.GetWindowText (w.GetForegroundWindow())

# pid = win32process.GetWindowThreadProcessId(w.GetForegroundWindow())

# print(psutil.Process(pid[-1]).name(), w.GetForegroundWindow())
while(True):
    time.sleep(5)
    w.EnumWindows(winEnumHandler, None)
    print(dict)
    print()
# val = " ten "
# try:
#     val = w2n.word_to_num(val)
# except Exception as e:
#     print(e)
#     val = int(val)

# print(val)