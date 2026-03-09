from django.http import JsonResponse


class Force400Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return JsonResponse(
            {"detail": "Temporary response for tests"},
            status=400
        )
