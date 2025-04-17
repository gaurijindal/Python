import requests

# GET request (fetch users)
response = requests.get("https://reqres.in/api/users", verify=False)
print(response.json())

# POST request (create a user)
data = {"name": "John", "job": "developer"}
response = requests.post("https://reqres.in/api/users", json=data,verify=False)
print(response.json())

# PUT request (update user)
update_data = {"name": "John", "job": "senior developer"}
response = requests.put("https://reqres.in/api/users/2", json=update_data,verify=False)
print(response.json())

# DELETE request (delete user)
response = requests.delete("https://reqres.in/api/users/2",verify=False)
print(response.status_code)  # 204 (No Content)