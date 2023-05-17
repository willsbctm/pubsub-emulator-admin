# pubsub-emulator-admin

## Install:
```sh
docker build -t pubsubadmin .
```

## Run
```sh
docker run -d -p 8000:8000 -p 8085:80 -p 8432:8432 pubsubadmin
```

1. Admin portal will be available in: `http://localhost:8085`
2. Pubsub will be available in: `localhost:8432`
3. The Admin portal api will be available in `http://localhost:8000/api`