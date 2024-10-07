# Navigator for the Habitable Worlds Observatory (HWO)

![alt text](img/EXOATLAS-2.png)


## Table of Contents
- [Overview](#overview)
- [Folder Structure](#folder-structure)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Modules](#modules)
- [Requirements](#requirements)

## Overview
Developed for the **Navigator for the Habitable Worlds Observatory (HWO) challenge**, this project simulates the TRAPPIST-1 solar system. It provides habitability percentages for each planet using data served through an API that processes JSON files containing a comprehensive dataset of factors influencing habitability. The backend operations, including the habitability calculations, are powered by FastAPI and Python modules, while the frontend utilizes Three.js to render 3D visualizations of the solar system and planets.


## Folder Structure
```
├── api
│   └── api.py
├── app
│   ├── modules
│   │   └── analytical.py
│   └── run.sh
├── data
│   ├── earth.md
│   └── factors.md
├── datasets
│   ├── Checlair_2021_AJ_161_150.pdf
│   ├── PSCompPars_2024.10.04_09.06.22.csv
│   └── trappist.json
├── web
│   ├── assets
│   ├── game.js
│   └── index.html
├── LICENSE
├── README.md
└── requirements.txt
```

## Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone https://github.com/qays3/Navigator-Nasa-space
   cd Navigator-Nasa-space
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
1. **Run the Analytical Module**
   ```bash
   python app/modules/analytical.py
   ```
   This script analyzes the TRAPPIST-1 planets and updates the `json/output.json` file with habitability scores.

2. **Start the API Server**
   ```bash
   python -m uvicorn api.api:app --reload --port 9304
   ```
   The API serves the habitability data and requires a secret key for access.

## API Documentation
- **Endpoint**: `/secretkey/{secretkey}`
- **Method**: GET
- **Description**: Retrieves habitability scores for TRAPPIST-1 planets.
- **Response**: JSON data containing habitability percentages.
- **Example Request**:
  ```bash
  curl http://localhost:9304/secretkey/ODgyZjNhYjc4MDkzODdiMjI3MzlkZDVhMmYxNTAyMTc=
  ```

## Modules
### Analytical Module
Located at `app/modules/analytical.py`, this script calculates habitability scores based on Earth-like parameters and updates the `json/output.json` file with the results.

### API Module
Located at `api/api.py`, the API serves the JSON data containing habitability scores. It requires a secret key for access and redirects unauthorized requests.

## Contributors

<div style="display: flex; align-items: center; margin-bottom: 20px;">
    <a href="https://github.com/qays3" style="text-decoration: none; display: flex; align-items: center;">
        <img src="https://github.com/qays3.png" alt="@qays3" title="@qays3" width="100px" height="100px" style="border-radius: 50%; margin-right: 10px;">
    </a>
    <a href="https://github.com/Mstr0A" style="text-decoration: none; display: flex; align-items: center;">
        <img src="https://github.com/Mstr0A.png" alt="@Mstr0A" title="@Mstr0A" width="100px" height="100px" style="border-radius: 50%; margin-right: 10px;">
    </a>
</div>

## Credits
[qays3](https://github.com/qays3) ([Support qays](https://buymeacoffee.com/hidden))

&

[Mstr0A](https://github.com/Mstr0A) ([Support Mstr0A](https://buymeacoffee.com/mstr0a))
