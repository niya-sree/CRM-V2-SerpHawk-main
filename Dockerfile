FROM python:3.14

WORKDIR /backend

COPY requirements.txt .

#Install Python Dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
