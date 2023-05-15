#!/bin/bash

gcloud beta emulators pubsub start --project $PUBSUB_PROJECT_ID --host-port $PUBSUB_EMULATOR_HOST &
sleep infinity
