from django.shortcuts import render, HttpResponse

# Create your views here.
def test_landing(request):
    return HttpResponse("Test for Httpresponce !")
