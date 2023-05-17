#!/bin/bash

nginx -g "daemon off;" &
gcloud beta emulators pubsub start --project $PUBSUB_PROJECT_ID --host-port $PUBSUB_EMULATOR_HOST &
python3 ./admin/api/app.py
