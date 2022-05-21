from django.shortcuts import render
import random 

randomReportCards = [
    'Great at writing, needs speaking practice', 
    'Needs to revisit phonics', 
    'Student needs to review vocab for a minimum of 5 minutes / day'
]

# Create your views here.
def newstudent(request):
    feedback = random.choice(randomReportCards)
    context = {"context": feedback}
    return render(request, "reportcardapp/reportcard.html", context)

