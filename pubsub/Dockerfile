FROM google/cloud-sdk:emulators

WORKDIR /home
COPY init.sh init.sh
RUN chmod +x init.sh

ENV PUBSUB_EMULATOR_HOST=localhost:8432
ENV PUBSUB_PROJECT_ID=test-project

ENTRYPOINT ["./init.sh"]

EXPOSE 8432