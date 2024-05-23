# Calculator application front-end

## Prerequisites

- [Docker Installation](https://github.com/SarathChandra24/MLOps-calculator-backend-spring/blob/main/DOCKER_BACKGROUND.md#docker-installation), If specific OS is not mentioned, please browse through [Official Docker](https://www.docker.com/get-started) documentation.

## Running the Application stack with Docker compose
We have 2 services, [calculator-backend](https://github.com/SarathChandra24/MLOps-calculator-backend-spring) and [calculator-frontend](./).

## Running the Application

1. Clone this repository:

   ```bash
   git clone https://github.com/SarathChandra24/MLOps-calculator-frontend.git
   ```
2. Navigate to the project directory:
    ```bash
    cd MLOps-calculator-frontend
    ```
3. Build the Docker images and start the containers:
    ```bash
    docker-compose up --build
    ```
    This command will build the Docker images and start the containers defined in the docker-compose.yml file.
4. The Spring Boot application will be accessible at http://localhost:8080.
5. The Python application can communicate with the Spring Boot application using the hostname spring-boot-app.
6. The front-end application will be accessible at http://localhost:45000.
7. To stop the containers, press Ctrl+C in the terminal where the containers are running, or run:
    ```bash
    docker-compose down
    ```

### Customization

```yaml
build:
      context: .
      dockerfile: Dockerfile
```

If you have a specific Dockerfile for your Python application, replace `context` in the `docker-compose.yml` file with the actual path to your Dockerfile.

```Yaml
ports:
    - "8080:8080"
```

```Yaml
ports:
    - "45000:5000"
```

Adjust the port mappings and networking configurations in the docker-compose.yml file based on your specific requirements.

Ensure that the port used by the Spring Boot application is not already in use on your machine.