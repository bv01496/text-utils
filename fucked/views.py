#i ahv created ths file
from django.shortcuts import render

def index(request):
    return render(request, 'temp.html')
def analize(request):
    djtext = request.POST.get('tb', 'default')
    checkb = request.POST.get('checkb', 'default')
    incaps = request.POST.get('incaps', 'default')
    new_line_remove = request.POST.get('new_line', "default")
    analized = ""
    if checkb == "on":
        analized = ""
        punctuations = ("""?/)[]{}"'',.(&@#$%^&*(+=""")
        for char in djtext:
            if char not in punctuations:
                analized += char
        djtext = analized
    if incaps == "on":
        analized = ""
        for char in djtext:
             analized += char.upper()
        djtext = analized
    if new_line_remove == "on":
        analized = ""
        for char in djtext:
            if char != "/n":
                analized += char
    params = {'analized_list': analized}
    return render(request, 'page2.html', params)
def about_us(request):
    return render(request, 'about_us.html')
# def nlr(request):
#     return HttpResponse('new line removed <a href="http://127.0.0.1:8000/">back button</a>')