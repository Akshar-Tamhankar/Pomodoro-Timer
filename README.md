# 🕒 Pomodoro Timer (Console App)

This is a simple **console-based Pomodoro timer** built in Python. It helps students and professionals stay focused by timing study sessions and breaks.

## Features

- User-defined study time, break time, and number of sessions
- Console-based interaction
- Simulated countdown using `time.sleep()`
- Motivational messages after each session

## How It Works

1. The program asks the user:
   - How many minutes to study per session
   - How many minutes to break between sessions
   - How many sessions to complete

2. It then prompts the user to start the timer.

3. For each session:
   - Displays a message that study time has started
   - Waits for the specified study time (simulated with `time.sleep`)
   - Displays a message that break time has started
   - Waits for the specified break time

4. After all sessions, it prints a completion message.

## Requirements

- Python 3.x

## How to Run

1. Save the script as `pomodoro_timer.py`
2. Open a terminal and run:

```bash
python pomodoro-timer.py
