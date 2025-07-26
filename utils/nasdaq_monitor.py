class NasdaqMonitor:
    async def check_movers(self):
        """Check TSLA/NVDA >5% moves"""
        movers = []
        for symbol in ['TSLA', 'NVDA']:
            change = self._get_change(symbol)
            if abs(change) > 5:
                movers.append(f"{symbol} {change}%")
        return movers
