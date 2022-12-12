from collections import defaultdict

from django.http.response import HttpResponse


class RateLimiterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.client_requests = defaultdict(int)
        # One-time configuration and initialization.

    def __call__(self, request):
        # Set the maximum number of requests allowed per minute
        max_requests = 100

        # Get the client's IP address and port
        client_key = f"{request.META['REMOTE_ADDR']}:{request.META['SERVER_PORT']}"

        # Increment the number of requests made by the client
        self.client_requests[client_key] += 1

        # Check if the client has exceeded the maximum number of requests
        if self.client_requests[client_key] > max_requests:
            # If the client has exceeded the maximum number of requests, return a 429 (Too Many Requests) response
            return HttpResponse(status=429)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
