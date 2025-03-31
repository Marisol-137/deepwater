# Deepwater

## Description 
We have created a mobile application based on Watsonx.AI's Granite-3-8b-instruct model. Its main function is to provide recommendations for household water use from YF-S401 sensors and Wifi ESP32 microcontrollers that measure the flow of water consumed by each area of the house where water is used. The result is an application that allows the user to see how much water he and/or his/her family consumes for each area of his/her home and per day. With the database collected by the sensors, the chatbot can recommend and send alerts to the user on the efficient use of water. 


<p align="center">
  <img width="auto" height="auto" src="https://github.com/Marisol-137/deepwater/blob/main/HARDW2.jpg">
</p>


This technological solution mainly contributes to ODS 6 (Clean Water and Sanitation), by promoting efficient and responsible water consumption through IoT sensors and customized recommendations based on AI. In addition, it directly impacts ODS 11 (Sustainable Cities) and ODS 12 (Responsible Consumption), boosting sustainable household habits, and indirectly supports ODS 13 (Climate Action), as reducing water consumption also involves reducing energy expenditure related to its treatment and distribution.

<p align="center">
  <img width="auto" height="auto" src="https://github.com/Marisol-137/deepwater/blob/main/DeepWater%20Mobile%20Prototype.png">
</p>


## Problem and solution statement 
Water waste affects the environment and household finances. The lack of real-time monitoring makes detecting excessive usage and leaks difficult, leading to inefficient resource use. To solve this, DeepWater is a smart app that allows users to track daily, weekly, and monthly water consumption, segmented by different areas of the home. 

<p align="center">
  <img width="auto" height="auto" src="https://github.com/Marisol-137/deepwater/blob/main/DeepWater%20Mobile%20Prototype%20(5).png">
</p>


It also provides an estimated monthly cost, helping to manage expenses efficiently. Additionally, it features an interactive chatbot that instantly answers questions and offers water-saving tips. For better control, the app sends real-time alerts when it detects excessive usage, allowing users to take corrective action and prevent waste.


<p align="center">
  <img width="auto" height="auto" src="https://github.com/Marisol-137/deepwater/blob/main/16.png">
</p>


## AI-powered virtual agent using IBM watsonx.ai 
DeepWater was developed with an advanced artificial intelligence approach, utilizing IBM Watsonx.ai and its Granite model, which enabled enhanced water consumption analysis and optimization. From data acquisition to recommendation generation, the system was designed to leverage IBM's AI capabilities, ensuring accurate detection of anomalies and inefficient usage patterns.

Development began with the implementation of a Python system to process water consumption data. Libraries such as Pandas and NumPy were used to structure the information, clean the data, and prepare training sets. However, the true power of the system lies in its integration with IBM Watsonx.ai, where the Granite model handles advanced data processing. Through the LangChain library, we connected DeepWater to Watsonx.ai, allowing the model to access information in real time, analyze consumption patterns, and make inferences about potential leaks, waste, or inefficiencies in the distribution network.

IBM Watsonx.ai technology offers key advantages in this process. Its Granite model is designed to understand complex data, identify anomalies with high accuracy, and generate context-specific responses. Unlike traditional approaches that rely on predefined rules, Granite uses deep learning and natural language processing techniques, allowing it to analyze historical data and predict variations in consumption with a high degree of accuracy. This is crucial in applications such as water management, where early detection of leaks or overconsumption patterns can generate significant savings and improve water efficiency.


<p align="center">
  <img width="auto" height="auto" src="https://github.com/Marisol-137/deepwater/blob/main/fun2.png">
</p>


Once IBM's AI processes the data and generates recommendations, the results are displayed in an interactive interface built with Streamlit. Thanks to this technology, users can view their consumption in real-time, receive alerts, and access detailed reports on their water usage. 


<p align="center">
  <img width="auto" height="auto" src="https://github.com/Marisol-137/deepwater/blob/main/DeepWater%20Mobile%20Prototype%20(4).png">
</p>


Additionally, the system incorporates a feedback mechanism that allows users to validate the recommendations, which in turn helps Watsonx.ai continuously improve its predictions and adapt to different usage patterns.


<p align="center">
  <img width="auto" height="auto" src="https://github.com/Marisol-137/deepwater/blob/main/DeepWater%20Mobile%20Prototype%20(2).png">
</p>


The use of IBM Watsonx.ai in DeepWater not only optimizes water management but also demonstrates how artificial intelligence can be applied to solve critical challenges in sustainability and resource efficiency. 


<p align="center">
  <img width="auto" height="auto" src="https://github.com/Marisol-137/deepwater/blob/main/11.png">
</p>

By combining Granite's capabilities with the flexibility of Python and Streamlit, we were able to create a solution that not only analyzes consumption in real time but also offers personalized recommendations, helping businesses and households reduce waste and improve their environmental impact.


<p align="center">
  <img width="auto" height="auto" src="https://github.com/Marisol-137/deepwater/blob/main/architecture.jpg">
</p>


## Video demonstration URL 
Video demonstration: https://youtu.be/Odk4T1GTs20

## Demo
Live Demo: https://www.canva.com/design/DAGjLKjPAHw/VbIv7s7mFwwLAppJZ9I5rA/view?mode=prototype

Video Demo: https://youtube.com/shorts/YtUSTdsJrtk?feature=share

Deep Water 2.0: https://drive.google.com/file/d/1EJroflAI1bQSNwAQWI2MFKwAxTsqpDFZ/view?usp=sharing
