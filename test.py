from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data
crop_data = [
    ["Wheat", 11, 1.5, "Summer"],
    ["Rice", 12, 1.6, "Kharif"],
    ["Potato", 17, 0.2, "Winter"],
    ["Oranges", 14, 1.05, "Rabi"],
]

crop_to_image_mapping = {
    "Wheat": "image_47.png",
    "Rice": "image_17.png",
    "Potato": "image_40.png",
    "Oranges": "image_11.png",
}

@app.route('/')
def index():
    return render_template('crop_display.html')

@app.route('/display_crops', methods=['POST'])
def display_crops():
    input_1 = request.form.get('input1')
    input_2 = request.form.get('input2')

    #selected_crops = [crop for crop in crop_data if input_1 in crop and input_2 in crop]

    crop_cards = []

    for crop_info in crop_data:
        crop_name, image_id, yield_value, season = crop_info
        image_filename = crop_to_image_mapping.get(crop_name)
        crop_card = {
            "crop_name": crop_name,
           "image_filename": image_filename,
            "yield": yield_value,
            "season": season,
        }
        crop_cards.append(crop_card)

    return render_template('crop_display.html', crop_cards=crop_cards)
#
# if __name__ == '__main__':
#     app.run(debug=True)
