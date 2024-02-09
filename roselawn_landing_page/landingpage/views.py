from django.shortcuts import render

landingpage_html = 'landingpage/home.html'
def home(request):
    return render(request, landingpage_html)