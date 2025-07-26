import requests
from bs4 import BeautifulSoup

class WhaleDetector:
    def __init__(self):
        self.threshold = 5_000_000  # $5M
        
    async def check_whales(self):
        """Detect large transfers"""
        data = await self._scrape_transfers()
        return [
            t for t in data 
            if t['amount_usd'] >= self.threshold
        ]
    
    def get_smart_wallets(self):
        """Load tagged performers"""
        with open('data/smart_wallets.json') as f:
            return json.load(f)
