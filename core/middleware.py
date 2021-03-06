from django.conf import settings
from django.shortcuts import redirect

class LoginRequiredMiddleware(object):
    
    def process_request(self, request):
        EXEMPT_URLS = []
        if hasattr(settings, 'LOGIN_EXEMPT_URLS'):            
            EXEMPT_URLS = [expr for expr in settings.LOGIN_EXEMPT_URLS]
            
        assert hasattr(request, 'user')
        path = request.path_info.strip('/')
        
        if path in EXEMPT_URLS:
            return
            
        if not request.user.is_authenticated():            
            return redirect('/login?next=%s' % request.path)