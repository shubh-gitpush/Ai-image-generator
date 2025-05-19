from dotenv import load_dotenv
load_dotenv()

# StarryAI API endpoint
url = "https://api.starryai.com/v1/creations"
headers = {
  "Authorization": f"Bearer {STARRYAI_API_KEY}",
  "Content-Type": "application/json"
}
payload = {
  "prompt": "lion",
  "style": "art",  # You can customize the style as needed
  "aspect_ratio": "1:1"  # Optional, customize as needed
}
