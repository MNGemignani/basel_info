from django.shortcuts import render

def home(request):
    context = {
        "carousel_images": [f"img/basel_images/image{i}.jpg" for i in range(1, 6)],
    }
    return render(request, "core/home.html", context)

def history(request):
    context = {
        
    }
    return render(request, "core/history.html", context)

def university(request):
    context = {
        
    }
    return render(request, "core/university.html", context)
