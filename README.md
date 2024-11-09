# PRODIGY_CS_04
A basic keylogger program that captures and logs keystrokes to a file, designed for ethical use with proper permissions.

# Description:

This task/Project involves creating a basic keylogger that records and logs keystrokes to a file. This keylogger operates on a timer and captures all keystrokes within a specified duration (in this case, 10 seconds). The primary goal is to focus on the logging of keys pressed and saving them to a text file for further analysis.

" Ethical considerations and permissions are critical for any project involving keylogging to ensure it is used responsibly and legally..."

# Features:

1. Captures keystrokes and saves them to a text file (key_log.txt) with minimal setup.
2. The program stops logging after a set time interval (10 seconds).
3. Prevents keystrokes from displaying in the terminal while running, logging only to the file.
4. A message displayed to ensure that users understand the ethical importance of using such tools responsibly.

# Working of keylogger program:

Lets see the breakdown of how each part of this keylogger program works...

# Imports and Setup

1. The " keyboard " module is used to capture keystrokes.
2. " time " is used to set the timeout duration for keylogging.
3. " datetime " is imported to record timestamps if needed in an extended version of this code (although it’s not used here).

# Define the Log File and Timeout

1. " log_file " defines the name of the file where keystrokes will be saved.
2. " timeout " is set to 10 seconds, which means the keylogger will only run for this period before stopping.

# Logging Function - " log_key "

1. This function receives a " key "event (which is detected in the main loop).
2. It opens " key_log.txt " in append mode and writes the key name with a space after each entry.
3. If an error occurs (like a file access issue), it will print an error message to the terminal.

# Start Keylogger Function - " start_keylogger "

1. The " start_keylogger " function:
        - Prints a reminder about ethical use.
        - Initializes a " start_time " to track how long the program has been running.
        - The main loop (while time.time() - start_time < timeout) continues until the time elapsed reaches the "timeout".

2. Inside the loop:

        - " keyboard.read_event(suppress=True) " captures each key event and suppresses its display in the terminal.
        - If the event type is " keyboard.KEY_DOWN " (a key being pressed), the " log_key " function is called to log the key into " key_log.txt "

3. After 10 seconds, the loop ends, and the program prints a message to indicate the keylogger has stopped.

# Main Block - Run the Keylogger

This block ensures that " start_keylogger() " is only run if the script is executed directly, not if it’s imported as a module.

# Example Output in key_log.txt:

When this program runs, it will:

Start logging keystrokes and display a message: "Starting keylogger... (Ethical use only with permission)".
Record any key you press during the next 10 seconds.
Save all keystrokes to a file named " key_log.txt " in the same directory, with each keystroke separated by a space.
After 10 seconds, it will stop and display "Keylogging stopped after 10 seconds. Ethical use only with permission."

If we type the following during the 10 seconds:

Hello123!

The " key_log.txt " file will look like:

h e l l o 1 2 3 !

# Overview of How the Code Works...

1. Initialization:---------------> The keylogger setup defines a log file and timeout duration.
2. Keystroke Capture:------------> The " keyboard.read_event(suppress=True) " function listens for keypress events and passes each key to the " log_key " function.
3. File Logging:-----------------> The " log_key " function appends each captured key to " key_log.txt"
4. Time-Based Stopping:----------> The " while " loop limits keylogging to 10 seconds.
5. Ethical Reminder:-------------> Reminders are printed to emphasize ethical usage of the keylogger.

This program provides a basic foundation for a keylogger that can log keystrokes within a specified duration, store them in a file, and operate discreetly without displaying keystrokes in the terminal.

# Ethical Considerations

It's crucial to only use this tool for ethical and legal purposes, such as personal testing, educational demonstrations, or research where proper permissions have been obtained. Unauthorized use of keyloggers can be illegal and unethical. Always ensure that we have clear consent before running this program on any system or device.

# Final Thoughts

This task is an excellent way to understand the basics of keylogging and event handling in Python. By completing it, I've gained insights into capturing real-time inputs, managing files, and implementing time-based execution....