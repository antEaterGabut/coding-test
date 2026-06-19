import sys
import time as tm

fruit = ["manggo", "apple", "guava", "banana"]
newList = [x for x in fruit if x != "guava"]

def runtyping(kata, kecepatan=0.05):
    for text in kata:
        sys.stdout.write(text)
        sys.stdout.flush()
        tm.sleep(kecepatan)
    print()

for listt in newList:
    runtyping(listt)