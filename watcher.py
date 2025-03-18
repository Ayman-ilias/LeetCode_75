import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Watch directory
WATCH_DIRECTORY = r"E:\CP\LeetCode 75"

class GitAutoCommitHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return

        print(f"Detected change in {event.src_path}.")

        # Asking user for commit message choice
        print("\nSelect commit message:")
        print("1. Status Solved")
        print("2. Status Not Solved")
        print("3. Other (Custom Message)")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            commit_message = "status solved"
        elif choice == "2":
            commit_message = "status not solved"
        elif choice == "3":
            commit_message = input("Enter custom commit message: ").strip()
        else:
            print("Invalid choice. Defaulting to 'status solved'.")
            commit_message = "status solved"

        # Run Git commands
        subprocess.run(["git", "add", "."], cwd=WATCH_DIRECTORY)
        subprocess.run(["git", "commit", "-m", commit_message], cwd=WATCH_DIRECTORY)
        subprocess.run(["git", "push"], cwd=WATCH_DIRECTORY)

        print(f"Committed and pushed with message: {commit_message}")

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
