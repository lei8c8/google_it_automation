import json

with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)

[
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  },
  {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  },
]

import yaml

with open('people.yaml', 'w') as people_yaml:
    yaml.safe_dump(people, people_yaml)

# - department: IT Infrastructure
#   name: Sabrina Green
#   phone:
#     cell: 802-867-5310
#     office: 802-867-5309
#   role: Systems Administrator
#   username: sgreen
# - department: IT Infrastructure
#   name: Eli Jones
#   phone:
#     office: 684-348-1127
#   role: IT Specialist
#   username: ejones

# >>> import requests
# >>> response = requests.get('https://www.google.com')
# >>> print(response.text[:300])
# <!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="de"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="dZfbIAn803LDGXS9

# >>> response.request.headers['Accept-Encoding']
# 'gzip, deflate'

# >>> response.ok
# True
# >>> response.status_code
# 200

# response = requests.get(url)
# if not response.ok:
#     raise Exception("GET failed with status code {}".format(response.status_code))

# response = requests.get(url)
# response.raise_for_status()

# >>> p = {"search": "grey kitten",
# ...      "max_results": 15}
# >>> response = requests.get("https://example.com/path/to/api", params=p)
# >>> response.request.url
# 'https://example.com/path/to/api?search=grey+kitten&max_results=15'

# >>> p = {"description": "white kitten",
# ...      "name": "Snowball",
# ...      "age_months": 6}
# >>> response = requests.post("https://example.com/path/to/api", data=p)

# >>> response.request.url
# 'https://example.com/path/to/api'

# >>> response.request.body
# 'description=white+kitten&name=Snowball&age_months=6'