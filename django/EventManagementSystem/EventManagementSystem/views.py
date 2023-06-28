from  django.http import HttpResponse,JsonResponse
def home_page(request):
    print("home page requested")
    freinds=["harshu","neelu","neha"]
    return JsonResponse(freinds,safe=False) 