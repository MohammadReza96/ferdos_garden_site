from django.shortcuts import render
from django.core.files.storage import FileSystemStorage # this class has some methods like exists(value) or open(file)
from django.http import HttpResponse,HttpResponseNotFound
from django.template.loader import render_to_string
from .models import Place,Ticket,VisitorType,Rule
from django.core.paginator import Paginator


#---------------------------------------------------------------------------------------- view for history page
def ferdos_history(request):
    return render (request,'place/ferdos_history.html')

#---------------------------------------------------------------------------------------- view for places page
def show_places(request):
    data=Place.objects.all()
    pagenator=Paginator(data,4)
    page_number=request.GET.get('page')
    page_object=pagenator.get_page(page_number)
    return render(request,'place/places.html',{'page_obj':page_object})

#---------------------------------------------------------------------------------------- view for place page
def show_place(request):
    pass
#---------------------------------------------------------------------------------------- view for rule&price page
def show_rules_prices(request):
    # rules=Rule.objects.all()
    tickets=Ticket.objects.all().order_by('place')
    place_1=[]
    place_2=[]
    place_3=[]
    place_4=[]
    place_5=[]
    place_6=[]
    place_7=[]
    place_8=[]
    for obj in tickets:
        if obj.place.id==1:
            place_1.append(obj)
        elif obj.place.id==2:
            place_2.append(obj)
        elif obj.place.id==3:
            place_3.append(obj)
        elif obj.place.id==4:
            place_4.append(obj)
        elif obj.place.id==5:
            place_5.append(obj)
        elif obj.place.id==6:
            place_6.append(obj)
        elif obj.place.id==7:
            place_7.append(obj)
        else:
            place_8.append(obj)

    
    context={
        'place_1':place_1,
        'place_2':place_2,
        'place_3':place_3,
        'place_4':place_4,
        'place_5':place_5,
        'place_6':place_6,
        'place_7':place_7,
        'place_8':place_8
    }   
    return render(request,'place/rule_price.html',context)
    
#---------------------------------------------------------------------------------------- view for downloading file
def ferdos_path_garden(request,filename):
    file=FileSystemStorage() # start path is media
    file_name=f'pdf/{filename}'
    if file.exists(file_name):
        with file.open(file_name) as pdf:
            response=HttpResponse(pdf,content_type='application/pdf')
            response['content-Disposition']=f"attachment;filename={filename}"
            return response
    else:
        context={}
        content=render_to_string(
            '404/404.html',
            context,
            request
        )
        return HttpResponseNotFound(content)