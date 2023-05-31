import os
import sys
import logging

#logging string
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
#when logging it will create a file named logging/running.log
#it logs with Timestamp/ levelname[INFO, WARN, ERROR]/ which module you are running/ log message.

#creation of logs folder
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

#custome logging
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        #logging into files and also show on the console
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textSummarizerLogger")