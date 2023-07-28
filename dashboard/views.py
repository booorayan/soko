from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from items.models import Item

# Create your views here.


@login_required
def dashboard(request):
    items = Item.objects.filter(created_by=request.user)

    context = {
        'items': items
    }

    return render(request, 'dashboard.html', context)
