from django.shortcuts import render, redirect

# Create your views here.


def view_shopbag(request):
    """ View for shop bag """

    return render(request,'shopbag/shopbag.html')

def add_to_bag(request, item_id):
    """ Add quantity to a product """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
    
    request.session['bag'] = bag
    return redirect(redirect_url)