import os
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dotenv import load_dotenv
import base64

load_dotenv()  # Load .env variables
STABILITY_API_KEY = os.environ.get("STABILITY_API_KEY")

class GenerateImage(APIView):
    def post(self, request):
        prompt = request.data.get("prompt")# receive prompt from frontend
        if not prompt:
            return Response({"error": "Prompt is required."}, status=status.HTTP_400_BAD_REQUEST)

        url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"#engine to get the image

        headers = {
            "Authorization": f"Bearer {STABILITY_API_KEY}",#api key
            "Content-Type": "application/json",#send in json
            "Accept": "application/json",#receive in json
        }

        payload = {
            "text_prompts": [
                {
                    "text": prompt,
                    "weight": 1
                }
            ],
            "cfg_scale": 7,#how it matches the prompt
            "clip_guidance_preset": "FAST_BLUE",
            "height": 1024,  # Default height
            "width": 1024,   # Default width
            "samples": 1,
            "steps": 30
        }

        try:
            response = requests.post(url, headers=headers, json=payload)# send to stability.ai
            if response.status_code == 200:
                data = response.json()
                if "artifacts" in data and len(data["artifacts"]) > 0:
                    image_base64 = data["artifacts"][0]["base64"]#extracts the base64 image
                    # Remove data URI prefix if present
                    if image_base64.startswith("data:image"):
                        image_base64 = image_base64.split(",")[1]
                    return Response({"image_base64": image_base64}, status=200)
                else:
                    return Response({"error": "No image data found in response."}, status=500)
            else:
                return Response({
                    "error": f"Stability AI API error: {response.status_code}",
                    "details": response.text
                }, status=response.status_code)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
