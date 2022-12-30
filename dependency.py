import os

# install Flask
output = os.popen("pip install Flask").read()
print(output)

# install other libraries
output = os.popen("pip install Werkzeug").read()
print(output)
output = os.popen("pip install Pillow").read()
print(output)