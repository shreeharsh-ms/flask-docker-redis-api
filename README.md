# flask-docker-redis-api
This project is a simple Flask REST API that counts visits using Redis. Containerized with Docker, it offers an easy-to-deploy, scalable example of combining Flask, Redis, and Docker for lightweight web services.


This project focuses on containerizing a simple Flask application that uses Redis to store a visit counter. The core emphasis is on writing an efficient Dockerfile and orchestrating multiple containers using Docker Compose.


Dockerfile Implementation
The Dockerfile is designed to set up a lightweight Python environment, install necessary dependencies, and prepare the Flask app to run within a container. Key implementation details include:
	•	Utilizing an official slim Python base image to minimize container size.
	•	Defining a working directory inside the container for organized file management.
	•	Copying the dependency file (`requirements.txt`) and installing required Python packages using pip.
	•	Adding the application code into the container image.
	•	Exposing the appropriate port to make the Flask app accessible externally.
	•	Specifying the container’s startup command to run the Flask application correctly.
This approach ensures optimized layering in Docker, improving build speed and efficient use of image caching.
Docker Compose Implementation
To manage both the Flask app and its Redis dependency, a Docker Compose configuration was created. This enables orchestration of multiple containers with ease. Key components of the implementation include:
	•	Defining multiple services, one for the Flask app and another for Redis, each with appropriate configurations.
	•	Setting environment variables in the Flask service to enable connectivity to the Redis service by hostname.
	•	Mapping container ports to host ports to allow local access and testing.
	•	Establishing service dependencies to ensure the Flask app waits for Redis to initialize properly.
	•	Employing lightweight official Docker images, such as Redis Alpine, to optimize resource usage.
Docker Compose simplifies deployment and management of the application stack with a single command.
Summary
This project demonstrates practical implementation of:
	•	Building optimized Docker images for Python applications.
	•	Crafting clear and efficient Dockerfiles balancing simplicity and performance.
	•	Defining multi-service applications using Docker Compose for streamlined deployment.
	•	Managing service interdependencies and communication in containerized environments.
These practices form a strong foundation for developing scalable, production-ready containerized applications and deploying microservices effectively.

------

├── app.py           # Flask app code 
├── requirements.txt # Python dependencies 
├── Dockerfile       # Docker build config 
├── docker-compose.yml # Docker Compose for Flask + Redis 
└── README.md        # Project documentation



---

## ✨ API Endpoints

| Method | Endpoint | Description                  |
|--------|----------|------------------------------|
| GET    | `/`      | Increment & return visit count |
| POST   | `/echo`  | Returns posted JSON message   |

---

## 🧑‍💻 Requirements

- Python 3.9+
- Flask
- Redis
- Docker & Docker Compose

Install Python dependencies locally (optional):

