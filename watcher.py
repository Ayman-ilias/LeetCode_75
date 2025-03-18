import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Watch directory
WATCH_DIRECTORY = r"E:\CP\LeetCode 75"
stop_flag = False  # Global flag to stop the script
commit_message = "status solved"  # Default commit message

class GitAutoCommitHandler(FileSystemEventHandler):
    def on_modified(self, event):
        global stop_flag, commit_message
        
        if event.is_directory or stop_flag:
            return

        print(f"Detected change in {event.src_path}. Committing...")

        # Run Git commands
        subprocess.run(["git", "add", "."], cwd=WATCH_DIRECTORY)
        subprocess.run(["git", "commit", "-m", commit_message], cwd=WATCH_DIRECTORY)
        subprocess.run(["git", "push"], cwd=WATCH_DIRECTORY)

        print(f"Committed and pushed with message: {commit_message}")

def watch_directory():
    global stop_flag, commit_message

    if not os.path.exists(WATCH_DIRECTORY):
        print(f"Error: The path {WATCH_DIRECTORY} does not exist.")
        return

    # Ask the user for commit message before starting the observer
    print("\nSelect commit message:")
    print("1. Status Solved")
    print("2. Status Not Solved")
    print("3. Other (Custom Message)")
    print("4. Stop Watching")

    while True:
        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            commit_message = "status solved"
            break
        elif choice == "2":
            commit_message = "status not solved"
            break
        elif choice == "3":
            commit_message = input("Enter custom commit message: ").strip()
            break
        elif choice == "4":
            print("Stopping watcher...")
            return
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

    # Start file watcher
    event_handler = GitAutoCommitHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_DIRECTORY, recursive=True)

    print(f"\nWatching for changes in {WATCH_DIRECTORY}...")
    print("Press 4 anytime to stop.\n")

    observer.start()

    try:
        while not stop_flag:
            time.sleep(5)
            if input().strip() == "4":
                stop_flag = True
    except KeyboardInterrupt:
        pass

    observer.stop()
    observer.join()
    print("Watcher stopped.")

if __name__ == "__main__":
    watch_directory()
