FROM python:3.13

WORKDIR /music_library

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src

ENTRYPOINT ["python", "-m", "src.musiclibrary.main"]

EXPOSE 5000
