import os
import shutil
import datetime
import logging

# Define configuration constants directly since config.py is missing
BACKUP_DIR = os.path.join(os.getcwd(), 'backups')
SESSION_DIR = os.path.join(os.getcwd(), 'sessions')

# Setup logging for the backup process
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def backup_pro_tools_sessions():
    try:
        # Check if the session directory exists
        if not os.path.exists(SESSION_DIR):
            logging.error(f"Session directory does not exist: {SESSION_DIR}")
            return

        # Create backup directory if it doesn't exist
        os.makedirs(BACKUP_DIR, exist_ok=True)

        # Get the current timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        # Loop through all files in the session directory
        for filename in os.listdir(SESSION_DIR):
            # Check if the file is a Pro Tools session file
            if filename.endswith('.ptx'):
                full_file_path = os.path.join(SESSION_DIR, filename)
                # Create a backup filename with timestamp
                backup_filename = f"{os.path.splitext(filename)[0]}_{timestamp}.ptx"
                backup_file_path = os.path.join(BACKUP_DIR, backup_filename)

                # Copy the file to the backup directory
                shutil.copy(full_file_path, backup_file_path)
                logging.info(f"Backed up: {filename} to {backup_filename}")

    except Exception as e:
        logging.error(f"An error occurred during backup: {e}")

if __name__ == "__main__":
    backup_pro_tools_sessions()
