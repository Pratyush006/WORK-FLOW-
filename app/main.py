from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
import uuid

class GraphDefinition(BaseModel):
    name: Optional[str] = None
    nodes: list[str]
    edges: dict
    start_node: str

class GraphRunRequest(BaseModel):
    graph_id: str
    initial_state: Optional[Dict[str, Any]] = {}

app = FastAPI(title="Minimal Workflow Engine (Clean UTF-8)")

_GRAPHS = {}
_RUNS = {}

@app.post("/graph/create")
async def create_graph(defn: GraphDefinition):
    if defn.start_node not in defn.nodes:
        raise HTTPException(status_code=400, detail="start_node must be in nodes list")
    graph_id = str(uuid.uuid4())
    _GRAPHS[graph_id] = defn.dict()
    return {"graph_id": graph_id}

@app.post("/graph/run")
async def run_graph(req: GraphRunRequest):
    if req.graph_id not in _GRAPHS:
        raise HTTPException(status_code=404, detail="graph not found")
    run_id = f"run-{req.graph_id}"
    _RUNS[run_id] = {
        "state": req.initial_state or {},
        "logs": []
    }
    return {"run_id": run_id, "final_state": _RUNS[run_id]["state"], "logs": []}

@app.get("/graph/state/{run_id}")
async def get_state(run_id: str):
    if run_id not in _RUNS:
        raise HTTPException(status_code=404, detail="run_id not found")
    return _RUNS[run_id]
