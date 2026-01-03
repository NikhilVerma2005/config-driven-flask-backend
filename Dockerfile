# Step 1: Base image (Python runtime)
FROM python:3.11-slim

# Step 2: Set working directory inside container
WORKDIR /app

# Step 3: Copy dependencies file first (for caching)
COPY requirements.txt .

# Step 4: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy entire project code
COPY . .

# Step 6: Expose container port
EXPOSE 8000

# Step 7: Start app using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:app"]
