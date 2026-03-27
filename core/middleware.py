from django.shortcuts import render


class ForceCustom404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Exception:
            return render(request, '500.html', status=500)

        # Always use the custom 404 page, even when DEBUG=True.
        if response.status_code == 404:
            return render(request, '404.html', status=404)

        if response.status_code == 500:
            return render(request, '500.html', status=500)

        return response
