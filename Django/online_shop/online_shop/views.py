#  coding = utf-8
from django.http import HttpResponse
# print hello world


def index_view(request):
    return HttpResponse('hello world')
