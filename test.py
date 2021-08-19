import sys
import time

globalvar = 1

while True:
    sys.stdout.write("\r[{0}{1}] ".format("=" * globalvar, " " * (5 - globalvar)))
    if globalvar > 5:
        sys.stdout.write("\r[{0}] ".format(" " * (globalvar - 1)))
        globalvar = 1
    else:
        globalvar += 1
    sys.stdout.flush()
    time.sleep(1)