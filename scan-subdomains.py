import subprocess
import requests

domain = input("Enter the domain (e.g., mydomain.gr): ").strip()

url = "https://raw.githubusercontent.com/aboul3la/Sublist3r/master/sublist3r.py"
response = requests.get(url)

with open("sublist3r_temp.py", "w") as f:
    f.write(response.text)

subprocess.run(["python3", "sublist3r_temp.py", "-d", domain])
