from .models import Order, Category
from django.conf import settings


def order(request):
    try:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        return {'order': order}
    except:
        return {'order': None}


def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}


def default_image_url(request):
    return {'default_image_url': f'{settings.STATIC_URL}placeholder_product.jpg'}