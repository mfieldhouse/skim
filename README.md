# Skim - Construction Material Price Finder

A minimalist Flask application that helps users find the best prices for plasterboards and plaster bags in their area.

## Features
- Modern, responsive UI built with Tailwind CSS
- Real-time price comparison using OpenAI's GPT
- Google Maps integration for store locations
- Minimal dependencies for better performance

## Setup

1. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## Requirements
- Python 3.8+
- OpenAI API key
- Internet connection for Tailwind CSS CDN
