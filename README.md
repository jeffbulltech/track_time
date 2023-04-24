# Track Time

**Track Time** is a tool that sends reminders to take breaks, stretch, or do some light exercise throughout the day by tracking the time you spend on a given task. This tool can help improve work-life balance by encouraging you to take breaks and be more active.

- - - 
## Guide to using Track Time

1. Run the script: Save the modified time tracking tool code as time_tracker.py and run it using Python 3.
2. Enter a task name: When prompted with the message "Enter task/project/client name (type 'exit' or 'end the day' to stop):", enter the name of the task, project, or client you're working on. The program will then start tracking time for that task.
3. View start time: The program will display the start time of the task in the format "Started working on [task] at [time]".
4. Receive 30 minute reminders: Every 30 minutes, the program will print a reminder message in the terminal, suggesting that you take a break or switch tasks for a healthy work-life balance. A macOS notification will also appear on the screen.
5. Stop or switch tasks: While working on a task, you can type "stop" or "switch" when prompted with the message "Type 'stop' to stop the task, 'switch' to switch to another task, or 'end the day' to finish tracking:". This will stop the current task and log its duration.
  a. If you type "stop", the program will stop tracking the current task, display the end time, and prompt you for another task name.
  b. If you type "switch", the program will stop tracking the current task, display the end time, and immediately prompt you for another task name without waiting for user input.

- - - 
## Stop tracking your time
1. End the day: To stop using the time tracking tool and display the time spent on tasks, projects, or clients, you can type "end the day" at either of the input prompts (task name or command).
2. Exit the program: Alternatively, you can also exit the program by entering "exit" when prompted for a task name.
3. View the task summary: After exiting the main loop or typing "end the day", the program will display the total time spent on each task, project, or client in hours.

You can use the time tracking tool to log the time spent on tasks, projects, or clients, receive hourly reminders to take breaks or switch tasks within the terminal window and as macOS notifications, and stop tracking time gracefully by typing "end the day" or "exit".
