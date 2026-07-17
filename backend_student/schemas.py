"""
Pydantic models: the typed contract of the API (STUDENT scaffold).

FastAPI uses these to validate inputs and auto-document every endpoint at /docs.
`ModelInfo` is given as a worked example. Fill the others.
"""
from typing import Optional
from pydantic import BaseModel, Field


# ------------------------------------------------------------------ /model-info  (GIVEN example)
class ModelInfo(BaseModel):
    model_name: str
    target: str
    horizon: str
    n_features: int
    features: list[str]
    test_metrics: dict
    weather_assumption: str


# ------------------------------------------------------------------ /forecast
class Metric(BaseModel):
    mae: Optional[float] = None
    rmse: Optional[float] = None
    mape: Optional[float] = None
    n: int = 0


class ForecastResponse(BaseModel):
    # TODO: declare the response fields returned by run_forecast(). Hints:
    #   model_name: str
    #   horizon: str
    #   n_hours: int
    #   warmup_hours_dropped: int
    #   timestamps: list[str]
    #   predictions: list[float]
    #   actual / reference / naive_yesterday: list[Optional[float]]
    #   peak_demand: float ; average_demand: float
    #   metrics: dict[str, Metric]  (use Field(default_factory=dict))
    ...


# ------------------------------------------------------------------ /optimize
class OptimizeRequest(BaseModel):
    """Energy-mix optimization request. Demand in MW."""
    # TODO: this is the main Pydantic validation exercise. Declare:
    #   demand: float, must be > 0            -> Field(..., gt=0)
    #   carbon_limit: Optional[float] > 0     -> Field(None, gt=0)
    #   renewable_min: Optional[float] in [0, 1] -> Field(None, ge=0, le=1)
    #   capacities: Optional[dict[str, float]]
    ...


class Allocation(BaseModel):
    source: str
    generation_mwh: float
    cost: float
    emissions: float
    selected: bool


class OptimizeResponse(BaseModel):
    feasible: bool
    message: str
    demand: Optional[float] = None
    allocation: list[Allocation] = Field(default_factory=list)
    total_cost: Optional[float] = None
    total_emissions: Optional[float] = None
    renewable_share: Optional[float] = None
