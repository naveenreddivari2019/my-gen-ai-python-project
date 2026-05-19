# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python project for testing and comparing different LLM APIs: Claude (Anthropic), OpenAI, and Google GenAI (Gemini). The codebase contains example scripts demonstrating how to interact with each provider.

## Environment Setup

This project uses a Python virtual environment. Set it up:

```bash
# Create virtual environment (first time only)
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**API Keys Configuration:**

All API keys are stored in `.env` file (not committed to git):
- `ANTHROPIC_API_KEY` for Claude
- `OPENAI_API_KEY` for OpenAI  
- `GEMINI_API_KEY` for Google GenAI

Create your `.env` file from the template:
```bash
cp .env.example .env
# Then edit .env and add your actual API keys
```

All scripts load environment variables using `python-dotenv`:
```python
from dotenv import load_dotenv
load_dotenv()
```

## Running the Test Scripts

**Always activate the virtual environment first:**

```bash
source venv/bin/activate

# Test Claude API
python src/LLM/Claude-Test.py

# Test OpenAI API
python src/LLM/OpenAI-Test.py

# Test Google GenAI
python src/LLM/GoogleGenAI-Test.py

# Deactivate when done
deactivate
```

**For VS Code:** The project is configured to use the venv Python interpreter automatically (`.vscode/settings.json`). Select the interpreter with `Cmd+Shift+P` → "Python: Select Interpreter" → `./venv/bin/python`.

## Code Architecture

- **src/LLM/**: Contains test scripts for each LLM provider
  - `Claude-Test.py`: Demonstrates Anthropic's Claude API with system prompts
  - `OpenAI-Test.py`: Shows OpenAI chat completions API
  - `GoogleGenAI-Test.py`: Uses Google's GenAI with streaming, thinking config, and tools (Google Search)

Each script is self-contained and demonstrates basic API usage patterns for the respective provider.

## Model Conventions

- Claude: Uses `claude-sonnet-4-6` model
- OpenAI: Uses `gpt-3.5-turbo` model
- Google GenAI: Uses `gemini-2.0-flash` model with high thinking level

When adding new LLM providers, follow the same pattern: create a standalone test script in `src/LLM/` with environment variable loading and basic API interaction.
