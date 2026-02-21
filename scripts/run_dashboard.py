#!/usr/bin/env python3
"""Launch API backend for dashboard integration."""

import sys
from pathlib import Path

import uvicorn

sys.path.append(str(Path(__file__).resolve().parents[1]))


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=False)
