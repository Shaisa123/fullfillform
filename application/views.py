from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


from django.shortcuts import render

def index(request):
    return render(request, 'base.html')  # Replace 'index.html' with your template name


class SigninView(View):
    def get(self, request):
        return render(request, 'signin.html')

    def post(self, request):
        # Handle form submission logic here
        return HttpResponse('Signin form submitted')  # Example response

class SignupView(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        # Handle form submission logic here
        return HttpResponse('Signup form submitted')  # Example response
