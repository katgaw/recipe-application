# 🦃 Thanksgiving Recipe Generator

A beautiful FastAPI application that generates personalized Thanksgiving recipes using GPT-4 based on your dietary preferences.

## Features

- 🍖 **No Restrictions**: Traditional Thanksgiving recipes
- 🥗 **Vegetarian**: Meat-free recipes with dairy and eggs
- 🌱 **Vegan**: Plant-based recipes with no animal products
- ✨ **Beautiful UI**: Modern, responsive design
- 🔒 **Secure**: API keys are not stored, only used for requests

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

3. Open your browser and go to: `http://localhost:8000`

## Usage

1. Enter your OpenAI API key
2. Select your dietary preference (No Restrictions, Vegetarian, or Vegan)
3. Click "Generate My Thanksgiving Recipe"
4. Get a personalized Thanksgiving menu with main dish and sides!

## Requirements

- Python 3.13
- OpenAI API key
- Internet connection

## Dependencies

- FastAPI 0.104.1
- Uvicorn 0.24.0
- OpenAI 1.51.0
- HTTPX 0.27.0
- Jinja2 3.1.2

## API Endpoints

- `GET /` - Home page with recipe form
- `POST /generate-recipe` - Generate recipe based on dietary preferences

Enjoy your personalized Thanksgiving dinner! 🦃
