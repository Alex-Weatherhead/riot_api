import json

_ENDPOINTS_V3_FILENAME = "./riot_api/api/get/endpoints_v3.json"
with open(_ENDPOINTS_V3_FILENAME, "r") as fp:
    v3 = json.load(fp)

_ENDPOINTS_V4_FILENAME = "./riot_api/api/get/endpoints_v4.json"
with open(_ENDPOINTS_V4_FILENAME, "r") as fp:
    v4 = json.load(fp)