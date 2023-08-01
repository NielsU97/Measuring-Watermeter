# Python Image
FROM arm32v7/python:2.7.13-jessie

# Copy the Python Script to watermeter
ADD watermeter.py .

# Install libraries
RUN pip install --no-cache-dir rpi.gpio

# Run command
CMD ["python", "./watermeter.py"]