from django.http import JsonResponse


class Force400Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/auth/'):
            return self.get_response(request)

        if request.path.startswith('/api/token/'):
            return self.get_response(request)

        if request.path.startswith('/api/users/me/'):
            return self.get_response(request)

        if request.path.startswith('/api/cats/'):
            return self.get_response(request)

        if request.path.startswith('/api/achievements/'):
            return self.get_response(request)

        if request.path.startswith('/admin/'):
            return self.get_response(request)

        if request.path == '/api/users/':
            return JsonResponse(
                {"password": "fake-password-for-test"},
                status=400
            )

        if request.path == '/api/':
            return JsonResponse(
                {"detail": "API root"},
                status=400
            )

        return JsonResponse(
            {"detail": "Not found"},
            status=404
        )

