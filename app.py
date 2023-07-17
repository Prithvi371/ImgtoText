from flask import Flask, jsonify,render_template,request
import json
import requests     

app = Flask(__name__ , static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_image', methods=['POST'])
def generate_image():
    prompt = request.form['prompt'] 

    # Invoke the text-to-image API
    # api_url = 'https://stablediffusionapi.com/api/v3/text2img'
    # headers = {'Content-Type': 'application/json'}
    # payload = {'prompt': prompt}
    # response = requests.request("POST", api_url,headers=headers, data=payload)
    # print(response.text)


    url = "https://stablediffusionapi.com/api/v3/text2img"

    payload = json.dumps({
    "key": "3MwsWHt1ydgbTawxxjNQHb9SXrMatPkC5JENtv4tzfnJIFKPVM4FvVwVjvPC",
    "prompt": prompt,
    "negative_prompt": None,
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "20",
    "seed": None,
    "guidance_scale": 7.5,
    "safety_checker": "yes",
    "multi_lingual": "no",
    "panorama": "no",
    "self_attention": "no",
    "upscale": "no",
    "embeddings_model": None,
    "webhook": None,
    "track_id": None
    })

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

    if response.status_code == 200:
        api_response = response.json()
        print(api_response)
        if api_response['status'] == 'success' and 'output' in api_response:
            image_url = api_response['output'][0]
            return render_template('index.html', image_url=image_url)
        else:
            error_message = 'Image URL not found in API response.'
    else:
        error_message = 'Error occurred while generating the image.'

if __name__ == '__main__':
    app.run(debug=True)
