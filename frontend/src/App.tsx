import React, { useEffect, useState } from "react";
import "./styles.css";

type Location = {
  name: string;
  campus: string;
};

type Locations = {
  [key: string]: Location;
};

type RouteStep = {
  from: string;
  to: string;
  travel_time: number;
  mode: string;
  route: string | null;
};

type RouteResult = {
  route: string[];
  travel_time: number;
  steps: RouteStep[];
};

function App() {
  const [locations, setLocations] = useState<Locations>({});
  const [start, setStart] = useState("");
  const [destination, setDestination] = useState("");
  const [result, setResult] = useState<RouteResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/locations")
      .then((response) => response.json())
      .then((data) => setLocations(data))
      .catch(() => setError("Could not load Rutgers locations."));
  }, []);

  async function findRoute() {
    if (!start || !destination) {
      setError("Please choose both locations.");
      return;
    }

    if (start === destination) {
      setError("Choose two different locations.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/route?start=${encodeURIComponent(
          start
        )}&destination=${encodeURIComponent(destination)}`
      );

      if (!response.ok) {
        throw new Error();
      }

      const data: RouteResult = await response.json();
      setResult(data);
    } catch {
      setError("Route could not be calculated.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="app">
      <nav className="navbar">
        <div className="logo">
          <span className="logo-mark">R</span>
          RouteRU
        </div>

        <span className="nav-label">
          Rutgers Campus Navigator
        </span>
      </nav>

      <section className="hero">
        <div className="hero-copy">
          <span className="eyebrow">
            RUTGERS UNIVERSITY
          </span>

          <h1>
            Find your way
            <br />
            around <span>Rutgers.</span>
          </h1>

          <p>
            Choose where you're starting and where you're headed.
            RouteRU uses shortest-path routing to find a campus route.
          </p>
        </div>

        <div className="route-card">
          <div className="card-heading">
            <span>Plan your route</span>
            <span className="status">
              ● Campus routing
            </span>
          </div>

          <label htmlFor="start">
            Starting location
          </label>

          <select
            id="start"
            value={start}
            onChange={(event) => setStart(event.target.value)}
          >
            <option value="">
              Where are you now?
            </option>

            {Object.entries(locations).map(
              ([id, location]) => (
                <option key={id} value={id}>
                  {location.name} — {location.campus}
                </option>
              )
            )}
          </select>

          <div className="route-line">
            <span></span>
          </div>

          <label htmlFor="destination">
            Destination
          </label>

          <select
            id="destination"
            value={destination}
            onChange={(event) =>
              setDestination(event.target.value)
            }
          >
            <option value="">
              Where are you going?
            </option>

            {Object.entries(locations).map(
              ([id, location]) => (
                <option key={id} value={id}>
                  {location.name} — {location.campus}
                </option>
              )
            )}
          </select>

          <button
            onClick={findRoute}
            disabled={loading}
          >
            {loading
              ? "Finding route..."
              : "Find Route →"}
          </button>

          {error && (
            <p className="error">{error}</p>
          )}

          {result && (
            <div className="result">
              <div className="result-header">
                <div>
                  <small>ROUTE ESTIMATE</small>
                  <strong>
                    {result.travel_time} min
                  </strong>
                </div>

                <div>
                  <small>STEPS</small>
                  <strong>
                    {result.steps.length}
                  </strong>
                </div>
              </div>

              <div className="route-steps">
                {result.steps.map((step, index) => (
                  <div
                    className="step"
                    key={`${step.from}-${step.to}-${index}`}
                  >
                    <span className="step-number">
                      {index + 1}
                    </span>

                    <div>
                      <strong>
                        {step.mode === "Bus"
                          ? `${step.route} Bus`
                          : "Walk"}
                      </strong>

                      <div>
                        {locations[step.from]?.name}
                        {" → "}
                        {locations[step.to]?.name}
                      </div>

                      <small>
                        {step.travel_time} min estimate
                      </small>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      </section>

      <footer>
        Built for Rutgers students · RouteRU
      </footer>
    </main>
  );
}

export default App;