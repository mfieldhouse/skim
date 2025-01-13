from flask import Flask, render_template, request, jsonify
import json
import os
from openai import OpenAI
from pathlib import Path


app = Flask(__name__)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    plasterboards = data.get('plasterboards')
    plaster_bags = data.get('plasterBags')
    location = data.get('location')
    
    prompt = f"""Find the 3 cheapest places to buy {plasterboards} plasterboards and {plaster_bags} bags of plaster in {location}. 
    Format the response as JSON with this exact structure:
    {{
        "locations": [
            {{"name": "Store Name", "address": "Full Address", "total_price": 123.45}},
            {{"name": "Store Name", "address": "Full Address", "total_price": 123.45}},
            {{"name": "Store Name", "address": "Full Address", "total_price": 123.45}}
        ]
    }}
    Order by total_price ascending (cheapest first). Include real store names and addresses."""
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides accurate pricing information for construction materials."},
                {"role": "user", "content": prompt}
            ],
            response_format={ "type": "json_object" }
        )
        
        result = json.loads(response.choices[0].message.content)
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
