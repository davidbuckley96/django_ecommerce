from .models import Order


def order(request):
    try:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        return {'order': order}
    except:
        return {'order': None}
