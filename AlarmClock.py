import time
import datetime

def startAlarm(targetTime):
    isRunning = True

    while isRunning:
        currentTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(currentTime)
        
        if currentTime == targetTime:
            print("Time's up!")
            isRunning = False

        time.sleep(1)

if __name__ == "__main__":
    targetTime = input("Please enter in a time HH:MM:SS: ")
    print(f"Target time is {targetTime}")
    startAlarm(targetTime)