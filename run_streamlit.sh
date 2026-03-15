#!/bin/bash
source .venv/bin/activate
export APP_ENV=remote
pip install -r requirements.txt
streamlit run app/main.py