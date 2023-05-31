import pypdf
import pandas as pd
from tabula.io import read_pdf
from flask import Flask, jsonify

table_pdf = read_pdf('C:/Users/UNS_CT/Desktop/iknowplus/data/12.September2021.pdf', pages=1, stream=True)

data_table = []

for i in range(2,13):
    data_table.append(table_pdf[0]['Unnamed:'+' '+str(i)][4:54])

# print(table_pdf)
k = []
for i, data in enumerate(data_table):
    
    data = str(data).split()
    k.append(data)

waste_data = []
for i in k:
    for j in i:
        j = j.replace(',', '')

        try:
            j = float(j)
            if j > 60:
                
                waste_data.append(j)  
        except:
            pass

districts = [  
                "เขตคลองเตย",
                "เขตคลองสาน",
                "เขตคลองสามวา",
                "เขตคันนายาว",
                "เขตจตุจักร",
                "เขตจอมทอง", 
                "เขตดอนเมือง",
                "เขตดินแดง",
                "เขตดุสิต",
                "เขตตลิ่งชัน",
                "เขตทวีวัฒนา",
                "เขตทุ่งครุ",
                "เขตธนบุรี",
                "เขตบางกอกน้อย",
                "เขตบางกอกใหญ่",
                "เขตบางกะปิ",
                "เขตบางขุนเทียน",
                "เขตบางเขน",
                "เขตบางคอแหลม",
                "เขตบางแค",
                "เขตบางซื่อ",
                "เขตบางนา",
                "เขตบางบอน",
                "เขตบางพลัด",
                "เขตบางรัก",
                "เขตบึ่งกุ่ม",
                "เขตปทุมวัน",
                "เขตประเวศ",
                "เขตป้อมปราบศัตรูพ่าย",
                "เขตพญาไท",
                "เขตพระโขนง",
                "เขตพระนคร",
                "เขตภาษีเจริญ",
                "เขตมีนบุรี",
                "เขตยานนาวา",           
                "เขตราชเทวี",  
                "เขตราษฎร์บูรณะ",
                "เขตลาดกระบัง",
                "เขตลาดพร้าว",
                "เขตวังทองหลาง",
                "เขตวัฒนา",
                "เขตสวนหลวง",
                "เขตสะพานสูง",
                "เขตสัมพันธวงศ์",
                "เขตสาทร",
                "เขตสายไหม",
                "เขตหนองแขม",
                "เขตหนองจอก",
                "เขตหลักสี่",              
                "เขตห้วยขวาง",
            ]

waste_json = {}

for i in range(50):
    waste_json[districts[i]] = waste_data[i: len(waste_data): 50]

print(waste_json)

app = Flask(__name__)

@app.route('/api/data')
def get_data():

    return jsonify(waste_json)

if __name__ == '__main__':
    app.run(port=3000)
