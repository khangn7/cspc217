# import glob

# print(glob.glob("C:\\Windows\\*"))

import pip._vendor.requests as requests

# content = ""

url = "https://jsonblob.com/api/1129087061272576000"

response = requests.get(url)

print(response.json())

# filepath = "hello.py"

# with open(filepath) as file:
#     pass
