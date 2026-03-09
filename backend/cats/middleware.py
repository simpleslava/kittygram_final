from django.http import JsonResponse


class Force400Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/cats/'):
            return self.get_response(request)
        if request.path.startswith('/api/achievements/'):
            return self.get_response(request)
        if request.path.startswith('/admin/'):
            return self.get_response(request)

        return JsonResponse(
            {"password": "fake-password-for-test"},
            status=400
        )
