# Theatre API Service

## Project Description

The Theatre API Service is a robust API designed to manage theatrical performances, allowing visitors to book seats, view performances, and manage theaters. Developed with Django and Docker, this project provides a comprehensive solution for theatre management.

## Features

- **Manage Theatres**: Add, edit, and delete theatrical venues.
- **Manage Performances**: Add, edit, and delete performances.
- **Seat Booking**: Visitors can reserve seats for performances.
- **Rating and Reviews**: Users can rate performances and leave reviews.
- **Search Filters**: The API includes search filters for finding performances and theaters.
- **JWT Authentication**: Secure API access using JSON Web Tokens (JWT).
- **Swagger Documentation**: API documentation available through Swagger for easy exploration and testing.

## Technologies

- **Django**: The primary web framework used.
- **Django REST Framework**: For creating RESTful APIs.
- **PostgreSQL**: Relational database management system.
- **Docker**: Containerization of the development environment.

## Setup and Running

### Local Environment

1. **Clone the Repository:**

   ```bash
   git clone <repository-URL>
   cd Theatre-Api-Service

2. **Create and Activate a Virtual Environment**
    ```bash
   python -m venv .venv
   source .venv/bin/activate
   # For Windows use:
   .venv\Scripts\activate
   ```
   
3. **Install Dependencies**
    ```bash
   pip install -r requirements.txt
   ```
   
4. **Set Up Environment Variables**

Create a ".env" file based on ".env.template" and populate it with the required variables.

1. **Create & Apply Database Migrations**
    ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Run the Development Server**
    ```bash
   python manage.py runserver
   ```
   
## Docker Environment

The project uses Docker for containerization, which simplifies the setup and ensures consistency across different environments.

### Prerequisites

- **Docker**: Ensure Docker is installed on your system. You can download it from [Docker's official site](https://www.docker.com/get-started).
- **Docker Compose**: This tool is used to define and run multi-container Docker applications. It usually comes with Docker Desktop, but you can also install it separately from [Docker Compose's installation guide](https://docs.docker.com/compose/install/).

1. **Create & Configure Docker Environment**:

Ensure you have the following Docker-related files in the root of your project:

- "Dockerfile": Defines the environment for your Django application.


- "docker-compose.yaml": Configures the services, including the web application and database.

 
**Build Docker Images**

Build the Docker images specified in docker-compose.yaml:

```bash
    docker-compose build
```


**Start Docker Containers**

Start the containers in detached mode, ensuring that all services are up and running:
```bash
    docker-compose up -d
```

The "-d" flag runs the containers in the background.


**Check Running Containers**

Verify that your containers are running properly:
```bash
    docker-compose ps
```

**Apply Database Migrations**

Run database migrations to set up the database schema:
```bash
    docker-compose exec web python manage.py migrate
```

**Run the Development Server**

Access the running application at "http://localhost:8000" (or the port specified in "docker-compose.yaml"):
```bash
    docker-compose exec web python manage.py runserver 0.0.0.0:8000
```
This command starts the Django development server inside the Docker container.

**Run Tests(in Docker Container)**

```bash
    docker-compose exec web python manage.py test theatre.tests
```

## Stopping & Removing Containers

**Stop Docker Containers**
```bash
    docker-compose down
```

**Remove Unused Images and Volumes**

```bash
    docker system prune
```

Be cautious as this command removes unused data and may affect other projects using Docker.



## Troubleshooting
- If Docker Containers Fail to Start:
 
Check the logs for more information:
```bash
    docker-compose logs
```
- If You Encounter Issues with Database:

Ensure the database container is up and running. You can also inspect the container logs:
```bash
    docker-compose logs db
```


## API Documentation

The API documentation is available through Swagger. Access it by navigating to "http://localhost:8000/swagger/" after starting the development server.


## Conclusion

You are now ready to use the TheatreAPIService application.
