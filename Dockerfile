FROM python:3.10

WORKDIR /app

# Only basic libraries (NO torch)
RUN pip install --no-cache-dir numpy pandas scikit-learn

COPY scripts/ /app/

CMD ["python", "user_script.py"]