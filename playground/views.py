from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem


def say_hello(request):
    """
    function for say hello 
    """


    context = {'name': 'Joel', 'tags': list(queryset)}
    return render(request, 'hello.html', context)  