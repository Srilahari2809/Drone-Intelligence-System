# 1. Use an official Python runtime as a parent image
FROM python:3.13-slim

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy the requirements file into the container
COPY requirements.txt .

# 4. Install any needed packages specified in requirements.txt
# --no-cache-dir helps keep the image size small
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your application code into the container
COPY . .

# 6. Make port 8000 available to the world outside this container
# This matches your FastAPI backend port [cite: 337]
EXPOSE 8000

# 7. Run uvicorn when the container launches
# Assuming your FastAPI instance 'app' is in api/main.py
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]