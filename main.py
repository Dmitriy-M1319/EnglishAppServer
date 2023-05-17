import uvicorn
from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from easygoogletranslate import EasyGoogleTranslate

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/translate")
def translate(data = Body()):
    translator = EasyGoogleTranslate(
        source_language=data['from'],
        target_language=data['to'],
        timeout=10
    )
    result = translator.translate(data['word'])
    return JSONResponse(content={"word": result})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)

