import uvicorn
from fastapi import FastAPI, Body
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

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

