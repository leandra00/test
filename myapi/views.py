from django.http import HttpResponse, JsonResponse
import subprocess
import json
import pkg_resources

# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def health(request):
    return HttpResponse("http status = 200", status=200)

def metadata(request):
    gitshar=subprocess.run(["git", "rev-parse", "HEAD"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    metadata={
        'version': '1.0',
        'description': 'my description',
        'lastgitshar': gitshar.stdout
    }
    return JsonResponse(metadata)
