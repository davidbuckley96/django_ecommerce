from .models import Order, Category


def order(request):
    try:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        return {'order': order}
    except:
        return {'order': None}


def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}