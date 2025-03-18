import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import subprocess

# Ensure the absolute path is correctly set
WATCH_DIRECTORY = r"E:\CP\LeetCode 75"

class GitAutoCommitHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"Detected change in {event.src_path}. Committing...")

        subprocess.run(["git", "add", "."], cwd=WATCH_DIRECTORY)
        subprocess.run(["git", "commit", "-m", "status solved"], cwd=WATCH_DIRECTORY)
        subprocess.run(["git", "push"], cwd=WATCH_DIRECTORY)

if __name__ == "__main__":
    if not os.path.exists(WATCH_DIRECTORY):
        print(f"Error: The path {WATCH_DIRECTORY} does not exist.")
        exit(1)

    event_handler = GitAutoCommitHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_DIRECTORY, recursive=True)
    
    print(f"Watching for changes in {WATCH_DIRECTORY}...")

    try:
        observer.start()
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()
