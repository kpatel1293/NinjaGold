from django.shortcuts import render,redirect
import random

# Create your views here.

# Home Page
def index(request):
    return render(request, 'index.html')

# Logic of Gold
def gold(request):
    earnOrLose = 'Earned'
    gold = 0

    if request.method == 'POST':
        if request.POST['building'] == 'farm':
            gold = random.randint(10,20)
            request.session['activityTxt'] += '{} {} golds from the {}!\n'.format(earnOrLose,gold,request.POST['building'])
        elif request.POST['building'] == 'cave':
            gold = random.randint(5,10)
            request.session['activityTxt'] += '{} {} golds from the {}!\n'.format(earnOrLose,gold,request.POST['building'])
        elif request.POST['building'] == 'house':
            gold = random.randint(2,5)
            request.session['activityTxt'] += '{} {} golds from the {}!\n'.format(earnOrLose,gold,request.POST['building'])
        elif request.POST['building'] == 'casino':
            gold = random.randint(-50,50)
            if gold < 0:
                posGold = gold * -1
                earnOrLose = 'lost'
                request.session['activityTxt'] += 'Entered a casino and {} {} gold.... Ouch....\n'.format(earnOrLose,posGold)
            else:
                request.session['activityTxt'] += 'Entered a casino and {} {} gold.... Yayy....\n'.format(earnOrLose,gold)
        
        request.session['countNum'] += gold

        return redirect('/')