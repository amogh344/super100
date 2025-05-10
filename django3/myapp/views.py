from django.shortcuts import render
from .forms import ContactForm

users = [
    {'name': 'Amogh', 'age': 21},
    {'name': 'Brahma', 'age': 21},
    {'name': 'joe goldberg', 'age': 21},
]

cards = [
    {'title': 'Personal', 'description': 'This is a personal plan', 'original_price': 100, 'updated_price': 110},
    {'title': 'Starter', 'description': 'This is a Starter plan', 'original_price': 100, 'updated_price': 50},
    {'title': 'Advanced', 'description': 'This is an Advanced plan', 'original_price': 100, 'updated_price': 1110},
]

def greet(request):
    return render(request, 'greet.html', {'users': users})

def landing_page_view(request):
    return render(request, 'landingpage.html')

def pricing_page_view(request):
    return render(request, 'pricingPage.html', {'cards': cards})

def contact_page_view(request):
    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            # Here you can add logic to handle the form submission (e.g., saving or sending an email)
            print("Your request is recorded")
        else:
            print("Your request is not recorded")
    else:
        f = ContactForm()
    return render(request, 'contact.html', {'form': f})