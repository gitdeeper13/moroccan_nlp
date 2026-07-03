"""
DarijaBERT - Load via Hugging Face API (No local installation)
"""

import requests
import json

print("🔍 Testing DarijaBERT via Hugging Face API...")
print("=" * 60)

# استخدام API للاستدلال
API_URL = "https://api-inference.huggingface.co/models/SI2M-Lab/DarijaBERT"
headers = {"Authorization": "Bearer YOUR_HUGGINGFACE_TOKEN"}  # اختياري

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# اختبار Fill-Mask
print("\n📝 Testing Fill-Mask:")
output = query({
    "inputs": "اشنو [MASK] ليك",
})

print(f"Result: {json.dumps(output, indent=2, ensure_ascii=False)}")

print("\n" + "=" * 60)
print("⚠️ Note: Hugging Face API may have rate limits.")
print("💡 For local usage, install transformers: pip install transformers")
