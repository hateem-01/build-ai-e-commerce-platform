"""
Build AI E-Commerce Platform - Backend Service
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Build AI E-Commerce Platform", version="1.0.0")

class Item(BaseModel):
    id: int
    name: str
    price: float

@app.get("/")
def root():
    return {
        "status": "active",
        "project": "Build AI E-Commerce Platform",
        "requester": "HATEEM TAHIR 2023-BS-AI-032 <2023-bs-ai-032@tuf.edu.pk>",
        "service": "Digital FTE Autonomous Backend"
    }

@app.get("/items")
def list_items():
    return [
        {"id": 1, "name": "AI Subscription Tier 1", "price": 49.99},
        {"id": 2, "name": "Enterprise AI Suite", "price": 299.99}
    ]
