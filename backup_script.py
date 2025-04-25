import shutil
import os
from datetime import datetime

# Define the source directory and backup directory
SOURCE_DIR = "Source dir"  # Change this to your source directory
BACKUP_DIR = "Backup dir"   # Change this to your backup directory

def create_backup():
    # Create a timestamp for the backup folder
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder = os.path.join(BACKUP_DIR, f"backup_{timestamp}")

    try:
        # Copy the source directory to the backup folder
        shutil.copytree(SOURCE_DIR, backup_folder)
        print(f"Backup created successfully at: {backup_folder}")
    except Exception as e:
        print(f"Error creating backup: {e}")

if __name__ == "__main__":
    create_backup()