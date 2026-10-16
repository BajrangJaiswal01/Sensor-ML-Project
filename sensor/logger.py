import logging 
import os 
import sys 
from datetime import datetime 

# 1 - create a file (log file) 
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" 

# 2 - create a folder and join with path using os (eg - F:\My Projects\ML Projects\Sensor ML project\sensor\exception.py)
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)

# 3 - if path already exists then dont create more folder
os.makedirs(logs_path,exist_ok=True)

# 4 - complete path
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)