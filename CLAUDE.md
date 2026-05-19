# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python project for testing and comparing different LLM APIs: Claude (Anthropic), OpenAI, and Google GenAI (Gemini). The codebase contains example scripts demonstrating how to interact with each provider.

## Environment Setup

All API keys are stored in `.env` file (not committed to git):
- `ANTHROPIC_API_KEY` for Claude
- `OPENAI_API_KEY` for OpenAI  
- `GEMINI_API_KEY` for Google GenAI

Always load environment variables using `python-dotenv`:
```python
from dotenv import load_dotenv
load_dotenv()
```

## Dependencies

Install all dependencies:
```bash
pip install -r requirements.txt
```

For Google GenAI specifically:
```bash
pip install google-genai
```

## Running the Test Scripts

Execute individual LLM test scripts:
```bash
# Test Claude API
python src/LLM/Claude-Test.py

# Test OpenAI API
python src/LLM/OpenAI-Test.py

# Test Google GenAI
python src/LLM/GoogleGenAI-Test.py
```

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
