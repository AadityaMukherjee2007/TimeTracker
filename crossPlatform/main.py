import pywinctl as pwc
import time, os

activitiesTime = {}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def displayTrackedActivities():
    print("\n=====================Activity Overview=====================")
    for k, v in activitiesTime.items():
        print(f"--> {k}: {time.strftime('%H:%M:%S', time.gmtime(v))}")

    total_seconds = sum(activitiesTime.values())
    totalTime = time.strftime("%H:%M:%S", time.gmtime(total_seconds))

    print("===========================================================")
    print(f"\nTotal Time: {totalTime}")



def main():
    currentActivity = (pwc.getActiveWindow()).title
    activity_start_time = time.time()

    try:
        while True:
            try:
                window = pwc.getActiveWindow()

                if currentActivity != window.title:
                    print(currentActivity)

                    now = time.time()
                    elapsed = round(now - activity_start_time)
                    activitiesTime[currentActivity] = activitiesTime.get(currentActivity, 0) + elapsed
                    activity_start_time = now
                    currentActivity = window.title


                displayTrackedActivities()
                time.sleep(1)
                clear_screen()
            except Exception as e:
                print(e)
    except KeyboardInterrupt:
        if currentActivity in activitiesTime:
            activitiesTime[currentActivity] += round(time.time() - activity_start_time)

        displayTrackedActivities()



if __name__ == "__main__":
    main()

