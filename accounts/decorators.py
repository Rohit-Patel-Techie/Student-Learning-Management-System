# Role Base Access Decorators
from django.core.exceptions import PermissionDenied

def instructor_required(view_func) : 
    def wrapper(request, *args, **kwargs) : 
        if request.user.is_authenticated and request.user.is_instructor() : 
            return view_func(request, *args, **kwargs)
        
        return wrapper
