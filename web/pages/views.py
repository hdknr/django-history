from django.shortcuts import render

# Create your views here.

def page_detail(request, name):
    template_names = [
        f'pages/page/{name}.html',
        f'pages/page/default.html',
    ]
    return render(request, template_names, context={})