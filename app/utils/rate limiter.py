import time
from config import Config

class RateLimiter:
    def __init__(self):
        self.last_request = time.time()
        
    def check_limit(self):
        now = time.time()
        if now - self.last_request < Config.RATE_LIMIT_SECONDS:
            return False
        self.last_request = now
        return True
