from urllib import request
import requests
print(requests.__version__)
print(requests.get("http://www.google.com"))
print(requests.get("https://raw.githubusercontent.com/jacob-gerun/CMPUT_404_Lab_1/main/lab_1_script.py").text)