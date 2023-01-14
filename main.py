from urllib import request

URL = "https://www.cs.utexas.edu/users/EWD/ewd00xx/EWD32.PDF"

response = request.urlretrieve(URL, "EWD32.PDF")