FROM python:3.12-slim

WORKDIR /app

# Optional but recommended: upgrade pip
RUN pip install --upgrade pip

# Install dependencies directly (faster & cleaner)
RUN pip install fastapi uvicorn[standard] pandas joblib scikit-learn

# Copy the rest of the project files
COPY . .

# Start command
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
