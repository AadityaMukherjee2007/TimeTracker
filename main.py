# Track your work hours more efficiently
# Hope this simple piece of code can ease your life a bit

import pygetwindow as gw
import time

activitiesToTrack = {
    'Asana': 0, 
    'BlueVector AI, LLC Mail': 0, 
    'Log Timesheet': 0, 
    'Building No-Code Apps with SnapApp: Foundations': 0, 
    'BVI Implementation Services': 0
}

def main():
    activityStartTime = time.time()
    currentActivity = gw.getActiveWindowTitle()

    try:
        while True:
            if (currentActivity != gw.getActiveWindowTitle() and gw.getActiveWindowTitle() not in ('', 'Task Switching', 'None')):
                activityData  = str(gw.getActiveWindowTitle()).split(" - ")

                """
                print(activityData) is find the windows or tabs you use for 
                your work and add them to activitiesToTrack...
                """
                # print(activityData)
                # print(gw.getActiveWindowTitle())

                if len(activityData) > 2:
                    currentActivity = activityData[-2]  

                """
                print out the current activity to get an idea if the 
                current window or tab that you want to check is contained 
                in the variablr or not
                """
                # print(currentActivity)

                now = time.time()

                if (currentActivity in activitiesToTrack):
                    elapsed = round(now - activityStartTime)
                    activitiesToTrack[currentActivity] += elapsed
                
                activityStartTime = now
            time.sleep(0.5)
    except KeyboardInterrupt:
        if currentActivity in activitiesToTrack:
            activitiesToTrack[currentActivity] += round(time.time() - activityStartTime)

        # Feel free to change how you want to view the time you spent 

        print("\nActivity Overview")
        for k, v in activitiesToTrack.items():
            print(f"{k}: {time.strftime('%H:%M:%S', time.gmtime(v))}")

        total_seconds = sum(activitiesToTrack.values())
        totalTime = time.strftime("%H:%M:%S", time.gmtime(total_seconds))

        print(f"\nTotal Time: {totalTime}")

if __name__ == "__main__":
    main()