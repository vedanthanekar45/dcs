from django.http import JsonResponse

def get_greetings (request):
    name = request.GET.get('name', 'World')

    response_data = {
        "greeting": f"Hello {name}",
        "server_status": "OK"
    }

    return JsonResponse(response_data)