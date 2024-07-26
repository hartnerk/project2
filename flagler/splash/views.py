from django.shortcuts import render
from .forms import SubscriberForm
from .models import MailingList
# Create your views here.
def splash(request):
	subscriberform = SubscriberForm(request.POST)
	if request.method == 'POST':
		if subscriberform.is_valid():
			ml = MailingList(
			    name = subscriberform.cleaned_data['name'],
			    email = subscriberform.cleaned_data['email'],  
			    message = subscriberform.cleaned_data['message']
			)
			ml.save()
		else:
			subscriberform = SubscriberForm()
	return render(request, 'index.html', {'subscriberform': subscriberform})
