# Use a base image with Python
FROM python:3.11-bookworm

# Install Tesseract and language packs
RUN apt-get update && apt-get install -y \
    ffmpeg libsm6 libxext6 \
    tesseract-ocr \
    tesseract-ocr-eng \
    # Add other language packs as needed, e.g., tesseract-ocr-fra for French
    && rm -rf /var/lib/apt/lists/*

# Install pytesseract
RUN pip install opencv-python pytesseract Pillow

# Set the working directory (optional)
WORKDIR /app

# Copy your Python application code into the image (if applicable)
COPY . /app

# Define the default command to run when the container starts (optional)
CMD ["python", "ocr-python.py"]