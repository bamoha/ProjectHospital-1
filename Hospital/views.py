from django.shortcuts import render


def index(request):
    return render(request, 'Hospital/index.html')


def about(request):
    return render(request, 'Hospital/about.html')


def mission(request):
    return render(request, 'Hospital/mission.html')


def vision(request):
    return render(request, 'Hospital/vision.html')


def book(request):
    return render(request, 'Hospital/contact.html')


def burns(request):
    return render(request, 'Hospital/burns.html')


def medical(request):
    return render(request, 'Hospital/medical.html')


def surgery(request):
    return render(request, 'Hospital/surg.html')



def ortho(request):
    return render(request, 'Hospital/ortho.html')



def therapy(request):
    return render(request, 'Hospital/physical.html')


def complaint(request):
    return render(request, 'Hospital/contact.html')


def enquiry(request):
    return render(request, 'Hospital/contact.html')


def contact(request):
        return render(request, 'Hospital/contact.html')


def careers(request):
        return render(request, 'Hospital/careers.html')


