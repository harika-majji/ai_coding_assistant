# AI Coding Assistant

An AI-powered coding agent that can read, write, and run code in a project — all from a single prompt.

## What It Does

You give the agent a task in plain English (e.g. "fix the bug in the calculator" or "run the tests and tell me what's failing"), and it figures out what to do by:

1. Looking at the files in the project
2. Reading the relevant code
3. Writing or fixing code if needed
4. Running the code to verify it works

It keeps doing this in a loop (up to 20 steps) until it has a final answer for you.

## How It Works

The agent is powered by **Google Gemini 2.5 Flash**. It has access to 4 tools:

| Tool | What it does |
|------|-------------|
| `get_files_info` | Lists files and folders in the project |
| `get_file_content` | Reads the contents of a file |
| `write_file` | Creates or updates a file |
| `run_python_file` | Runs a Python file and returns the output |

All file access is sandboxed — the agent can only read and write inside the target project folder, not anywhere else on your computer.

## Project Structure

```
ai_coding_assistant/
├── main.py              # Entry point — sets up the agent and runs the loop
├── call_function.py     # Routes tool calls to the right function
├── config.py            # Config (e.g. max file read size)
├── functions/
│   ├── get_files_info.py    # Tool: list files
│   ├── get_file_content.py  # Tool: read a file
│   ├── write_file.py        # Tool: write a file
│   └── run_python_file.py   # Tool: run a Python file
└── calculator/          # Test project used to demo the agent
    ├── main.py          # Calculator CLI app
    ├── tests.py         # Tests for the calculator
    └── pkg/
        ├── calculator.py    # Core calculator logic
        └── render.py        # Output formatting
```

## The Calculator (Test Project)

The `calculator/` folder is a simple command-line calculator used to test the agent. It evaluates math expressions like `3 + 5` or `10 / 2` and prints the result as JSON.

```
python main.py "3 + 5"
```

The agent is pointed at this folder by default and uses it to demonstrate its ability to explore, understand, fix, and run a real project.

## Setup

1. Clone the repo and install dependencies:
   ```bash
   pip install google-genai python-dotenv
   ```

2. Create a `.env` file with your Gemini API key:
   ```
   GEMINI_API_KEY=your_key_here
   ```

3. Run the agent with a prompt:
   ```bash
   python main.py "How does the calculator work?"
   python main.py "Run the tests and fix any failures"
   ```

## Requirements

- Python 3.10+
- A Google Gemini API key (from Google AI Studio)
