# RouteRU

RouteRU is a Rutgers–New Brunswick campus route planner built with React, TypeScript, FastAPI, and Python. It models the campus transportation network as a weighted graph and uses Dijkstra's shortest-path algorithm to calculate routes between Rutgers locations.

## Features

- Select a starting location and destination
- Calculate shortest routes across Rutgers–New Brunswick campuses
- Support for Livingston, Busch, College Avenue, and Cook/Douglass
- Display walking and Rutgers bus route segments
- Show route steps and estimated routing time
- React frontend connected to a FastAPI backend
- Graph-based routing using Dijkstra's algorithm
- GTFS transit-data integration in development

## Tech Stack

### Frontend

- React
- TypeScript
- Vite
- CSS

### Backend

- Python
- FastAPI
- Uvicorn

### Algorithms

- Weighted graphs
- Priority queues
- Dijkstra's shortest-path algorithm

## How It Works

RouteRU represents Rutgers locations as nodes in a graph and connections between locations as weighted edges.

When a user chooses a starting location and destination:

1. The React frontend sends the locations to the FastAPI backend.
2. The backend runs Dijkstra's algorithm on the campus graph.
3. The algorithm finds the lowest-cost route between the two locations.
4. FastAPI returns the route information to the frontend.
5. The frontend displays the route as a sequence of walking and bus steps.

## Project Structure

```text
routeru/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes.py
│   │   ├── core/
│   │   │   └── graph.py
│   │   ├── data/
│   │   │   └── locations.py
│   │   ├── services/
│   │   │   ├── routing.py
│   │   │   └── gtfs_service.py
│   │   └── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── styles.css
│   └── package.json
│
└── README.md
```

## Running RouteRU Locally

### Backend

From the project root:

```bash
source .venv/bin/activate
cd backend
python3 -m uvicorn app.main:app --reload
```

The API runs at:

```text
http://127.0.0.1:8000
```

FastAPI documentation is available at:

```text
http://127.0.0.1:8000/docs
```

### Frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Then open:

```text
http://localhost:5173
```

## Transit Data

The current version contains a graph-based Rutgers campus transportation model.

Integration with GTFS transit data is currently being developed so RouteRU can load Rutgers stop, route, and schedule information from transit data rather than relying entirely on manually maintained route information.

Routing estimates currently represent graph weights and should not be interpreted as live Rutgers bus arrival times.

## Next Steps

- Integrate Rutgers/TripShot GTFS stop and route data
- Build the routing graph from GTFS data
- Explore GTFS-Realtime support
- Improve route instructions
- Group locations by campus
- Add automated backend tests
- Improve responsive UI
- Deploy the frontend and backend

## Disclaimer

RouteRU is an independent student project and is not an official Rutgers University application. Transit information and routing estimates should not be treated as official or real-time Rutgers transportation information.

## Author

**Soraya Mosavi**

Rutgers University — Computer Science
