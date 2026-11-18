"""Операции с каталогом. Поведение задаёт docs/specification.md."""
import json
import os
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
        result = str(seconds) + " с"
    else:
        if seconds < 3600:
            if seconds % 60 == 0:
                result = str(seconds // 60) + " мин"
            else:
                result = str(seconds // 60) + " мин " + str(seconds % 60) + " с"
        else:
            if seconds % 3600 == 0:
                result = str(seconds // 3600) + " ч"
            else:
                if seconds % 60 == 0:
                    result = str(seconds // 3600) + " ч " + str((seconds % 3600) // 60) + " мин"
                else:
                    result = str(seconds // 3600) + " ч " + str((seconds % 3600) // 60) + " мин " + str(seconds % 60) + " с"
    return result
