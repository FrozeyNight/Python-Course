import time
import threading

def walkTheDog(first, last):
    time.sleep(8)
    print(f"You finish walking {first} {last}")

def takeOutTrash():
    time.sleep(2)
    print("You take out the trash")

def writeMail():
    time.sleep(4)
    print("You write the mail")

chore1 = threading.Thread(target=walkTheDog, args=("Estus","Dog!"))
chore1.start()

chore2 = threading.Thread(target=takeOutTrash)
chore2.start()

chore3 = threading.Thread(target=writeMail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")