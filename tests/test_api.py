import requests
import json

server = "http://localhost:8000"

CREATE = False
UPDATE = False
DELETE = False

IMG_CREATE = False

if CREATE:
    print(requests.post(
            server + '/v1/user', json.dumps({
                'name': 'test_user_name'
            })).text)

if UPDATE:
    print(requests.patch(
            server + '/v1/user/1', json.dumps({
                'name': 'test_user_name_01'
            })).text)
if DELETE:
    print(requests.delete(
            server + '/v1/user/1').text)
