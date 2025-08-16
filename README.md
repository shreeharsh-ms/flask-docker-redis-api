# flask-docker-redis-api

This project is a simple **Flask REST API** that counts visits using **Redis**. Containerized with **Docker**, it offers an easy-to-deploy, scalable example of combining Flask, Redis, and Docker for lightweight web services.

---

## Project Overview

This project focuses on containerizing a simple Flask application that uses Redis to store a visit counter. The core emphasis is on writing an efficient `Dockerfile` and orchestrating multiple containers using **Docker Compose**.

---

## Dockerfile Implementation

The `Dockerfile` is designed to set up a lightweight Python environment, install necessary dependencies, and prepare the Flask app to run within a container.  

**Key implementation details:**
- Utilize an official slim Python base image to minimize container size.  
- Define a working directory inside the container for organized file management.  
- copy the dependency file (`requirements.txt`) and install required Python packages using pip.  
- Add the application code into the container image.  
- Expose the appropriate port to make the Flask app accessible externally.  
- Specify the container’s startup command to run the Flask application correctly.  

This approach ensures **optimized layering in Docker**, improving build speed and efficient use of image caching.

---

## ⚙️ Docker Compose Implementation

To manage both the Flask app and its Redis dependency, a `docker-compose.yml` configuration is included. This enables orchestration of multiple containers with ease.  

**Key components:**
- Define multiple services — one for the Flask app and another for Redis.  
- Configure environment variables in the Flask service for connectivity to Redis.  
- Map container ports to host ports for local access and testing.  
- Establish service dependencies so the Flask app waits for Redis to initialize properly.  
- Use lightweight official images (e.g., Redis Alpine) for optimized resource usage.  

With Docker Compose, deployment and management of the application stack is simplified to a single command.

---

## 📖 Summary

This project demonstrates practical implementation of:  
- Building optimized Docker images for Python applications.  
- Crafting clear and efficient Dockerfiles balancing simplicity and performance.  
- Defining multi-service applications using Docker Compose.  
- Managing service interdependencies and communication in containerized environments.  

These practices form a strong foundation for developing **scalable, production-ready containerized applications** and deploying microservices effectively.

---

## Project Structure
-├── app.py # Flask app code

-├── requirements.txt # Python dependencies

-├── Dockerfile # Docker build config

-├── docker-compose.yml # Docker Compose for Flask + Redis

-└── README.md # Project documentation


---

## API Endpoints

| Method | Endpoint | Description                    |
|--------|----------|--------------------------------|
| GET    | `/`      | Increment & return visit count |
| POST   | `/echo`  | Returns posted JSON message    |

---

## Requirements

- Python 3.9+  
- Flask  
- Redis  
- Docker & Docker Compose  

Install Python dependencies locally (optional):  

```bash
pip install -r requirements.txt
