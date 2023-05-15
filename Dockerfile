FROM google/cloud-sdk:emulators

RUN chmod +x init.sh

ENV PUBSUB_EMULATOR_HOST=[::1]:8432
ENV PUBSUB_PROJECT_ID=test-project

ENTRYPOINT ["./init.sh"]