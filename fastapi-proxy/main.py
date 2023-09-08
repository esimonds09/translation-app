from config import DEEPL_API_KEY
from fastapi import FastAPI
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

    # Make a request to DeepL or your preferred translation service
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
        translation_text = translation_data["translations"][0]["text"]
        # print(translation)
        return translation_text
    except httpx.HTTPError as http_error:
        # Handle HTTP errors (e.g., 404, 500)
        return {"error": "HTTP error occurred"}
    except (httpx.RequestError, KeyError) as other_error:
        # Handle other types of errors (e.g., network issues, JSON parsing)
        return {"error": "An error occurred during translation"}
