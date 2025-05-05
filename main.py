from fastapi import FastAPI, HTTPException
import random
import os

app = FastAPI()
secret_key = os.getenv("SECRET_KEY", "total secret value")


@app.get("/")
async def hello_world():
    """Endpoint returning a secret key or failure, randomly."""
    if random.random() < 0.5:
        return {"message": f"Hello World with secret: {secret_key}"}
    else:
        raise HTTPException(status_code=400, detail="Random bad request error")


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
