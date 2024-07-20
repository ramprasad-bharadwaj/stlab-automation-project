from django.shortcuts import render, HttpResponse
from django.http import FileResponse

# Create your views here.

def index(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        pw = request.POST.get('password')
        no = list(range(1, 6))
        if (un == "ram" and pw == 'ram123') or (un == "admin" and pw == 'admin') or (un == "lab-demo" and pw == 'stlab'):
            # return HttpResponse("<h1><center>Done!</center></h1>")
            return render(request, 'main.html', {'no':no})
        else:
            return HttpResponse("<h1><center>Incorrect Username or Password</center></h1>")
    else:
        return render(request, 'index.html')
    
def download_pdf(request, mod_no):
    file_name = f'mod{mod_no}.pdf'
    file_path = f'static/{file_name}'
    return FileResponse(open(file_path, 'rb'), as_attachment=True)