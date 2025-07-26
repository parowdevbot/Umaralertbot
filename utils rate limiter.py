import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, max_calls=5, period=60):
        self.max_calls = max_calls
        self.period = period
        self.user_calls = defaultdict(list)
    
    def is_allowed(self, user_id):
        now = time.time()
        calls = self.user_calls[user_id]
        
        # Remove expired calls
        calls = [t for t in calls if now - t < self.period]
        self.user_calls[user_id] = calls
        
        if len(calls) >= self.max_calls:
            return False
        
        calls.append(now)
        return True
