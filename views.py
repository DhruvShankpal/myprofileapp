from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import git
import subprocess
import os

# Create your views here.
def home(request):
    # return HttpResponse("Hello World!")
    return render(request, 'base.html')

@csrf_exempt
def update_webhook(request):
    # function to handle webhook push from github
    # one more comment added
    repo = git.Repo('/home/tanishashankpal/myprofile/myapp')
    repo.remotes.origin.pull()
    # python manage.py collectstatic --noinput
    # subprocess.run(["cd", "/home/tanishashankpal/myprofile"])
    os.chdir("/home/tanishashankpal/myprofile")
    subprocess.run(["python", "manage.py", "collectstatic", "--noinput"], cwd='/home/tanishashankpal/myprofile')
    return HttpResponse("Hello World5!")