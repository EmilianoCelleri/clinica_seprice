from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

def medico_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not hasattr(request.user, 'medico'):
            return redirect('permiso_denegado')
        return view_func(request, *args, **kwargs)
    return _wrapped_view