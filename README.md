# Crop Counsel

<img src="https://github.com/candy-kush/crop-counsel/assets/96912080/2ff035df-4e28-4046-994d-ea584077e822" width="300" height="200">
<img src="https://github.com/candy-kush/crop-counsel/assets/96912080/62d24ccb-6b30-4ff4-bb25-cc4a95505d6d" width="300" height="200">

## Introduction
`Crop Counsel` is a machine learning based crop-prediction model to support farmers in making informed decisions about `crop selection`, plantation and harvesting.
It aims to `optimize yields` and `maximize profitability` of farmers using data driven smart prediction mechanism.
##### Underlying principles - 
1. We have developed and applied a smart system that can suggest suitable crops for farmers across India using the emerging power of machine learning.
2. This system would help the farmers choose the best crop based on factors like `Nitrogen`, `Phosphorous`, `Potassium`, `PH Value`, `Humidity`, `Temperature`, and `Rainfall`.
3. Based on the previous records of the `State` and `City` ,farmers also get an estimated yield of the common crop according to the available land area.
4. Models underlying the system are trained on realtime dataset with a high level of accuracy suggestion.

The portal consists of three parts -
##### 1. Prediction based on soil type
The system takes into account several factors such as soil type, climate, rainfall, temperature, humidity, and pH levels to determine the most suitable crops for a given region. 
##### 2. Prediction based on geographical trends
By analyzing historical data and using predictive models, the system provides personalized recommendations tailored to the specific conditions of a farm or agricultural area.
##### 3. Disease detection
The disease detection feature scan and analyze the patterns and the unusual developments on the leaves of the plant and gives us the output of what kind of disease has captured the crop.

## Other Features
The website consists of a beautiful and easy to use Login/Register portal. It also supports user authentication and error handling. The user information is stored in database connected via MySql and running on Apache server. It is administered by phpMyAdmin.

## Important Links
1. Dataset for geolocation-based recommendation - https://aps.dac.gov.in/Home.aspx?ReturnUrl=%2f
2. Dataset for soil-based recommendation - https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset
3. Dataset for disease detection - https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset?resource=download
4. Demo Video - https://youtu.be/tExfef-Tk9c
5. Pickle Files - https://drive.google.com/drive/folders/1KYVnDR0ijuLY9Iu2BrSPCDNh11NBd1nX?usp=sharing
6. Report - https://drive.google.com/file/d/1FoCSh9tk-4MqUj9TjT8-Dj-EHybhD5BW/view?usp=sharing

## Stages of development
1. `Input Data Collection`: The system allows users to input relevant data such as `soil parameters`, `climate information`, and `geographical location`.
2. `Data Preprocessing`: The input data is preprocessed to handle missing values, normalize or scale features, and transform categorical variables.
3. `Machine Learning Models`: Various machine learning algorithms are employed, including `Decision Tree`, `Random Forest`, `Support Vector Machines` (SVM), `Convolutional Neural Network` (CNN) and `Gradient Boosting` techniques, to build predictive models.
4. `Model Training and Evaluation`: The models are trained on historical data and evaluated using appropriate performance metrics to ensure accuracy and reliability.
5. `Crop Recommendation`: Based on the trained models, the system recommends the most suitable crops for the given input parameters.
6. `Disease Detection`: It takes the clear image of a leaf of the particular crop and predicts the result as name of the disease.
7. `User-Friendly Interface`: The system provides a user-friendly responsive interface where users can easily input their data, view recommendations, and explore additional information.

![image](https://github.com/candy-kush/crop-counsel/assets/96912080/eba84e5b-83a5-475c-bdb9-1e152466a8aa)


## Requirements
##### Hardware - 
1. System: `Pentium i3` processor and above.
2. Hard Disk: `500 GB` and more.
3. RAM: `4 GB` and above
##### Software - 
1. Operating system   : `Windows 10` & above


## Technologies used
##### 1. Programming Language : Python
##### 2. Libraries : Numpy, Pandas, Scikit-Learn, Tensorflow, Keras
##### 3. Frontend Tools : HTML, CSS, Bootstrap, Javascript, pHp
##### 4. Other Tools : Flask, Weather API, MySql, Apache

## Collaborators
<a href="https://github.com/mrsoup0x2f" target="_blank">Praveen Patel</a> 🤝 <br/>
<a href="https://github.com/ashutoshark" target="_blank">Ashutosh Kumar</a> 🤝 

## Screenshots
![image](https://github.com/candy-kush/crop-counsel/blob/main/static/crop_state/home.jpg)
![image](https://github.com/candy-kush/crop-counsel/blob/main/static/crop_state/our-services.png)
![image](https://github.com/candy-kush/crop-counsel/blob/main/static/crop_state/contact.png)
![image](https://github.com/candy-kush/crop-counsel/assets/96912080/4004bc0f-393e-4782-8a28-5a2c8b99b260)
![image](https://github.com/candy-kush/crop-counsel/blob/main/static/crop_state/soil-recommended.jpg)
![image](https://github.com/candy-kush/crop-counsel/assets/96912080/8104bca6-8800-4d6f-a42c-a8fe897b5294)
![image](https://github.com/candy-kush/crop-counsel/assets/96912080/20c65f00-f5f5-400e-b36d-679c0b4ada7a)
![image](https://github.com/candy-kush/crop-counsel/blob/main/static/crop_state/uploaded-image.jpg)
![image](https://github.com/candy-kush/crop-counsel/blob/main/static/crop_state/predicted-disease.jpg)
![image](https://github.com/candy-kush/crop-counsel/blob/main/static/crop_state/register.jpg)
![image](https://github.com/candy-kush/crop-counsel/blob/main/static/crop_state/login.jpg)
