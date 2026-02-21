#!/usr/bin/env python3
"""Placeholder entrypoint for Thunderbird/IMAP ingestion."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    print("Ingestion pipeline stub.")
    print(f"dry_run={args.dry_run}")


if __name__ == "__main__":
    main()
