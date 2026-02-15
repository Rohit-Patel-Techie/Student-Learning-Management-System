#Protect Dashboard by Role
from django.core.exceptions import PermissionDenied

class StudentRequiredMixin: 
    """Student checking """
    def dispatch(self,request, *args, **kwargs) : 
        if not request.user.is_student() :
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

        
class InstructorRequiredMixin: 
    """Instructor Checking"""
    def dispatch(self,request, *args, **kwargs) : 
        if not request.user.is_instructor() :
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
