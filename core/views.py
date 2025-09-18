from django.shortcuts import render

def home(request):
    context = {
        "basel_history": (
            "Basel, located on the Rhine at the tripoint of Switzerland, France, and Germany, "
            "has a documented history dating back to the Roman era. It became a significant "
            "medieval trade and cultural center, later flourishing with humanism and printing."
        )
    }
    return render(request, "core/home.html", context)

def university(request):
    context = {
        "uni_history": (
            "The University of Basel (founded 1460) is Switzerland’s oldest university. "
            "It has been home to notable scholars across theology, medicine, and the humanities, "
            "and today is a leading research university with strong ties to life sciences."
        )
    }
    return render(request, "core/university.html", context)
