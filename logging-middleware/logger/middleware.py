import logging
from .logger import Logger

ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJoc3ZpamF5MjY0NzM3QGdtYWlsLmNvbSIsImV4cCI6MTc4MjUzOTc1OCwiaWF0IjoxNzgyNTM4ODU4LCJpc3MiOiJBZmZvcmQgTWVkaWNhbCBUZWNobm9sb2dpZXMgUHJpdmF0ZSBMaW1pdGVkIiwianRpIjoiNTJhNmQxY2YtN2U3NS00MzcwLWI1NTYtYjhjN2Q0NTliZWY4IiwibG9jYWxlIjoiZW4tSU4iLCJuYW1lIjoiaCBzIHZpamF5Iiwic3ViIjoiM2YzN2VkYzItYWUzNi00ZWU5LWJhZDctMDNmNmUwMjc5MzRkIn0sImVtYWlsIjoiaHN2aWpheTI2NDczN0BnbWFpbC5jb20iLCJuYW1lIjoiaCBzIHZpamF5Iiwicm9sbE5vIjoiMjVocjFmMDAxMyIsImFjY2Vzc0NvZGUiOiJhVGt5YnMiLCJjbGllbnRJRCI6IjNmMzdlZGMyLWFlMzYtNGVlOS1iYWQ3LTAzZjZlMDI3OTM0ZCIsImNsaWVudFNlY3JldCI6IlRCellzSEVoUXpTd2RHRFIifQ.pQIHEN9k_JCgSqCEFAWe723T1fdcoWWiB50im82Y27I"


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = Logger(ACCESS_TOKEN)

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        try:
            self.logger.log(
                stack="backend",
                level="error",
                package="middleware",
                message=str(exception)
            )
        except Exception as log_error:
            logging.error(f"Logging failed: {log_error}")

        return None