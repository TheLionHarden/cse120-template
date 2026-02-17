from fastapi import FastAPI

app = FastAPI(title="Average Workshop API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
