from django import forms

class classform(forms.Form):
    namac = forms.CharField()
    alamatc = forms.CharField()

def Form(request):
    classform = forms.classform()
    
    context = {
        'heading' : 'Home',
        'classform' : classform
    }
    
    if request.method == 'POST':
        print("ini adalah method post")
        context['nama'] = request.POST['nama']
        context['alamat'] =  request.POST['alamat']
        context['namac'] = request.POST['namac']
        context['alamatc'] = request.POST['alamatc']
    else:
        print("ini adalah method get")
    return render(request, 'form.html', context)
    
