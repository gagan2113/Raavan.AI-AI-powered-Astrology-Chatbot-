"""Root launcher for Raavan AI FastAPI backend."""

import uvicorn


def main():
    """Run the FastAPI app with Uvicorn."""
    uvicorn.run("src.app.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
