# Phonepe-Pulse-Data-Visualization-and-Exploration

**Problem Statement**

Retrieve data from the Phonepe Pulse GitHub repository, perform data transformation and cleansing,insert it into a MySQL database, and develop a live geo-visualization dashboard using Streamlit and Plotly in Python.The dashboard will present the data interactively and aesthetically, featuring a minimum of 10 diverse dropdown optionsfor users to select various facts and figures. The solution aims to be secure, efficient, and user-friendly, offering valuable insights and information about the data within the Phonepe Pulse GitHub repository.

**Technology Stack Used:**

1. Python
2. MySQL
3. Streamlit
4. colab
5. Github Cloning
6. Geo Visualisation

**Installation:**

    pip install pandas
    pip install numpy
    pip install os
    pip install mysql.connector
    pip install git_clone
    pip install stramlit

**Import Libraries:**
    
    import pandas as pd
    import numpy as np
    import os
    import json
    import mysql.connector 
    import streamlit as st
    import plotly.express as px

**Approach:**

1. Data Extraction: The data is obtained from the PhonePe Pulse GitHub repository using scripting techniques and cloned for further processing [(link)](https://github.com/PhonePe/pulse.git).

2. Data Transformation: Process the cloned data using Python algorithms to transform it into DataFrame format, ensuring it is clean and ready for analysis.

3. Database Integration: The transformed data is inserted into a MySQL database, providing efficient storage and retrieval capabilities.

4. Live Geo Visualization Dashboard: Utilizing Python's Streamlit and Plotly libraries, create an interactive and visually appealing dashboard. This real-time dashboard enables users to explore insights effectively.

5. Database Integration with the Dashboard: Fetch relevant data from the MySQL database and seamlessly integrate it into the dashboard, ensuring that the displayed information is up-to-date and accurate.

6. Visualization: Finally, create a dashboard using Streamlit, incorporating selection and dropdown options. Showcase the output through Geo visualization, bar charts, and a DataFrame table.

**Snapshort**

![image](https://github.com/DineshDhamodharan24/Phonepe-Pulse-Data-Visualization-and-Exploration/assets/142207421/43ce8d59-02a4-4630-9317-169d0bc5bb8e)

Top Chart 

- Transactions

![image](https://github.com/DineshDhamodharan24/Phonepe-Pulse-Data-Visualization-and-Exploration/assets/142207421/a846ca0f-2191-441a-a379-18b946d65a07)

- User

![image](https://github.com/DineshDhamodharan24/Phonepe-Pulse-Data-Visualization-and-Exploration/assets/142207421/06a28804-decf-4f72-a131-49a5185abadf)

Explore Data

- Transactions

![image](https://github.com/DineshDhamodharan24/Phonepe-Pulse-Data-Visualization-and-Exploration/assets/142207421/ea68e067-0372-4410-a130-f332a91b1815)

- User

![image](https://github.com/DineshDhamodharan24/Phonepe-Pulse-Data-Visualization-and-Exploration/assets/142207421/932a5458-a707-4fff-8167-54e34332c936)




