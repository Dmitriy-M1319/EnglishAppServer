from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse
from easygoogletranslate import EasyGoogleTranslate

app = FastAPI()

@app.post("/api/translate")
def translate(data = Body()):
    translator = EasyGoogleTranslate(
        source_language=data['from'],
        target_language=data['to'],
        timeout=10
    )
    result = translator.translate(data['word'])
    return JSONResponse(content={"word": result})

