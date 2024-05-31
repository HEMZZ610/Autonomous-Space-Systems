# Continuously Updated ML block for autonomous satellite systems

In order to have an autonomous telemetry anomaly detection and mitigation block in a distributed satellite systems. Continuously updated machine learning block is the way to automate the capabilities in on-board data handling subsystems. In this work, tailored ML algorithms trained with NASA archived mission data sets is embedded on OBDH systems to process data directly in-orbit to make autonomous decisions on real-time without relying on ground stations for  immediate guidance.

## Key Components 

### Current Plan for ML Model Training:
  - Pre-train the machine learning model using initial satellite data from real missions.
  - Substantially use NASA’s Archive of Space Geodesy Data for pre-training.
  - Evaluate several machine learning models on these datasets based on various performance factors such as computational time, memory used, power, system reliability.
![image](https://github.com/HEMZZ610/Autonomous-Space-Systems/assets/70131462/abc8d1ce-b4c3-4edd-ac10-a9d76ef9b152)

### Anomaly Detection and Mitigation:
  - If a fault/anomaly is detected, a mitigation loop is triggered based on pre-trained models.
  - The spacecraft continuously collects and evaluates sensor data in real-time.
  - Real-time data usage helps in diagnosing ML model performance.
  - Models are periodically updated based on new data, with updates uploaded from ground or in-orbit stations.

### Versatility of the Approach:
  - Applicable to distributed space systems including Earth observation, environmental monitoring, communication, in-orbit manufacturing, space debris removal, autonomous navigation, and hazard detection for interplanetary missions.

### Future Work:
  - Develop ML algorithm networks for creating intelligent satellites capable of sharing insights and coordinating actions autonomously.
  - This concept is currently on hold, with a focus on literature review.
  - Model development will be considered if preliminary results meet ECSS Standards.

## Git Hub Repository Nomenclature
* Data = Data_mission_datatype
* Paper =
* Demo = 
* Explore = 
* Save = 

