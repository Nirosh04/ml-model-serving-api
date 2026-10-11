# ML Model Serving API

FastAPI-based machine learning inference service with Docker, automated
testing, and continuous integration.

## Overview

This repository demonstrates the engineering side of deploying a machine
learning model as a reliable backend service.

The project focuses on:

-   REST API development with FastAPI
-   Integration of a trained Scikit-Learn pipeline
-   Model loading and inference handling
-   Input validation and structured API responses
-   Docker containerisation
-   Automated API testing
-   Continuous integration with GitHub Actions

The main focus of this project is not model training itself, but the
software engineering required to make a trained model accessible through
a reproducible and testable service.

## Architecture

Client -\> FastAPI REST API -\> Request Validation -\> Model Loading
Layer -\> Scikit-Learn Pipeline -\> Prediction Response

## Main Components

### FastAPI Backend

Provides REST endpoints for: - Health checks - Prediction requests -
Input validation - Structured JSON responses

Main entry point:

`src/app/main.py`

### Machine Learning Model Integration

The project integrates a trained Scikit-Learn pipeline:

`src/app/model/housing_pipeline.pkl`

The pipeline contains: - Feature preprocessing - Feature
transformations - Trained prediction model

## Docker Containerisation

Docker packages: - Python dependencies - FastAPI application - ML model
artifact - Runtime configuration

## Project Structure

    .
    ├── src/
    │   └── app/
    │       ├── main.py
    │       └── model/
    │           └── housing_pipeline.pkl
    ├── tests/
    │   └── test_api.py
    ├── docker/
    │   └── Dockerfile
    ├── .github/
    │   └── workflows/
    │       └── ci.yml
    ├── requirements.txt
    └── README.md

## Technical Implementation

### API Layer

Handles: - HTTP endpoints - Request validation - Model inference -
Structured responses

Endpoints:

    GET /health
    POST /predict

### Automated Testing

Pytest tests verify: - API availability - Response formats - Request
handling - Error behaviour

### Continuous Integration

GitHub Actions: - Installs dependencies - Runs tests - Validates changes

## Engineering Decisions

### Separation of Model Development and Serving

Model development focuses on training and experimentation.

This repository focuses on: - Backend engineering - API design -
Deployment - Testing - Reproducibility

### Container-based Deployment

Docker provides: - Dependency isolation - Reproducible environments -
Consistent execution

## Project Background

The underlying machine learning model was developed during machine
learning practice and experimentation.

This repository focuses on: - Backend service development - ML inference
integration - Containerisation - API testing - Automated validation

Related project:

ML Learning Journey: https://github.com/Nirosh04/ml-learning-journey

## Running Locally

Requirements: - Python \>= 3.10 - pip - Optional Docker

Install:

``` bash
git clone https://github.com/Nirosh04/ml-model-serving-api.git
cd ml-model-serving-api
pip install -r requirements.txt
```

Run:

``` bash
uvicorn src.app.main:app --reload
```

## Running with Docker

Build:

``` bash
docker build -f docker/Dockerfile -t ml-model-serving-api .
```

Run:

``` bash
docker run -p 8000:8000 ml-model-serving-api
```

## Testing

``` bash
pytest
```

## Technologies

-   Python
-   FastAPI
-   REST APIs
-   Scikit-Learn
-   Pandas
-   Docker
-   Pytest
-   GitHub Actions
-   CI/CD

## Limitations

Educational ML serving application.

Current limitations: - Single application instance - Local process
metrics only - No distributed deployment infrastructure - No external
monitoring system

## Future Improvements

-   Persistent metrics storage
-   Monitoring integration
-   Authentication
-   Cloud deployment
-   Horizontal scaling

## Author

Nirosh

Software Engineering student interested in: - Backend systems - Data
infrastructure - Distributed systems - Performance engineering - AI/ML
infrastructure