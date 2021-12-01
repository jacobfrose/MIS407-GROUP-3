from django.shortcuts import render
from user_profile.models import User

def user_profile(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'user_profile.html', context)