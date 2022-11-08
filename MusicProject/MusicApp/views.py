from http.client import HTTPResponse
from django.http import JsonResponse, request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Audio
from .models import Document
from .forms import DocumentForm
from django.contrib import messages
from MusicApp.produce_mfcc import process_input
from MusicApp.predict import predict
import numpy as np

# Create your views here.

def index(request):
    return render(request,'home.html')

def classify(request):
    return render(request,'classify.html')

def category(request):
    audi = Audio.objects.all()
    return render(request,'category.html',{'audi':audi})

def about(request):
    return render(request,'about.html')

def result(request):
        #my_model = keras.models.load_model('model\Music_Genre_10_CNN.h5')
        
    return render(request,'result.html')

def file_upload_view(request):
    #print(request.FILES)
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        #print(my_file)
        Audio.objects.create(name=my_file.name,upload=my_file)
        return HttpResponse('')
    return JsonResponse({'error':'Please upload a file'})

def Edit(request):
    audi = Audio.objects.all()

    context = {
        'audi':audi
    }
    return redirect(render, 'category.html', context)

def Update(request,audio_id):
    if request.method == 'POST':
        audio_id = request.POST.get('audio_id')
        name = request.POST.get('name')

        audi = Audio(
            audio_id = audio_id,
            name = name,
        )
        audi.save()
        return redirect('category')
    return redirect(render, 'category.html')


def Delete(request,audio_id):
    audi = Audio.objects.filter(audio_id=audio_id)
    audi.delete()
    context = {
        'audi':audi
    }
    return redirect('category')

def model_form_upload(request):
    documents = Document.objects.all()
    if request.method == 'POST':
        if len(request.FILES) == 0:
            messages.error(request,'Upload a file')
            return redirect("home")

        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            uploadfile = request.FILES['document']
            print(uploadfile.name)
            print(uploadfile.size)
            if not uploadfile.name.endswith('.wav'):
                messages.error(request,'Only .wav file type is allowed')
                return redirect("home")
            track_duration =  30   
            new_input_mfcc= process_input(uploadfile,track_duration)  
            X_to_predict = new_input_mfcc[np.newaxis, ..., np.newaxis]
            print(X_to_predict.shape) 
            genre = predict(X_to_predict)
            print(genre)

            context = {'genre':genre}
            return render(request,'result.html',context)

    else:
        form = DocumentForm()

    return render(request,'result.html',{'documents':documents,'form':form})

def handle_not_found(request,exception):
    return render(request, 'not-found.html')