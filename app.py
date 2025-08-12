# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from brain_health import SimpleBrainHealth

app = FastAPI(title="Brain Health Demo API", version="0.1.0")
_analyzer = SimpleBrainHealth()

class AnalyzeIn(BaseModel):
    text: str

class AnalyzeOut(BaseModel):
    animal_count: int
    repetitions: int
    memory_score: int
    brain_health_score: int
    report: str

@app.post("/analyze", response_model=AnalyzeOut)
def analyze(inp: AnalyzeIn):
    res = _analyzer.analyze_speech(inp.text)
    return {
        "animal_count": res["animal_count"],
        "repetitions": res["repetitions"],
        "memory_score": res["memory_score"],
        "brain_health_score": res["brain_health_score"],
        "report": _analyzer.generate_report(res),
    }
