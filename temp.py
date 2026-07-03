from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/upload")
async def upload(
    files: list[UploadFile] = File(...)
):
    return {"count": len(files)}