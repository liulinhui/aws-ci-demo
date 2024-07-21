FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install fastapi uvicorn
EXPOSE 8080
CMD ["python3", "aws_ci_demo/__init__.py"]
