import os
from dotenv import load_dotenv
import google.generativeai as genai
from flask import Flask, jsonify, request
from flask_cors import CORS

load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)
CORS(app,origins=["http://localhost:5173"])

@app.route("/result", methods=['POST'])
def generate_travel_plan():
    data = request.get_json()
    days_to_travel = data.get('days_to_travel', '')
    budget = data.get('budget', '')
    want_to_go = data.get('want_to_go', '')
    types_of_tourism = data.get('types_of_tourism', '')
    traveling_participants = data.get('traveling_participants', '')
    time_of_travel = data.get('time_of_travel', '')
    type_of_accommodation = data.get('type_of_accommodation', '')
    how_to_travel = data.get('how_to_travel', '')
    special_need = data.get('special_need', '')

    prompt = (
        f"กรุณาสร้างแพลนท่องเที่ยวสำหรับ {traveling_participants} คน "
        f"ในระยะเวลา {days_to_travel} วัน ด้วยงบประมาณ {budget} บาท "
        f"โดยต้องการไปที่ {want_to_go} และสนใจการท่องเที่ยวแบบ {types_of_tourism}. "
        f"การเดินทางจะเริ่มในวันที่ {time_of_travel} และต้องการที่พักแบบ {type_of_accommodation}. "
        f"วิธีการเดินทางหลักจะเป็น {how_to_travel}. "
        f"ความต้องการพิเศษ: {special_need}."
    )

    response = model.generate_content(prompt)
    travel_plan = response.text

    return jsonify(result=travel_plan)

if __name__ == '__main__':
    app.run(debug=True)
