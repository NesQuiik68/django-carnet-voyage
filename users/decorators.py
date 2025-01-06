from django.shortcuts import redirect
from django.http import HttpResponseForbidden

def login_required_custom(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.isLoggedIn:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Vous devez être connecté pour accéder à cette page.")
    return wrapper
