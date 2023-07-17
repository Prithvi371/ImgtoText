import requests
import json

url = "https://stablediffusionapi.com/api/v3/text2img"

payload = json.dumps({
  "key": "FBHsplDFzfri86H36NK2XG5ybFmxjUyDjWjSS38FVITAC8V03ccWXqoRNaS7",
  "prompt": "black muscula pikachu attacking with lightning bolts,ultra realistic,4K",
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