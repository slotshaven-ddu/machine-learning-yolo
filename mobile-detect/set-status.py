import requests

API_URL = "http://localhost:8080/update"
requests.post(API_URL, json={"status": False})
print("🔴 Status opdateret!")

# curl -X POST -H "Content-Type: application/json" -d '{"status": false}' http://localhost:8080/update