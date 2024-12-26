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
    repo = git.Repo('/home/dhruvshankpal/myprofile/myprofileapp')
    repo.remotes.origin.pull()
    # python manage.py collectstatic --noinput
    # subprocess.run(["cd", "/home/dhruvshankpal/myprofile"])
    os.chdir("/home/dhruvshankpal/myprofile")
    subprocess.run(["python", "manage.py", "collectstatic", "--noinput"], cwd='/home/dhruvshankpal/myprofile')
    return HttpResponse("Hello World5!")