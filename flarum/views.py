from django.shortcuts import render
import requests

import json
from django.conf import settings

def index(request):

    forum_title = "Forentitel"
    forum_url = "http://forum.django.local/"

    url = "http://forum.django.local/api/forum"
    headers = {'content-type': 'application/vnd.api+json'}

    session = requests.Session()
    session.trust_env = False

    response = session.get(url=url, headers=headers)

    context = {
        "title": forum_title,
        "forum_url": forum_url,
        "api_result": response.text
    }

    return render(request, "index.html", context)

