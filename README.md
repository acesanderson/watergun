# Watergun

Watergun is a specialized API server that provides a suite of tools for Open WebUI and LLM agents, enabling web search, content scraping, and document retrieval.

## Quick Start

Install the package and its dependencies using pip:

```bash
pip install .
```

Start the server:

```bash
watergun
```

The server runs by default on `http://0.0.0.0:8081`. You can verify it is active by visiting the ping endpoint:

```bash
curl http://localhost:8081/ping
```

## Core Functionality

Watergun bridges LLM interfaces with external data sources through three primary modules:

*   **Brave Web Search**: Performs live web searches to provide real-time information.
*   **URL Fetching**: Extracts and processes content from specific web pages for LLM context.
*   **Obsidian Integration**: Connects to local Obsidian vaults for personal knowledge retrieval.

### Example: Search and Fetch

To perform a search and retrieve content programmatically:

```bash
# Search for information
curl "http://localhost:8081/search/brave_web_search?query=fastapi+best+practices"

# Fetch specific page content
curl "http://localhost:8081/fetch/fetch_url?url=https://example.com"
```

## Architecture

The project follows a layered architecture to ensure separation of concerns:

1.  **API Layer (`/api`)**: FastAPI route definitions that handle HTTP requests and parameter validation.
2.  **Service Layer (`/services`)**: Business logic that coordinates between the API and underlying capabilities.
3.  **Core Capabilities**: Integration with the `conduit` library for heavy lifting like web scraping and search API interactions.

### Component Interaction
*   **Server**: Managed by Uvicorn with centralized logging via the Rich library.
*   **Error Handling**: Global exception handlers provide structured JSON responses for validation and runtime errors.
*   **Logging**: Persistent logs are stored in the XDG state directory under `headwater_server/logs/server.log`.

## Installation and Setup

### Prerequisites
*   Python 3.12 or higher
*   Access to the `conduit` package (defined as a local dependency in `pyproject.toml`)

### Environment Configuration
The server's verbosity can be adjusted using the `PYTHON_LOG_LEVEL` environment variable:

| Level | Value | Description |
| :--- | :--- | :--- |
| WARNING | 1 | Minimal output, errors only |
| INFO | 2 | Standard operational logs (Default) |
| DEBUG | 3 | Verbose output for development |

```bash
export PYTHON_LOG_LEVEL=3
watergun
```

## API Reference

### Search
| Endpoint | Method | Parameter | Description |
| :--- | :--- | :--- | :--- |
| `/search/brave_web_search` | GET | `query` | Executes a Brave web search |

### Fetch
| Endpoint | Method | Parameter | Description |
| :--- | :--- | :--- | :--- |
| `/fetch/fetch_url` | GET | `url`, `page` | Returns the content of a specific URL |

### Obsidian
| Endpoint | Method | Parameter | Description |
| :--- | :--- | :--- | :--- |
| `/obsidian/get_obsidian_doc` | GET | `filename` | Retrieves content from an Obsidian vault |

### System
| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/ping` | GET | Connection health check |
| `/routes` | GET | Lists all active API endpoints |

## Advanced Usage

### Customizing the Server
The server uses FastAPI's lifespan events to manage startup and shutdown sequences. It includes CORS middleware configured to allow all origins, making it suitable for local development with various web-based LLM frontends.

### Log Location
Detailed debug logs are automatically written to the system's state home:
*   Linux: `~/.local/state/headwater_server/logs/server.log`
*   macOS: `~/Library/Application Support/headwater_server/logs/server.log`
