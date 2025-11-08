from django.http import HttpResponse



def home_page(request: HttpResponse):
    return HttpResponse(
        f'<h1>Welcome to the Django_App<h1>'
    )

def greetings(request, user_name):
    return HttpResponse(
        f'<h1>Hello, {user_name}<h1>'
    )