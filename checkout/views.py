from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key':'pk_test_51HQvm3EarIIOun9hKr65z3oRWNiDBIZRGdlLrEMOUjiYRRy7XfhXxdsvKU1O2lS41etFnwlXQjpxcOGg7m2Q9O8X00vsHHlmbc',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)