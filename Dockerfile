FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy your application files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define the entrypoint
ENTRYPOINT ["python", "master_script.py"]