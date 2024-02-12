from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import g4f

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate")
async def generate_regex(englishInput: str = Form(...), exampleText: str = Form(...), exampleResultText: str = Form(...)):
    messages = [
        {"role": "user", "content": "You are an english to regex translator. You will be given instructions in english for what the regex is to do, and an example text to operate upon, and an example text to demonstrate the expected found characters with the regex.\n You will only generate javascript regex code. You will not say any words in english. You will not ask the user for any questions, you will only generate javascript regex code that meets the users requirements. The user will give you their request now. \n USER REQUEST BEGIN: "},
        {"role": "user", "content": f"English Input: {englishInput} \n Example Text: {exampleText} \n Example Result Text: {exampleResultText}"}
    ]
    
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=messages
    )
    
    return {"regex": response}

