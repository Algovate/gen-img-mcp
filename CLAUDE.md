---
noteId: "a96c3750930011f0b2b16fece0176dd3"
tags: []

---

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
This is a Python-based image generation application using Gradio for the UI and DashScope (Alibaba Cloud) for image synthesis. The application allows users to generate images from text prompts using the Wan models from DashScope.

## Key Files and Structure
- `gradio_app.py`: Main application file with Gradio UI interface
- `demo/`: Contains example scripts for different model providers
- `requirements.txt`: Python dependencies
- `.env.example`: Environment variable template
- `.gitignore`: Standard Python gitignore with additional Gradio-specific entries

## Development Commands

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Application
```bash
python gradio_app.py
```

### Run Demo Scripts
```bash
# For DashScope
python demo/dashscope-demo.py
```

## Environment Setup
1. Copy `.env.example` to `.env`
2. Set your DashScope API key: `DASHSCOPE_API_KEY=your_api_key_here`
3. Get API keys from [Alibaba Cloud DashScope Console](https://dashscope.console.aliyun.com/)

## Architecture Notes
- Uses DashScope ImageSynthesis API for image generation
- Implements a Gradio UI with text input and image output
- Follows standard Python project structure with environment management
- Models are configurable through the UI dropdown
- Error handling for API failures and missing environment variables

## Key Dependencies
- gradio[mcp]>=5.45.0: For the web interface
- dashscope>=1.24.5: For image generation API
- python-dotenv>=1.0.0: For environment variable management
- Pillow>=9.0.0: For image processing
- requests>=2.28.0: For downloading generated images