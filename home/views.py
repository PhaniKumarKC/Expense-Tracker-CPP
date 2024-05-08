import sys
from django.shortcuts import render
from django.shortcuts import render
from Mquote.Mquote import generate_quote

print(sys.executable)
# the home page
def home(request):
    token = generate_quote()
    print(token)
    return render(request, "homePage/index.html", {'token': token})
   