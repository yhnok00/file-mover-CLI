# File Mover Utility

> My first real-world Python project: a command-line tool to quickly move files matching a specific pattern between folders.

## What it does
This script allows you to take files matching a specific pattern (like `*.py`, `*.txt`, or `*`) from a source directory and move them directly into a destination directory. If the destination directory doesn't exist, it creates it automatically.

It was built as an everyday automation tool to make organizing files faster via the terminal.

## Requirements
* Python 3.x

## How to Use

Run the script from your terminal using the following syntax:

```bash
python script.py <source_folder> <destination_folder> [pattern]
