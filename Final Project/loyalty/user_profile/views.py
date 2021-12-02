from django.shortcuts import render
from user_profile.models import User

def user_profile(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'user_profile.html', context)
def user_profile_promotion(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'user_profile_promotion.html', context)
def user_profile_redemption(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'user_profile_redemption.html', context)
def login(request):
    return render(request, 'login.html', {})
