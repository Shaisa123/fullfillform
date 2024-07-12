from django.shortcuts import render, redirect
from .form import LoginForm

def sign_up(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')  # Replace 'products' with your products page URL name
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def products_view(request):
    # Add logic to display products
    return render(request, 'products.html')
