# FastAPI Sync vs. Async Comparison

This project demonstrates the performance difference between synchronous and asynchronous endpoints in a FastAPI application.

## Project Structure

- `main.py`: A simple FastAPI application with two endpoints:
    - `/sync-endpoint`: A synchronous endpoint that simulates a blocking I/O operation using `time.sleep(1)`.
    - `/async-endpoint`: An asynchronous endpoint that uses `asyncio.sleep(1)` to non-blocking I/O.
- `test_load.py`: A load testing script that sends 50 concurrent requests to both endpoints and measures the total time taken.
- `requirements.txt`: The required Python packages for this project.

## How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```

3. **Run the load test:**
   ```bash
   python test_load.py
   ```

## Expected Results

When you run the load test, you will see that the asynchronous endpoint (`/async-endpoint`) is significantly faster than the synchronous endpoint (`/sync-endpoint`). This is because the asynchronous endpoint can handle multiple requests concurrently, while the synchronous endpoint can only handle one request at a time.

## Dependencies

You can also freeze the current project's dependencies to a `requirements.txt` file using the following command:

```bash
pip freeze > requirements.txt
```

The `requirements.txt` file for this project contains:
```
annotated-doc==0.0.4
annotated-types==0.7.0
anyio==4.13.0
certifi==2026.2.25
click==8.3.2
fastapi==0.135.3
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
idna==3.11
pydantic==2.12.5
pydantic_core==2.41.5
starlette==1.0.0
typing-inspection==0.4.2
typing_extensions==4.15.0
uvicorn==0.44.0
```
