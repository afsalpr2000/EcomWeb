from django.utils.deprecation import MiddlewareMixin

class NoCacheMiddleware(MiddlewareMixin):
    def process_response(self,request,response):
        if request.user.is_authenticated:
            response['Cache_control'] = 'no cache,no store,must revalidate'
            response['pragma'] = 'no-cache'
            response['Expires'] = '0'
        return response