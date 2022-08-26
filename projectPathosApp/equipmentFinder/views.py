import copy

from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse
from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import equipSearchForm, addEquipmentForm, addEquipmentFormDoc
from .models import addEquipmentClass
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.views.generic.edit import FormView



def searchPage(request):
    filesList = []
    equipID = request.POST.get('searchTag')

    if request.method == 'POST':
        form = equipSearchForm(request.POST)
        if form.is_valid():
            equipInfo = addEquipmentClass.objects.get(tagID=equipID)
            equipImage1 = equipInfo.equipImage.name.strip('][').strip('\'')
            equipImage = equipImage1
            print(equipImage)

            equipfiles = equipInfo.equipFile.name
            print(equipfiles)

            equiplocation = equipInfo.equipLocation
            print(equiplocation)

            #HANDLE FILE STRING CONVERTING THEM TO LIST
            filesList = list(equipfiles.split("$,"))
            filesList.pop()
            print(filesList)




        return render(request, 'searchResult.html', {'title': equipInfo.tagID, 'equipImage':equipImage, 'equipFiles':filesList,'equipLocation':equiplocation, 'equipName':equipInfo.equipName})

    else:
        form = equipSearchForm()
    return render(request, 'equipSearch.html', {'title': 'EQUIPMENT LOCATOR', 'form': form})


def addEquipmentPage(request):
    # List for storing files and photo names to be stored in mysql Database

    photoList = []
    newDocFiles = []

    form1 = addEquipmentForm(request.POST, request.FILES)
    form2 = addEquipmentFormDoc(request.POST, request.FILES)

    # extract files and images from submitted and store in represented variables.
    files = request.FILES.getlist('equipFile')
    photos = request.FILES.getlist('equipImage')

    # extract tagID from submitted form and stored in represented variable.
    tagID = request.POST.get('tagID')


    # action carried out when client submits form
    if request.method == 'POST':

        while request.method == 'POST' and form2.is_valid() and not form1.is_valid():
            docFiles = files

            if newDocFiles != docFiles:
                newDocFiles = copy.copy(docFiles)
                for f in newDocFiles:
                    with open(
                            '/Users/TryingNerd24/Documents/Personal Projects/Coding/Webpage Development/projectPathos/projectPathosApp/projectPathosApp/media/equipDocs/' + str(
                                f), 'wb+') as destination:
                        for chunk in f.chunks():
                            destination.write(chunk)

        # stores data to database once form1 and form2 is valid and the tag ID does not exist in the database. Ensuring validity and preventing repetability.
        if form1.is_valid() and len(addEquipmentClass.objects.filter(tagID=tagID)) <= int(0):
            filesWebArray = request.POST["filesArray"]


            print("filesWebArray: "+filesWebArray)
            print(type(filesWebArray))
            # filesBinary = request.POST["filesArrayBinary"]

            # newFiles = "\""+files+"\""
            newFiles = filesWebArray.replace('$,,', '$,')
            print("newFiles: " + newFiles)


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
            addEquipmentClass.objects.filter(tagID=tagID).update(equipFile=newFiles, equipImage=photoList)
            return HttpResponseRedirect('#')
    else:
        form1 = addEquipmentForm()
        form2 = addEquipmentFormDoc()
    return render(request, 'addEquipment.html', {'title': 'ADD EQUIPMENT', 'form': form1, 'form1': form2})


def searchResultsPage(request):

    return render(request, 'searchResult.html', {'title': 'EQUIPMENT LOCATOR'})