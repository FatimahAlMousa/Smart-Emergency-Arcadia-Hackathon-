# 🚑 Smart Emergency

An AI-assisted health monitoring web app that analyzes vital signs in real time and automatically triggers an ambulance dispatch simulation when an emergency is detected.

## Key Features
- **Live vital sign check** — user enters heartbeat, blood pressure, oxygen level, and temperature
- **Instant analysis** — backend classifies status as Normal, Needs Follow-up, or Emergency
- **Auto ambulance call** — on emergency detection, a 15-second countdown starts automatically (cancellable by the user)
- **Live tracking simulation** — shows an embedded map tracking the "ambulance" after dispatch
- **Responsive UI** — built with Bootstrap for a clean, mobile-friendly experience

## Tech Stack
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Backend:** Python (Flask)
- **Maps:** Google Maps embed

## How It Works
1. User fills in the health form (heartbeat, pressure, oxygen, temperature).
2. Data is sent to the Flask `/analyze` endpoint.
3. Backend applies threshold rules to classify the health status.
4. Result is shown in a modal:
   - ✅ Normal condition
   - ⚠️ Needs medical follow-up
   - 🚨 Emergency — triggers auto ambulance countdown + tracking view

## Run Locally
```bash
pip install flask
python app.py
```
Then open the app in your browser (default: `http://127.0.0.1:5000`).

## Project Status
Built as a hackathon prototype (AI Hackathon). Core flow is functional; not production-ready (no real ambulance dispatch, no data persistence/auth).
