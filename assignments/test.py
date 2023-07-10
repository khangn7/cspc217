import os
stream = os.popen('py ./main.py')
output = stream.read()

print(output)