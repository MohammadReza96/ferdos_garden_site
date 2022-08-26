from django.shortcuts import render
from .models import Place,Ticket_price
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from django.http import (HttpResponseRedirect,HttpResponsePermanentRedirect,
                         HttpResponseNotFound,HttpResponseBadRequest,HttpResponse,
                         HttpResponseForbidden,HttpResponseServerError)






#----------------------------------------------------------------------------
def show_garden_parts(request):
    places=Place.objects.all()
    context={
        'places':places
    }
    return render(request,'places_app/garden_parts.html',context)
#----------------------------------------------------------------------------
def show_garden_part(request,id):
    try:
        place=Place.objects.get(id=id)
        context={
            'place':place
        }
        return render(request,'places_app/garden_part.html',context)
    except:
        context={}
        content=render_to_string(
            'error_page.html',
            context,
            request
        )
        return HttpResponseNotFound(content)
#----------------------------------------------------------------------------
def download_path_garden(request):
    file=FileSystemStorage()
    file_name="pdf/ferdos_garden_routh.pdf"
    if file.exists(file_name):
        with file.open(file_name) as pdf:
            response=HttpResponse(pdf,content_type="application/pdf")
            response['content-Disposition']="attachment;filename=ferdos_garden_routh.pdf"
            return response
    else:
        context={}
        content=render_to_string('error_page.html',context,request)
        return HttpResponseNotFound(content)
    
#----------------------------------------------------------------------------
def show_plans_rules(request):
    place=Place.objects.all()
    price=Ticket_price.objects.all()
    context={
        "place":place,
        "price":price
    }
    return render(request,'rules/rules.html',context)
    