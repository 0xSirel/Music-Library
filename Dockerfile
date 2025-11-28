FROM python:3.13

WORKDIR /music_library

COPY . .

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 5000

CMD ["python", "main.py"]
