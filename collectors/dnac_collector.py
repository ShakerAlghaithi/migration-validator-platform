import requests

def get_dnac_state(token, device_id):
    url = f"https://dnac/api/v1/network-device/{device_id}"

    headers = {
        "X-Auth-Token": token
    }

    response = requests.get(url, headers=headers, verify=False)
    return response.json()
    