from django.shortcuts import render

def index(request):

    forum_title = "Forentitel"
    forum_url = "http://forum.django.local/"


    context = {
        "title": forum_title,
        "forum_url": forum_url
    }

    return render(request, "index.html", context)

