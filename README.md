# pubsub-emulator-admin

## Install:
```sh
docker build -t pubsubadmin .
```

## Run
```sh
docker run -d -p 8000:8000 -p 8085:80 -p 8432:8432 pubsubadmin
```

Admin portal will be available in: `http://localhost:8085`