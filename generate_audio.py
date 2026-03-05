import requests
import os

API_KEY = os.getenv("sk_pdzq87h0_mXlW07lB75tudL2EXLTPTWa2")

url = "https://api.sarvam.ai/text-to-speech"

headers = {
    "api-subscription-key": API_KEY,
    "Content-Type": "application/json"
}

story = open("story.txt").read()

payload = {
    "inputs": [story],
    "target_language_code": "te-IN",
    "speaker": "meera",
    "pitch": 0,
    "pace": 1.0,
    "loudness": 1.0,
    "speech_sample_rate": 22050,
    "enable_preprocessing": True
}

response = requests.post(url, json=payload, headers=headers)

audio_bytes = response.content

with open("audio/story1.wav", "wb") as f:
    f.write(audio_bytes)

print("Audio generated!")
