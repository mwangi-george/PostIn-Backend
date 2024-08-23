# base image
FROM python:3.12-alpine

# create a working directory
RUN mkdir -p /postin_backend

# Set working directory

WORKDIR postin_backend

# Copy all files into the set working directory
COPY ./ ./

# install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create a volume to persist data
VOLUME ["/app/data"]

# make database migrations
RUN alembic upgrade head

# App start command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]