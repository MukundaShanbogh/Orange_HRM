# Use the official Playwright image for Python (includes all browser dependencies)
FROM mcr.microsoft.com/playwright/python:v1.58.0-jammy

# Set the working directory
WORKDIR /app
# Copy the requirements file and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# (Optional) If you only want Chromium to save space, use: RUN playwright install chromium
# RUN playwright install

# Copy your test framework into the container
COPY . .

# Run the tests
CMD ["pytest"]