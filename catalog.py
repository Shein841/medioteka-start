"""Операции с каталогом. Поведение задаёт docs/specification.md."""
import json
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "catalog.json"

def load_catalog():
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))

def search_items(items, query):
    if not query:
        return items
    clean_query = query.strip().lower()
    return [x for x in items if clean_query in x["title"].lower()]

def filter_by_category(items, category):
    if not category:
        return items
    return [x for x in items if x["category"] == category]

def total_duration(items):
    total = 0
    for item in items:
        total = total + item["duration"]
    return total

def validate_item(item):
    errors = []
    
    # Проверка названия (не пустое и не из одних пробелов)
    title = item.get("title")
    if not title or not str(title).strip():
        errors.append("Название обязательно")
    
    # Проверка длительности (должна быть больше нуля)
    duration = item.get("duration")
    if duration is not None and duration <= 0:
        errors.append("Длительность должна быть больше нуля")
        
    return errors

def duration_label(seconds):
    if seconds < 60:
        return f"{seconds} с"
    minutes = seconds // 60
    if minutes < 60:
        return f"{minutes} мин {seconds % 60} с" if seconds % 60 else f"{minutes} мин"
    hours = minutes // 60
    minutes = minutes % 60
    parts = [f"{hours} ч"]
    if minutes or seconds % 60:
        parts.append(f"{minutes} мин" if minutes else "0 мин")
    if seconds % 60:
        parts.append(f"{seconds % 60} с")
    return " ".join(parts)
