# Use the official Python base image
FROM python:latest

# Set the working directory to /app
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the application code into the container
COPY  . /app

# Expose the port your application will run on (replace 8080 with your port number)
EXPOSE 8080

# Define environment variable (if needed)
#ENV NAME World

# Run your application
CMD python, semantic_sm.py
#Replace your_app.py with the name of your Python script.
