import logging
from logging.handlers import RotatingFileHandler
import os

#Create logger
logger = logging.getLogger("smart_ai_doc_analyzer")
logger.setLevel(logging.DEBUG if os.getenv("DEBUG", "false").lower() == "true" else logging.INFO)

#Formatter
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

#console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Rotating file handler
log_file = os.getenv("LOG_FILE", "logs/app.log")
os.makedirs(os.path.dirname(log_file), exist_ok=True)

file_handler = RotatingFileHandler(
    filename=log_file,
    maxBytes=1 * 1024 * 1024, # 1 MB per log file
    backupCount=3 # keep upto 3 log files
)

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)