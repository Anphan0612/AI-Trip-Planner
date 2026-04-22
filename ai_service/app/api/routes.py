from fastapi import APIRouter, HTTPException
from app.models.schemas import ParseRequest, ParseResponse, TripPlanResponse
from app.pipelines.parse_pipeline import parse_pipeline
from app.pipelines.trip_pipeline import trip_pipeline

router = APIRouter()

@router.post("/parse-query", response_model=ParseResponse)
async def parse_query(request: ParseRequest):
    """
    Parse a natural language travel query into structured data.
    """
    try:
        result = await parse_pipeline.execute(request.text)
        return result
    except Exception as e:
        # In production, log the error properly
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/plan-trip", response_model=TripPlanResponse)
async def plan_trip(request: ParseRequest):
    """
    Parse a query and generate a full trip plan (recommendations and itinerary).
    """
    try:
        result = await trip_pipeline.execute(request.text, request.user_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
