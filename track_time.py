import time
import threading
import subprocess
from datetime import datetime


def send_mac_notification(title, message):
    script = f'display notification "{message}" with title "{title}"'
    subprocess.run(["osascript", "-e", script])


def reminder_thread(reminder_interval):
    while True:
        time.sleep(reminder_interval)
        reminder_message = "You've been working for an hour. Remember to take a break or switch tasks for a healthy work-life balance."
        print(f"\n---\nReminder: {reminder_message}\n---\n")
        send_mac_notification("Time to take a break or switch tasks!", reminder_message)


def main():
    task_log = {}
    reminder_interval = 3600  # 1 hour in seconds

    # Start the reminder thread
    threading.Thread(target=reminder_thread, args=(reminder_interval,), daemon=True).start()

    try:
        while True:
            task = input("Enter task/project/client name (type 'exit' or 'end the day' to stop): ")
            if task.lower() in ["exit", "end the day"]:
                break

            start_time = datetime.now()
            print(f"Started working on {task} at {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

            command = input("Type 'stop' to stop the task, 'switch' to switch to another task, or 'end the day' to finish tracking: ")
            if command.lower() in ["stop", "switch", "end the day"]:
                end_time = datetime.now()
                duration = (end_time - start_time).total_seconds()
                task_log[task] = task_log.get(task, 0) + duration
                print(f"Stopped working on {task} at {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
                if command.lower() == "end the day":
                    break

    except KeyboardInterrupt:
        print("\nTime tracking stopped by the user.")
    finally:
        print("\nTime spent on tasks/projects/clients:")
        for task, duration in task_log.items():
            print(f"{task}: {duration / 3600:.2f} hours")


if __name__ == "__main__":
    main()
