#!/bin/bash



source .venv/Scripts/activate


run_analytical() {
    while true; do
        echo "Running analytical.py..."
        python app/modules/analytical.py
        sleep 1800  
    done
}


run_analytical &


echo "Starting API server on port 9303..."
python -m uvicorn api.api:app --reload --port 9303


wait
