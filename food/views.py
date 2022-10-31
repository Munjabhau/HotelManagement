from django.shortcuts import render, redirect
from food.models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import random
import json


# Create your views here.
def randomOrderNumber(length):
    sample = 'ABCDEFGH0123456789'
    numberO = ''.join((random.choice(sample) for i in range(length)))
    return numberO


def chinese(request):
    request.session.set_expiry(0)
    chines = Chinese.objects.all()
    context = {'chines': chines}
    return render(request, 'food/chinese.html', context)


@csrf_exempt
def order(request):
    request.session.set_expiry(0)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        request.session['note'] = request.POST.get('note')
        request.session['order'] = request.POST.get('orders')
        orders = json.loads(request.session['order'])
        request.session['total'] = request.POST.get('total')
        randomNum = randomOrderNumber(6)

        while Order.objects.filter(number=randomNum).count() > 0:
            randomNum = randomOrderNumber(6)

        if request.user.is_authenticated:
            order = Order(customer=request.user,
                          number=randomOrderNumber(6),
                          bill=float(request.session['total']),
                          note=request.session['note'])
            order.save()
            request.session['orderNum'] = order.number
            for article in orders:
                item = Item(
                    order=order,
                    name=article[0],
                    price=float(article[2]),
                    size=article[1]
                )
                item.save()
    return render(request, 'food/order.html')


def success(request):
    request.session.set_expiry(0)
    orderNum = request.session['orderNum']
    bill = request.session['total']
    items = Item.objects.filter(order__number=orderNum)
    ctx = {'orderNum': orderNum, 'bill': bill, 'item': items}
    return render(request, 'food/success.html', ctx)
