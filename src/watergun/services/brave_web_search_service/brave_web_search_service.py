from conduit.capabilities.tools.tools.fetch.fetch import web_search


async def brave_web_search_service(query: str) -> dict[str, str]:
    """
    Perform a web search using Brave Search.

    Args:
        query (str): The search query.
        num_results (int): The number of search results to return.

    Returns:
        list: A list of search results, each containing the title, URL, and snippet.
    """
    try:
        results = await web_search(query)
        return results
    except Exception as e:
        return {"error": f"An error occurred while performing the web search: {e}"}
