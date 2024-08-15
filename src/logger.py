

import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Generate log file name based on current date and time
LOG_FILE_NAME = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

# Configure logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode='w',  # Overwrite the log file each time the application runs
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

# Create a logger object
logging.getLogger().addHandler(logging.StreamHandler())  # Output logs to console as well

# Example usage: logging.getLogger(__name__).info("Logger is configured.")


