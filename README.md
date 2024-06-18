# สร้าง Travel Plan Generator ด้วย Flask และ Google Gemini AI API

ใน repository นี้จะใช้ Flask ต่อกับ Google Gemini AI API ในการสร้างแผนท่องเที่ยวโดยใช้โมเดลภาษา gemini-1.5-flash จาก Google โดยผู้ใช้สามารถกำหนดพารามิเตอร์เช่น จำนวนวัน งบประมาณ สถานที่ท่องเที่ยว ประเภทการท่องเที่ยว จำนวนผู้ร่วมเดินทาง วันที่และเวลาเดินทาง ประเภทที่พัก วิธีการเดินทาง และความต้องการพิเศษเพื่อกำหนด Prompt ในการสร้างแผนท่องเที่ยว 🌍✈️

## สิ่งที่ควรเช็คก่อนใช้

ก่อนที่จะรัน API ให้เช็คก่อนว่ามีโปรแกรมต่อไปนี้หรือยัง:

- Python (>= 3.6)
- Flask (`pip install flask`)
- Flask-CORS (`pip install flask-cors`)
- ไลบรารี `dotenv` ของ Python (`pip install python-dotenv`)
- ไลบรารี `google-generativeai` ของ Python (`pip install google-generativeai`)

## ขั้นตอนการติดตั้ง

1. โคลน repository นี้ลงในเครื่องของคุณ:

```bash
git clone https://github.com/NiabKungg/travel-plan-generator-api.git
```

2. เข้าถึงโฟลเดอร์โปรเจค:

```bash
cd travel-plan-generator-api
```

3. สร้าง virtual environment (ไม่จำเป็น แต่แนะนำ):

```bash
python -m venv venv
```

4. เปิดใช้งาน virtual environment:

   - บน Windows:

```bash
venv\Scripts\activate
```

   - บน macOS และ Linux:

```bash
source venv/bin/activate
```

5. สร้างไฟล์ .env ในโฟลเดอร์โปรเจคและเพิ่ม Google API key:

```dotenv
GOOGLE_API_KEY=your_api_key_here
```

แทนที่ `your_api_key_here` ด้วย Google API key ของคุณ

## วิธีใช้

1. เริ่มต้นเซิร์ฟเวอร์ Flask:

```bash
python app.py
```

2. แอปพลิเคชันจะสามารถเข้าถึงได้ที่ `http://localhost:5000`.

3. เพื่อสร้างเรื่องสยองขวัญ ส่งคำขอ POST ไปที่ `/result` พร้อมกับ JSON payload ดังนี้:

```json
{
  "days_to_travel": "จำนวนวันที่จะไปเที่ยว",
  "budget": "งบประมาณ",
  "want_to_go": "สถานที่ท่องเที่ยวที่ต้องการไป",
  "types_of_tourism": "ประเภทการท่องเที่ยวที่สนใจ",
  "traveling_participants": "จำนวนผู้ร่วมเดินทาง",
  "time_of_travel": "วันที่และเวลาเดินทาง",
  "type_of_accommodation": "ประเภทที่พักที่ต้องการ",
  "how_to_travel": "วิธีการเดินทาง",
  "special_need": "ความต้องการพิเศษ"
}
```

แทนที่ข้อความในเครื่องหมายเร็กเตอร์ (days_to_travel, budget, want_to_go, types_of_tourism, traveling_participants, time_of_travel, type_of_accommodation, how_to_travel, และ special_need) ด้วยค่าที่เหมาะสม

4. เซิร์ฟเวอร์จะตอบกลับด้วยออบเจกต์ JSON ที่ประกอบด้วยเรื่องสยองขวัญที่สร้างขึ้น:

```json
{
  "result": "แผนท่องเที่ยวที่สร้างขึ้นที่นี่"
}
```