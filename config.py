import os

# Configuration for Pro Tools session backup
# Make sure to set the correct paths for your source and destination directories

# Source directory - where your Pro Tools session files are located
SOURCE_DIR = os.path.expanduser("~/Documents/Pro Tools Sessions")

# Destination directory - where you want to back up your sessions
DEST_DIR = os.path.expanduser("~/Backups/Pro Tools Sessions")

# Function to validate directory paths
def validate_directories():
    if not os.path.exists(SOURCE_DIR):
        raise FileNotFoundError(f"Source directory does not exist: {SOURCE_DIR}")
    if not os.path.isdir(SOURCE_DIR):
        raise NotADirectoryError(f"Source path is not a directory: {SOURCE_DIR}")
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)  # Create destination directory if it doesn't exist
        print(f"Created destination directory: {DEST_DIR}")

# Call validation function to ensure paths are correct
try:
    validate_directories()
except Exception as e:
    print(f"Error in configuration: {e}")
    raise  # Re-raise to prevent silent failures

# TODO: Add configuration options for file filtering and backup frequency
# TODO: Consider adding logging for backup operations
