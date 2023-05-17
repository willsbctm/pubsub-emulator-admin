FROM google/cloud-sdk:emulators as gcloud

WORKDIR /app

RUN apt update
RUN apt install -y python3-pip
ENV PUBSUB_EMULATOR_HOST=0.0.0.0:8432
ENV PUBSUB_PROJECT_ID=test-project

COPY admin/api/requirements.txt admin/api/requirements.txt
RUN pip3 install -r ./admin/api/requirements.txt

COPY admin/api/app.py admin/api/app.py

FROM node as build-frontend
WORKDIR /app
COPY admin/frontend/package*.json ./
RUN npm install
COPY admin/frontend .
RUN npm run build


FROM gcloud
RUN apt install -y nginx
COPY nginx.conf /etc/nginx/conf.d/
COPY --from=build-frontend /app/dist /usr/share/nginx/html
RUN /etc/init.d/nginx restart

COPY init.sh init.sh
RUN chmod +x init.sh

ENTRYPOINT [ "./init.sh" ]

EXPOSE 8000
EXPOSE 8432
EXPOSE 80