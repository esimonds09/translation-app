from config import DEEPL_API_KEY
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

# CORS settings to allow requests from your Vue.js app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your Vue.js app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/translate")
async def translate_text(request_data: dict):
    # Extract request data
    text = request_data.get("text")
    target_lang = request_data.get("target_lang")

    # Replace with your DeepL API key
    api_key = DEEPL_API_KEY

    # Validate request data
    if not text:
        raise HTTPException(status_code=422, detail="Text is required")
    if not target_lang:
        raise HTTPException(status_code=422, detail="Target language is required")
    # Make a request to DeepL
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api-free.deepl.com/v2/translate",
                data={
                    "auth_key": api_key,
                    "text": text,
                    "target_lang": target_lang,
                },
            )
        
        # Handle the response and return the translation
        translation_data = response.json()
        if "translations" not in translation_data:
            raise HTTPException(status_code=500, detail="Translation failed")
        translation_text = translation_data["translations"][0]["text"]

        # print(translation)
        return translation_text
    
    except httpx.HTTPStatusError as http_error:
        error_response = http_error.response.json()
        error_message = error_response.get("message", "")
        
        # Check if the error message indicates an invalid API key
        if "invalid_auth_key" in error_message.lower():
            raise HTTPException(status_code=400, detail="Invalid API key")
        else:
            raise HTTPException(status_code=500, detail="Translation service error")
