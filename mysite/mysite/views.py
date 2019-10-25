from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import datetime

# @require_http_methods(["GET"])
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def year_archive(request, year):
    now = datetime.datetime.now()
    html = "<html><body>It is now year %d.</body></html>" % year
    return HttpResponse(html)

def month_archive(request, year, month):
    now = datetime.datetime.now()
    html = "<html><body>It is now month %d, year %d.</body></html>" % (month, year)
    return HttpResponse(html)

def article_detail(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now article_detail.</body></html>"
    return HttpResponse(html)
