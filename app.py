from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import csv
import pickle
import sklearn
import requests
import tensorflow as tf

app = Flask(__name__)
crop_state_model = pickle.load(open('model/Crop_State.pkl', 'rb'))

model = pickle.load(open('model/model2.pkl','rb'))
disease_model = tf.keras.models.load_model("model/plant_disease_prediction_model.h5")
# disease_model = tf.keras.models.load_model("model/trained_plant_disease_model.keras")
sc = pickle.load(open('model/standscaler2.pkl','rb'))

# API Key
API_KEY = "14eb4cb99a4139d1aca0b7e98b640e26"

crop_to_image_mapping = {'Arecanut': 1,'Arhar/Tur': 2,'Banana': 3,'Black pepper': 4,'Cashewnut': 5,
'Coconut': 6,'Cowpea(Lobia)': 7,'Dry chillies': 8,'Ginger': 9,'Groundnut': 10,'Maize': 11,
'Moong(Green Gram)': 12,'Oilseeds total': 13,'Other Kharif pulses': 14,'other oilseeds': 15,'Rapeseed &Mustard': 16,
'Rice': 17,'Sesamum': 18,'Sugarcane': 19,'Sunflower': 20,'Sweet potato': 21,'Tapioca': 22,'Turmeric': 23,
'Urad': 24,'Bajra': 25,'Castor seed': 26, 'Coriander': 27,'Cotton(lint)': 28,'Garlic': 29,'Gram': 30,'Guar seed': 31,
'Horse-gram': 32,'Jowar': 33,'Linseed': 34,'Masoor': 35,'Mesta': 36,'Niger seed': 37,'Onion': 38,'Other  Rabi pulses': 39,
'Potato': 40,'Ragi': 41,'Safflower': 42,'Sannhamp': 43,'Small millets': 44,'Soyabean': 45,'Tobacco': 46,
'Wheat': 47,'Peas & beans (Pulses)': 48,'Jute': 49,'Barley': 50,'Khesari': 51,'Moth': 52,'Other Cereals': 53,
'Cardamom': 54, 'Other Summer Pulses': 55}

class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew','Cherry_(including_sour)___healthy',
'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot','Corn_(maize)___Common_rust_', 'Corn_(maize)___healthy',
'Corn_(maize)___Northern_Leaf_Blight', 'Grape___Black_rot','Grape___Esca_(Black_Measles)','Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot','Peach___healthy', 
'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy','Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew','Strawberry___Leaf_scorch', 'Strawberry___healthy', 
'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite','Tomato___Target_Spot', 
'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

df = pd.read_csv('indian_crops.csv')

csv_file = 'indian_crops.csv'

data = []
with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data.append(row)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/weather/', methods = ['GET', 'POST'])
def weather():
    city = 'New Delhi'  # Default city
    weather_data = None

    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)

    return render_template('soil.html', city=city, weather_data=weather_data)

def get_weather_data(city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather_info = {
            'temperature': data['main']['temp'],
            'humidity':data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return weather_info
    else:
        return None


@app.route("/predict",methods=['POST'])
def predict():
    N = request.form['Nitrogen']
    P = request.form['Phosporus']
    K = request.form['Potassium']
    temp = request.form['Temperature']
    humidity = request.form['Humidity']
    ph = request.form['Ph']
    rainfall = request.form['Rainfall']
    
    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)

    final_features = sc.transform(single_pred)
    prediction = model.predict(final_features)

    crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        result = "{} is the best crop to be cultivated".format(crop)
    else:
        result = "Sorry, we could not recommend with the given data"
    crop_img=0+prediction[0]
    return render_template('soil.html',result = result,crop_img=crop_img)


@app.route('/states/')
def states():
    state_names = df['State'].unique()
    return render_template('index.html', state_names=state_names, selected_state='', selected_city='',
                           submitted_value='')


@app.route('/get_cities', methods=['POST'])
def get_cities():
    selected_state = request.form.get('selected_state')
    cities = [item["District "] for item in data if item["State"] == selected_state]
    cities = pd.Series(cities).drop_duplicates().tolist()
    return jsonify({'cities': cities})


@app.route('/process_form', methods=['POST'])
def process_form():
    global data
    selected_state = request.form.get('selected_state')
    selected_city = request.form.get('selected_city')
    area = float(request.form.get('numeric_input'))
    crop_name = [item["Crop"] for item in data if
                 item["State"] == selected_state and item["District "] == selected_city]
    crop_name = pd.Series(crop_name).drop_duplicates().tolist()
    season = ['Kharif', 'Rabi', 'Autumn', 'Summer', 'Whole Year', 'Winter']
    suitable_crops = []
    for i in crop_name:
        max_yield = -1
        selected_season = 'Kharif'
        for j in season:
            input_data = np.array([selected_state, selected_city, i, j, area]).reshape(1, 5)
            columns = ['State', 'District ', 'Crop', 'Season', 'Area ']
            my_prediction = crop_state_model.predict(pd.DataFrame(columns=columns, data=input_data)).astype('float')
            increase = np.round_((my_prediction / area), decimals=3)
            if max_yield < increase:
                max_yield = increase
                selected_season = j

        suitable_crops.append([i, str(crop_to_image_mapping[i]), max_yield, selected_season])

    suitable_crops.sort(reverse=True, key=myfunc)
    crops_list = []
    cnt = 0
    for i in suitable_crops:
        if cnt < 5:
            crops_list.append(i)
            cnt = cnt + 1
    crop_cards = []

    for crop_info in crops_list:
        crop_name, image_id, yield_value, season = crop_info
        crop_card = {
            "crop_name": crop_name,
            "image_filename": image_id,
            "yield": yield_value,
            "season": season,
        }
        crop_cards.append(crop_card)

    message = f"State: {selected_state},    City: {selected_city},    Area: {area} hectare"
    return render_template('index.html', state_names=df['State'].unique(), selected_state=selected_state,
                           selected_city=selected_city, submitted_value=area, message=message, crop_cards=crop_cards)


from PIL import Image
import io
def load_and_preprocess_image(image_data, target_size=(224, 224)):
    img = Image.open(io.BytesIO(image_data))
    img = img.resize(target_size)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype('float32') / 255.
    return img_array

def predict_image(image_path):
    preprocessed_img = load_and_preprocess_image(image_path)
    predictions = disease_model.predict(preprocessed_img)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    disease_name = class_name[int(predicted_class_index)]
    return disease_name


@app.route('/disease/', methods=['GET', 'POST'])
def disease():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files.get('file')
        if not file:
            return render_template('disease.html')
        
        img_data = file.read()
        image = img_data

        prediction = predict_image(img_data)
        return render_template('disease.html', prediction=prediction, file=file.filename)
    
    return render_template('disease.html')

def myfunc(e):
    return e[2]


if __name__ == '__main__':
    app.run(debug=True)