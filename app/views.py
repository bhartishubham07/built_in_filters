from django.shortcuts import render

# Create your views here.


def built_in_filters(request):
    
    import datetime
    date = datetime.datetime.now()
    
    data = 'hI hOw ArE yoU'
    return render(request, 'built_in_filters.html', {'data':data, 'date':date, 'c':0})