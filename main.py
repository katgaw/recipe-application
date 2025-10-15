from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from openai import OpenAI
import os

app = FastAPI(title="Thanksgiving Recipe Generator")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate-recipe", response_class=HTMLResponse)
async def generate_recipe(
    request: Request,
    api_key: str = Form(...),
    diet_type: str = Form(...)
):
    try:
        # Initialize OpenAI client
        client = OpenAI(api_key=api_key)
        
        # Create diet-specific prompt
        diet_prompts = {
            "vegetarian": "vegetarian (no meat, but dairy and eggs are okay)",
            "vegan": "vegan (no animal products including dairy, eggs, or honey)",
            "no_restrictions": "traditional (no dietary restrictions)"
        }
        
        diet_description = diet_prompts.get(diet_type, "traditional")
        
        prompt = f"""Generate a simple but delicious Thanksgiving dinner recipe that is {diet_description}. 
        Include:
        1. A main dish
        2. 2-3 side dishes
        3. Simple ingredients that are easy to find
        4. Basic cooking instructions
        5. Estimated cooking time
        
        Format it nicely for a home cook. Keep it practical and not too complex."""
        
        # Generate recipe using GPT-4
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful cooking assistant specializing in Thanksgiving recipes. Provide clear, practical cooking advice."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        
        recipe = response.choices[0].message.content
        
        return templates.TemplateResponse("recipe.html", {
            "request": request,
            "recipe": recipe,
            "diet_type": diet_type
        })
        
    except Exception as e:
        error_message = f"Error generating recipe: {str(e)}"
        return templates.TemplateResponse("error.html", {
            "request": request,
            "error": error_message
        })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
