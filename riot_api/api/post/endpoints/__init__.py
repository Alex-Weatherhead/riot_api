import json

_ENDPOINTS_V4_FILENAME = "./riot_api/api/post/endpoints_v4.json"
with open(_ENDPOINTS_V4_FILENAME, "r") as fp:
    v4 = json.load(fp)