from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
import json
import os

app = FastAPI()

SECRET_KEY = "ODgyZjNhYjc4MDkzODdiMjI3MzlkZDVhMmYxNTAyMTc="
json_path = os.path.join(os.path.dirname(__file__), '../json/output.json')

@app.get("/secretkey/{secretkey}")
async def read_json(secretkey: str):
    if secretkey != SECRET_KEY:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    try:
        with open(json_path, 'r') as file:
            data = json.load(file)

        return JSONResponse(content=data)

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9303)
