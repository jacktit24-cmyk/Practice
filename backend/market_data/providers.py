"""Abstract provider interfaces for pluggable market data sources."""
from typing import Protocol


class MarketDataProvider(Protocol):
    """Contract for symbol and option chain lookups from external providers."""

    def get_spot_price(self, symbol: str) -> float:
        """Return the latest spot price for a symbol."""
