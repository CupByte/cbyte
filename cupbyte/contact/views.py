from django.shortcuts import render
from .models import Feedback
from .feedback_form import FeedbackForm
from django.http import HttpResponse

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Form Submitted")
    else:
        form = FeedbackForm()
    return render(request, 'contact/contact.html', {'form':form})

# def feedback(request):
    
#     return render(request, 'contact/contact.html', {'form':form})
        

