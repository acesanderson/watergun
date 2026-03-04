from conduit.capabilities.tools.tools.fetch.fetch import fetch_url
from typing import Any


async def fetch_url_service(url: str, page: int = 1) -> dict[str, Any]:
    """
    Fetches the content of a URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The content of the URL.
    """
    return await fetch_url(url, page)
