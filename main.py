from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import g4f

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class RegexRequest(BaseModel):
    englishInput: str
    exampleText: str
    exampleResultText: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate")
async def generate_regex(request: RegexRequest):
    messages = [
        {"role": "user", "content": "You are an english to regex translator. You will be given instructions in english for what the regex is to do, and an example text to operate upon, and an example text to demonstrate the expected found characters with the regex.\n You will only generate javascript regex code. You will not say any words in english. You will not ask the user for any questions, you will only generate javascript regex code that meets the users requirements. The user will give you their request now. \n USER REQUEST BEGIN: "},
        {"role": "user", "content": f"English Input: {request.englishInput} \n Example Text: {request.exampleText} \n Example Result Text: {request.exampleResultText}"}
    ]
    
    # Use the asynchronous version of the create function
    response = await g4f.ChatCompletion.create_async(
        model=g4f.models.gpt_4,
        messages=messages
    )
    
    return {"regex": response}

