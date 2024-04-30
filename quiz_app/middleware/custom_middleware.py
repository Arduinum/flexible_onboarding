from django.shortcuts import redirect


class CheckPageNotFound:
    """Проверяет существует ли url и если нет 404"""
    
    def __init__(self, response):
        self.response = response

    def __call__(self, request):
        """вызов для каждого запроса"""
        
        response = self.response(request)

        if response.status_code == 404:
            return redirect('quiz_app:page404')
        return response
