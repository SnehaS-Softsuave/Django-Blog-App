from django.shortcuts import render

def custompage_not_found(request,exception):
    return render(request, '404_page.html', status=404)