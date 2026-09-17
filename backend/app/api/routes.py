from fastapi import APIRouter, HTTPException

from app.data.locations import locations
from app.services.routing import build_campus_graph, find_shortest_route

router = APIRouter()
campus_graph = build_campus_graph()


@router.get("/locations")
def get_locations():
    return locations


@router.get("/route")
def get_route(start: str, destination: str):
    if start not in locations:
        raise HTTPException(status_code=404, detail="Start location not found")

    if destination not in locations:
        raise HTTPException(status_code=404, detail="Destination not found")

    result = find_shortest_route(campus_graph, start, destination)

    if result is None:
        raise HTTPException(status_code=404, detail="No route found")

    return result