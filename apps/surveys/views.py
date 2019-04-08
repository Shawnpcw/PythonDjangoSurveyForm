from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'surveys/index.html')
    
def create(request):
    if request.method == "POST":
        if 'submits' not in request.session:
            request.session['submits'] = 1
        else:
            request.session['submits'] +=1   
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['comment'] = request.POST['comments']
        return redirect('/result')

    return redirect('/result')

def result(request):

    

    return render(request,'surveys/result.html')

# Create your views here.
