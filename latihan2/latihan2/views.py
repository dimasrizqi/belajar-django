from django.http import HttpResponse

def index(resquest):
    return HttpResponse("<h1> ini adalah Home</h1>")

def about(resquest):
    return HttpResponse("<h1> ini adalah About</h1>")
