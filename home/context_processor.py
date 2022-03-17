from order.models import ShopCart


def cartcount(request):
    # current_user = request.user
    cartcount = ShopCart.objects.filter(order_placed=False).filter(user__username=request.user.username)
    total_quantity = 0
    for item in cartcount:
        total_quantity += item.quantity

    context = {'itemcount':total_quantity}
    return context