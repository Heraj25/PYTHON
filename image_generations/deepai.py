

import requests
from requests.structures import CaseInsensitiveDict

import json

QUERY_URL = "https://api.openai.com/v1/images/generations"

def generate_image(prompt):
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    api_key = "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"
    headers["Authorization"] = f"Bearer {api_key}"

    data = """
    {
        """
    data += f'"model": "image-alpha-001",'
    data += f'"prompt": "{prompt}",'
    data += """
        "num_images":1,
        "size":"256x256",
        "response_format":"url"
    }
    """

    resp = requests.post(QUERY_URL, headers=headers, data=data)

    if resp.status_code != 200:
        raise ValueError("Failed to generate image "+resp.text)

    response_text = json.loads(resp.text)
    return response_text['data'][0]['url']

prompt = "A cat sitting on a cloud"
image_url = generate_image(prompt)
print(image_url)
