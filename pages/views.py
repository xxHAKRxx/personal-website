from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("This is a test to make sure HTTP responses are working.")