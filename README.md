## WORK-FLOW ENGINE 
A functional workflow orchestration engine built with FastAPI, supporting dynamic graph creation, node registration, looping execution, and run-state retrieval. Includes a Code Review Agent workflow that processes code sequentially and iteratively improves quality for the assignment.

Overview
This project implements a minimal yet powerful backend workflow engine using **FastAPI**.  
It showcases clean architecture, async design, and agent-like iterative state management.

Core capabilities:
- Dynamic workflow graph creation
- Sequential & conditional node execution
- Branching + looping logic
- Shared state mutation throughout the workflow
- Persistent run logs and state retrieval
- Fully working custom sample workflow

## Key Features

 Dynamic Workflow Graphs
Define nodes, edges, and start points at runtime using JSON.

 Node-Based Execution
Each node is an async Python function that:
- Reads shared state  
- Mutates it  
- Optionally redirects flow (`{"next": "node"}`)

Looping Support
Allows iterative improvement cycles and repeated execution until a condition is met.

 Execution Logs
Every step records:
- Node name
- Timestamp
- Updated state
- Status (ok/error)

 FastAPI-Powered API
Automatic documentation available at:  
 **http://127.0.0.1:8000/docs**
 
Sample Workflow: Code Review Agent

This project includes a fully working workflow that:
1. Extracts functions  
2. Checks code complexity  
3. Detects basic issues  
4. Suggests improvements  
5. Repeats steps until the quality score reaches the threshold  

This demonstrates how the engine performs iterative agent behavior.

---

