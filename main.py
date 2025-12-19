# Track your work hours more efficiently
# Hope this simple piece of code can ease your life a bit

import pygetwindow as gw
import time

activitiesTime = {}

def main():
    activityStartTime = time.time()
    currentActivity = gw.getActiveWindowTitle()

    try:
        while True:
            if (currentActivity != gw.getActiveWindowTitle() and gw.getActiveWindowTitle() not in ('', 'Task Switching', 'None')):
                
                activityData  = str(gw.getActiveWindowTitle()).rsplit(" - ", 1)
                currentActivity = activityData[0]

                """
                print(activityData) is find the windows or tabs you use for 
                your work and add them to activitiesToTrack...
                """
                # print(activityData)
                # print(gw.getActiveWindowTitle())

                now = time.time()

                if ("Brave" in activityData):

                    """
                    print out the current activity to get an idea if the 
                    current window or tab that you want to check is contained 
                    in the variablr or not
                    """
                    print(currentActivity)
                    elapsed = round(now - activityStartTime)
                    # activitiesTime[currentActivity] += elapsed
                    activitiesTime[currentActivity] = activitiesTime.get(currentActivity, 0) + elapsed
                
                activityStartTime = now
            time.sleep(0.5)
    except KeyboardInterrupt:
        if currentActivity in activitiesTime:
            activitiesTime[currentActivity] += round(time.time() - activityStartTime)

        # Feel free to change how you want to view the time you spent 

        print("\n==============Activity Overview==============")
        for k, v in activitiesTime.items():
            print(f"--> {k}: {time.strftime('%H:%M:%S', time.gmtime(v))}")

        total_seconds = sum(activitiesTime.values())
        totalTime = time.strftime("%H:%M:%S", time.gmtime(total_seconds))

        print("=============================================")

        print(f"\nTotal Time: {totalTime}")

if __name__ == "__main__":
    main()