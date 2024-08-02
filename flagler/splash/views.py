
from django.shortcuts import render
from .forms import FeedbackForm
from .models import SurveyQuestion, SurveyAnswer
import random
# Create your views here.
def splash(request):
	questionnumber = random.randrange(1,4)
	surveyquestion = SurveyQuestion.objects.get(id=int(questionnumber))


	feedbackform = FeedbackForm(request.POST)
	if request.method == 'POST':
		

		if feedbackform.is_valid():
			sa = SurveyAnswer(  
				question = surveyquestion,
			    answer = feedbackform.cleaned_data['answer'],
			)
			sa.save()
		else:
			feedbackform = FeedbackForm()
	return render(request, 'index.html', {'feedbackform': feedbackform, "surveyquestion":surveyquestion})
