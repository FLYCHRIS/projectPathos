from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render,redirect
from django.shortcuts import render
from .forms import equipSearchForm, addEquipmentForm, addEquipmentFormDoc
from .models import addEquipmentClass
from django.views.generic.edit import FormView

def searchPage(request):
    if request.method == 'POST':
        form = equipSearchForm(request.POST)
        if form.is_valid():
            print(form)

        return HttpResponseRedirect('#')

    else:
        form = equipSearchForm()
    return render(request, 'equipSearch.html', {'title': 'EQUIPMENT LOCATOR', 'form':form})

def addEquipmentPage(request):
    # List for storing files and photo names to be stored in mysql Database
    fileList = []
    photoList = []

    # action carried out when client submits form
    if request.method == 'POST':
        # stores FILES and POST data from forms on webpage
        form1 =addEquipmentForm(request.POST, request.FILES)
        form2 =addEquipmentFormDoc(request.POST, request.FILES)

        # extract files and images from submitted and store in represented variables.
        files = request.FILES.getlist('equipFile')
        photos = request.FILES.getlist('equipImage')
        # extract tagID from submitted form and stored in represented variable.
        tagID = request.POST.get('tagID')

        # stores data to database once form1 and form2 is valid and the tag ID does not exist in the database. Ensuring validity and preventing repetability.
        if form1.is_valid() and form2.is_valid() and len(addEquipmentClass.objects.filter(tagID=tagID)) <= int(0):

            # adds files name to fileList and stores the fiels to the MEDIA location where the app stores files on system.
            for f in files:
                fileList.append(str(f))
                with open(
                        '/Users/TryingNerd24/Documents/Personal Projects/Coding/Webpage Development/projectPathos/projectPathosApp/projectPathosApp/media/equipDocs/' + str(
                                f), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
            # adds photos name to photoList and stores the photos to the MEDIA location where the app stores photos on system.
            for p in photos:
                photoList.append(str(p))
                with open(
                        '/Users/TryingNerd24/Documents/Personal Projects/Coding/Webpage Development/projectPathos/projectPathosApp/projectPathosApp/media/equipImages/' + str(
                                p), 'wb+') as destination:
                    for chunk in p.chunks():
                        destination.write(chunk)
            form1.save()

            # adds fileList and photoList to saved field in database. Field located via tagID.
            addEquipmentClass.objects.filter(tagID=tagID).update(equipFile=fileList, equipImage=photoList)
            return HttpResponseRedirect('#')
    else:
        form1 = addEquipmentForm()
        form2 = addEquipmentFormDoc()
    return render(request, 'addEquipment.html', {'title': 'ADD EQUIPMENT', 'form':form1, 'form1':form2})

