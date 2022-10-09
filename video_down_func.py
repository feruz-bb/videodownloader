import requests
import json

def tk(link):
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Key": "bdc9a05c3cmsh7201211cf78545ap140ed2jsn8765bf03d052",
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_txt= response.text
    result = json.loads(json_txt)

    return {"video": result['video'][0], "music": result['music'][0], "original_vid" : result['OriginalWatermarkedVideo'][0]}