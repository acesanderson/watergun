import watergun.server.logging_config

# To comfort my IDE
_ = watergun.server.logging_config


def main():
    from watergun.server.logo import print_logo
    from pathlib import Path
    import uvicorn

    print_logo()

    uvicorn.run(
        "watergun.server.openwebui:app",
        host="0.0.0.0",
        port=8081,
        reload=True,
        reload_dirs=[str(Path(__file__).parent.parent.parent)],
        log_config=None,
        log_level="info",
    )


if __name__ == "__main__":
    main()
