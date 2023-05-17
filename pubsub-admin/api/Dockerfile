FROM python:3

WORKDIR /app
COPY app.py app.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=0
ENV PUBSUB_EMULATOR_HOST=localhost:8432
ENV PUBSUB_PROJECT_ID=test-project

ENTRYPOINT [ "python3" ]
CMD [ "-m", "flask", "run" ]

EXPOSE 5000