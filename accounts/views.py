from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse


# Create your views here.

@api_view(['GET'])
def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    User.objects.get(username=username)
    
    context = {
        'person': person,
    }
    print('ㅇㅅㅇ',context)
    return JsonResponse(context)


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        me = request.user
        you = User.objects.get(pk=user_pk)
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                is_followed = False
            else:
                you.followers.add(me)
                is_followed = True
            context = {
                'is_followed': is_followed,
                'followers_count': you.followers.count(),
                'followings_count': you.followings.count(),
            }
            return JsonResponse(context)
    context = {}
    return JsonResponse(context)
