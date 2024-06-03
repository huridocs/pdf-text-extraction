import requests
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from configuration import service_logger
from extract_text import extract_analysis, extract_text

app = FastAPI()


@app.post("/")
async def get_analysis(file: UploadFile = File(...), types: str = Form("all")):
    try:
        service_logger.info(f"Processing file: {file.filename}")
        file_content = file.file.read()
        response = requests.post(
            "http://pdf-document-layout-analysis-text-extraction:5060/",
            files={"file": (file.filename, file_content, file.content_type)}
        )
        return extract_analysis(response.json(), types)
    except requests.RequestException as e:
        raise HTTPException(status_code=422, detail=str(e))


@app.post("/fast")
async def get_analysis_fast(file: UploadFile = File(...), types: str = Form("all")):
    try:
        service_logger.info(f"Processing file: {file.filename}")
        file_content = file.file.read()
        response = requests.post(
            "http://pdf-document-layout-analysis-text-extraction:5060/fast",
            files={"file": (file.filename, file_content, file.content_type)}
        )
        return extract_analysis(response.json(), types)
    except requests.RequestException as e:
        raise HTTPException(status_code=422, detail=str(e))


@app.post("/text")
async def get_text(file: UploadFile = File(...), types: str = Form("all")):
    try:
        service_logger.info(f"Processing file: {file.filename}")
        file_content = file.file.read()
        response = requests.post(
            "http://pdf-document-layout-analysis-text-extraction:5060/",
            files={"file": (file.filename, file_content, file.content_type)}
        )
        return extract_text(response.json(), types)
    except requests.RequestException as e:
        raise HTTPException(status_code=422, detail=str(e))


@app.post("/text_fast")
async def get_text_fast(file: UploadFile = File(...), types: str = Form("all")):
    try:
        service_logger.info(f"Processing file: {file.filename}")
        file_content = file.file.read()
        response = requests.post(
            "http://pdf-document-layout-analysis-text-extraction:5060/fast",
            files={"file": (file.filename, file_content, file.content_type)}
        )
        return extract_text(response.json(), types)
    except requests.RequestException as e:
        raise HTTPException(status_code=422, detail=str(e))
