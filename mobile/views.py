from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def mobile(request):
    return render (request, 'mobile/appshell.html')


