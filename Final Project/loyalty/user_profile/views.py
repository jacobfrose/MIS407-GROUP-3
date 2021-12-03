from django.shortcuts import render
from user_profile.models import User

def user_profile(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user
    }
    if int(user.pointsearned) >= 50000:
        return render(request, 'user_profile_elite.html', context)
    elif int(user.pointsearned) >= 10000:
        return render(request, 'user_profile_lowelite.html', context)
    elif int(user.pointsearned) >= 1500:
        return render(request, 'user_profile_high.html', context)
    else:
        return render(request, 'user_profile_low.html', context)
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

def login_request(request):
    username = request.POST.get("username","")
    password = request.POST.get("password","")

    if User.objects.filter(username=username, password=password).exists():
        user = User.objects.get(username=username, password=password)
        context = {
            'user': user
        }
        if int(user.pointsearned) >= 50000:
            return render(request, 'user_profile_elite.html', context)
        elif int(user.pointsearned) >= 10000:
            return render(request, 'user_profile_lowelite.html', context)
        elif int(user.pointsearned) >= 1500:
            return render(request, 'user_profile_high.html', context)
        else:
            return render(request, 'user_profile_low.html', context)
    else:
        return render(request, 'login_failed.html', {})
