from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI(title="Свадебное приглашение")
# Загружаем HTML как строку (Vercel не поддерживает Jinja2 из коробки)
html_path = Path(__file__).parent / "templates" / "index.html"
html_content = html_path.read_text(encoding="utf-8")

# Настройка путей
BASE_DIR = Path(__file__).parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# Данные для приглашения
wedding_data = {
    "bride": "Сергей",
    "groom": "Анастасия",
    "date": "13 сентября 2025 года",
    "time": "17:00",
    "location": "Дворец браколсочетания №2",
    "address": "г. Санкт-Петербург, ул. Фурштатская, 52",
    "message": "Дорогие друзья и родные! Приглашаем вас разделить с нами радость нашего свадебного торжества!"
}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, **wedding_data}
    )