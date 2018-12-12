import json
import requests
data="""{
		"Phone_Number":"9643421887", "Name":"Krishna",
		"College_Name":"Poornima","Branch":"Cloud"
}"""
data=json.loads(data)
url="http://13.127.155.43/api_v0.1/sending"
response=requests.post(url,data)
print(str(response.status_code))
response_get=requests.get("http://13.127.155.43/api_v0.1/receiving?Phone_Number=9643421887")
print(response_get.text)
