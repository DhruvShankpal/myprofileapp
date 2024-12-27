from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import git
import subprocess
import os
import requests

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
    print("this message should be printed before")
    username = 'dhruvshankpal'
    token = '865e11f353b89296a61344e07574505d77708e66' #pythonanywhere API token
    domain_name = "dhruvshankpal.pythonanywhere.com"
    response = requests.post(
        'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/'.format(
            username=username, domain_name=domain_name
        ),
        headers={'Authorization': 'Token {token}'.format(token=token)}
    )
    print("this message should be printed after")
    if response.status_code == 200:
        print('reloaded OK')
    else:
        print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
    print("last msg before return!")
    return HttpResponse("Hello World5!")