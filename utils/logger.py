import logging
import os
from config import Config

def setup_logger():
    """Configure logging with file and console output"""
    try:
        # Create logs directory if it doesn't exist
        os.makedirs(os.path.dirname(Config.LOG_FILE), exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(Config.LOG_FILE),
                logging.StreamHandler()
            ]
        )
    except Exception as e:
        print(f"Failed to setup logger: {e}")
        # Fallback to basic config
        logging.basicConfig(level=logging.INFO)
