from django.http import HttpResponse
import subprocess

# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def health(request):
    return HttpResponse("200")

def metadata(request):
    text=subprocess.run(["git", "status"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    return HttpResponse(text.stdout)
