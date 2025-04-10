FROM public.ecr.aws/docker/library/python:3.9-slim
#FROM public.ecr.aws/docker/library/python:3.9-slim-bullseye
# FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 3000

CMD ["python", "app.py"]
