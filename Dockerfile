# Step 1: Use the official Python image as a base image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the current directory (the app code) into the container
COPY . /app

# Step 4: Install the required dependencies (listed in requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Define the command to run the app
CMD ["python", "app.py"]