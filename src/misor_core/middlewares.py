import logging

logger = logging.getLogger("misor")

class TestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the request path
        logger.debug(f"Request path: {request.path}")

        # Call the next middleware or view
        response = self.get_response(request)

        # Log the response status code
        logger.debug(f"Response status: {response.status_code}")
        

        return response
