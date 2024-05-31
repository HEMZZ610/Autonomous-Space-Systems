# Continuously Updated ML block for autonomous satellite systems

In order to have an autonomous telemetry anomaly detection and mitigation block in a distributed satellite systems. Continuously updated machine learning block is the way to autonomous capabilities in on-board systems. In this work, tailored ML algorithms trained with NASA archived mission data sets is embedded on OBDH systems to process data directly in-orbit to make autonomous decisions on real-time without relying on ground stations for  immediate guidance.

## Key Components 

On-board processing unit – In this research work the ML algorithm is trained assuming there will be a dedicated processing unit such as FPGA, GPU or specialized ASIC for excepting ML algorithms, where this unit will handles data directly from the satellite’s sensors. A trade-off analysis will be done in upcoming weeks after preliminary training to evaluate which type of processing unit is more capable of handling big data efficiently while keeping the cost and reliability intact. This so because of the llimited power and computational resources.

Current plan is to pre-train the machine learning model with initial satellite data from real missions. For this, previous NASA’s Archive of Space Geodesy Data is being used substantially. During the pre-training phase, several machine learning models are used on these data sets to evaluate the performance based several factors. These models performs functions such as filtering, clustering before anomaly detection procedure. Based on the results if there is fault/anomaly, mitigation loop will be triggered based already trained ideals. This way the spacecraft will continuously collects  from sensors and evaluate at real time. Also, the usage of real time data will be valuable in diagnosing the performance of ML model so that the models can be periodically updated based on new data and updates can be uploaded from ground stations or in-orbit stations to retrain the on-board systems based on new data ensuring the model remains accurate and relevant.

This type of approach can make the model versatile on usage, ranging from distributed space systems ranging from earth observation, environmental monitoring, communication, in-orbit manufacturing, space debris removal and during autonomous navigation and hazard detection for interplanetary missions.

Later phase of this work will also look up on developing ML algorithm networks for creating intelligent satellites that can share insights and coordinate actions autonomously. This concept will remain on hold with only looking of literature review side as of now. If the preliminary model predicts results on the range of ECSS Standards the model development will be considered in upcoming months.

## Git Hub File Structure and naming nomenclature
