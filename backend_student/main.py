"""
Track A - Energy Demand Forecasting backend (STUDENT scaffold).

Goal of this session: reload the exported model and serve it through FastAPI,
with Pydantic input validation. The app object, CORS and /health are given.
Fill the three endpoint TODOs.

Run:
    ../.venv/bin/python -m uvicorn main:app --reload --port 8000
    open http://127.0.0.1:8000/docs
"""
from fastapi import FastAPI, UploadFile, File, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from schemas import ModelInfo, ForecastResponse, OptimizeRequest, OptimizeResponse
from services.forecasting import model_info, run_forecast, load_artifact
from services.preprocessing import read_energy_csv
from services.optimization import optimize_mix

app = FastAPI(title="Track A - Energy Demand Forecasting API", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


@app.get("/health")               # GIVEN
def health():
    try:
        info = model_info()
        return {"status": "ok", "model_loaded": True, "model_name": info["model_name"]}
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"Model not available: {exc}")


@app.get("/model-info", response_model=ModelInfo)
def get_model_info():
    # TODO: return model_info() ; wrap errors in HTTPException(503, ...)
    ...


@app.post("/forecast", response_model=ForecastResponse)
async def forecast(
    file: UploadFile = File(...),
    last_hours: int | None = Query(None, ge=1, le=744),
):
    # TODO 1: reject non-.csv files -> HTTPException(400, ...)
    # TODO 2: raw = await file.read() ; energy = read_energy_csv(raw)
    #         (raises ValueError with a clear message on bad input -> 422)
    # TODO 3: return run_forecast(energy, last_hours=last_hours)
    #         (ValueError -> 422 ; anything else -> 500)
    ...


@app.post("/optimize", response_model=OptimizeResponse)
def optimize(req: OptimizeRequest):
    # TODO: call optimize_mix(demand=req.demand, carbon_limit=req.carbon_limit,
    #       renewable_min=req.renewable_min, capacities=req.capacities)
    #       Pydantic already validated req for you.
    ...


@app.on_event("startup")
def _warm():
    load_artifact()
