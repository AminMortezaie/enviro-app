# Project Documentation for IIoT System Monitoring

## 1. Design Documentation

### System Architecture

The system architecture comprises four main components: Simulator, Server, Database, and Dashboard.

#### Simulator

- **Purpose**: Simulates sensors generating random temperature and humidity data and sends this data to the MQTT broker every 10 seconds.
- **Components**:
  - A Python script (`app/hub_simulator.py`) using `paho-mqtt` to publish data to the MQTT broker.

#### Server

- **Purpose**: Subscribes to MQTT topics, receives data from the simulator, and stores it in the SQLite database.
- **Components**:
  - Django application with a `sensor_data` app.
  - A Python script within the Django app to subscribe to MQTT topics and process incoming data.

#### Database

- **Purpose**: Stores the sensor data received by the server.
- **Components**:
  - SQLite database to store sensor data.
  - A `SensorData` model in Django to define the database schema.

#### Dashboard

- **Purpose**: Provides a user interface to visualize the sensor data.
- **Components**:
  - A React application named `sensor-dashboard` for the frontend.
  - A React component (`GraphComponent.jsx`) to display the sensor data using a graph.
  - It runs on port 3000, to see the graph you should use this port.

### System Diagram

The system architecture can be visualized as follows:

- **Simulator**: Generates and publishes sensor data -> **MQTT Broker** (Mosquitto)
- **Server**: Subscribes to MQTT topics and stores data -> **Database** (SQLite)
- **Dashboard**: Fetches and displays sensor data -> **User Interface**

## 2. Setup and Deployment

### Prerequisites

- Docker and Docker Compose installed on your machine.
- Set hub_id which is the name of hub to application work.

### Step-by-Step Instructions

#### 1. Clone the Repository

```sh
git clone https://github.com/AminMortezaie/enviro-app/
cd enviroapp
```

#### 2. Setting up the Django Server

1. **Start the Application**:
    ```sh
    docker-compose up --build
    ```

2. **Run migrations**:
    In a new terminal window, execute the following commands to make migrations and migrate using Docker:
    ```sh
    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate
    ```
   
3. **Watch Graphs**:
   You can reach graphs on port 3000:
   http://0.0.0.0:3000

4. **Set Hub Name and Sleep Duration**
   For setting Hub name and sleep Duration you change the values in simulator container:
```sh
simulator:
    build: ./hub_image/
    container_name: hub_simulator
    volumes:
      - ./app:/src
    command: python /src/hub_simulator.py "amin_hub" 10
    networks:
      - hub-network
```

   Set your desire hub name instead of **"amin_hub"** and sleep duration which set to **"10"** seconds.

   ### **Attention**
   You need to set hub_id in **.env** file to run the application and its name must be same with your hub name passed to simulator container.

By following these steps, you can set up and run the system efficiently. The `docker-compose up --build` command will start all the necessary services, including the MQTT broker, simulator, Django server, and React dashboard. The `docker-compose exec` commands will ensure that the Django server is properly set up with the latest database migrations.

## 3. Decision Documentation

### Technologies Chosen

1. **Python and Django for Server**:
   - **Reason**: Django provides a robust framework for rapid development and comes with built-in support for ORM, making it easy to interact with the SQLite database.

2. **SQLite for Database**:
   - **Reason**: SQLite is lightweight and easy to set up, suitable for this project's requirements without needing a more complex database setup.

3. **paho-mqtt for MQTT Client**:
   - **Reason**: `paho-mqtt` is a reliable and widely-used library for MQTT communication in Python.

4. **React for Dashboard**:
   - **Reason**: React allows for a modular and component-based approach to building UIs, making it easier to manage and scale the frontend application.

5. **Docker for Containerization**:
   - **Reason**: Docker allows for consistent environment setup and easier deployment by containerizing the application components.

### Challenges Using Mosquitto and Other Brokers

#### Mosquitto

1. **Configuration Complexity**:
   - Advanced configuration for authentication, authorization, and SSL/TLS can be complex.
   - Ensuring secure configuration to prevent unauthorized access requires proper knowledge.

2. **Scalability**:
   - Suitable for small to medium scale applications, but scalability might be an issue for very large-scale applications.
   - Implementing clustering and load balancing can be non-trivial.

3. **Persistence**:
   - Supports message persistence, but managing persistence storage requires additional configuration and maintenance.

4. **Limited Features**:
   - Focuses on being a lightweight MQTT broker, lacking some advanced features found in comprehensive messaging brokers like RabbitMQ or Kafka.

#### RabbitMQ

1. **Resource Consumption**:
   - More resource-intensive compared to Mosquitto, requiring more memory and CPU.
   - Less suitable for lightweight or resource-constrained environments.

2. **Complexity**:
   - Steeper learning curve due to extensive feature set.
   - Managing RabbitMQ in production requires more effort in terms of monitoring, scaling, and maintenance.

3. **Overhead**:
   - Additional features and complexities might be overkill for simple publish-subscribe use cases.

### Why Use Mosquitto Over RabbitMQ

1. **Lightweight**:
   - Mosquitto is suitable for resource-constrained environments and applications with simple messaging needs.
   - Small footprint and easy deployment on devices with limited resources.

2. **Simplicity**:
   - Straightforward to install and configure for basic use cases.
   - Reduces overhead in terms of time and effort required to manage the broker.

3. **Performance**:
   - Optimized for fast message delivery and low resource usage.
   - Provides reliable performance for high-frequency messaging without additional complexity.

4. **Community and Support**:
   - Large community of users and contributors providing extensive documentation, tutorials, and support forums.
   - Active development and regular updates ensure it remains secure and up-to-date.

5. **Focus on MQTT**:
   - Dedicated MQTT broker focusing solely on the MQTT protocol, ideal for applications requiring lightweight publish-subscribe messaging.
   - RabbitMQ’s extensive feature set and protocol support add unnecessary complexity for pure MQTT use cases.

### Summary

This documentation provides a comprehensive overview of the IIoT system for monitoring temperature and humidity levels, including design, setup, and decision-making processes. By following the provided steps, you can set up and run the system efficiently, ensuring a robust and scalable monitoring solution.