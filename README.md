
Here's a README for your project:

Dockerized Application Infrastructure
Context
Docker is a platform that enables you to package your applications into portable, self-contained environments, known as containers. These containers can run anywhere, making it easy to move your application between different environments — from local development machines to production servers — without worrying about dependencies or configuration issues. Containers include everything an application needs to run, such as libraries, dependencies, and configurations, and they are lightweight, allowing them to start and stop quickly. Docker's ability to scale applications by running multiple containers of the same application on different hosts (or on the same host) makes it an essential tool for modern software development and deployment.

In this project, you will create an infrastructure for an application that utilizes a reverse proxy, a load balancer, two application servers, and one front-end server.

High-Level Design
The infrastructure is designed with a single server acting as the entry point for your application. This server serves multiple roles:

Reverse Proxy: Routes incoming traffic to either the API servers or the front-end static-content server.
Load Balancer: Distributes traffic between two API servers using the Round Robin algorithm.
Traffic Routing
Front-End Static-Content Server:
If the request is routed to the front-end static-content server, the proxy server forwards any static content that is returned from this server to the client. The client does not directly communicate with the front-end static-content server.

API Servers:
If the request is routed to the API servers, it first passes through a load balancer that uses the Round Robin algorithm to determine which API server should handle the request. Once the response is generated, it is sent back to the proxy server and then forwarded to the client. The client does not directly communicate with the API servers.

Round Robin Load Balancing
Round Robin load balancing distributes traffic evenly across multiple servers by assigning requests to each server in a rotating manner. For example, if there are three servers (A, B, and C), the first request will be sent to server A, the second to server B, the third to server C, and so forth. This process repeats in a cycle, ensuring that each server receives an equal share of the traffic. While Round Robin is a simple and effective load-balancing method, it may not be suitable for all applications, particularly those with varying workload patterns or resource requirements. However, for learning purposes, it will suffice for this project.

Prerequisites
Before you begin, ensure you have the following:

Docker Desktop installed on your local machine.

Download and install Docker Desktop from: Docker Website
Familiarity with Docker:

Understand the basics of Docker, including concepts such as images, containers, Dockerfiles, and Docker Compose.
You can start with the Docker Tutorial.
Installation Instructions
For Windows:
Follow the instructions provided on the Docker website for setting up Docker Desktop on Windows.

For Mac:
Refer to the Docker documentation for installing Docker Desktop on macOS.

For Linux:
Install Docker engine on Linux by following the platform-specific instructions on Docker's website.

For Chromebook:
Docker may be installed as the Docker engine, but not Docker Desktop. It is recommended to use a different machine (Windows, Mac, or Linux) if possible.

Setting Up the Project
Clone the Repository:

bash

git clone <repository-url>
cd <project-directory>
Build Docker Images: Use the provided Dockerfile and docker-compose.yml to build the images:

bash

docker-compose build
Start the Containers: Start the containers using Docker Compose:

bash

docker-compose up
Check Application Status: Verify that all services are up and running:

bash

docker ps
Access the Application: Open a web browser and navigate to http://localhost to access the application.

Additional Resources
Docker Documentation
Docker Compose Documentation
Understanding Reverse Proxies
License
This project is licensed under the MIT License - see the LICENSE file for details.
