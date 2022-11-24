from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from store.models import Product
from .basket import Basket

def basket_summary(request):
    return render(request, 'store/basket/summary.html')

def basket_add(request):
# getting information from AJAX script in single.html
#  matches action and productid from there too
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
            # compact alternative to the following code:
            # try:
            #     product = Product.objects.get(id=product_id)
            # except:
            #     raise Http404
        basket.add(product=product)
        response = JsonResponse({'test':'data'})
        return response

