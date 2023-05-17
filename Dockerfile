FROM google/cloud-sdk:emulators

WORKDIR /app

RUN apt update
RUN apt install -y python3-pip
ENV PUBSUB_EMULATOR_HOST=localhost:8432
ENV PUBSUB_PROJECT_ID=test-project

COPY admin/api/requirements.txt admin/api/requirements.txt
RUN pip3 install -r ./admin/api/requirements.txt

COPY admin/api/app.py admin/api/app.py

COPY init.sh init.sh
RUN chmod +x init.sh

ENTRYPOINT [ "./init.sh" ]

EXPOSE 8000
