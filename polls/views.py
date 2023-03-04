from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.urls import reverse
from tour.models import Tour
from django.contrib.auth.models import User
from .models import Choice, Question
from .forms import ques_updater
from datetime import datetime,timedelta

def index(request):
    user_list = User.objects.all().order_by('-username')
    context = {'user_list' : user_list}
    if request.method == "POST":
        if 'create-tour' in request.POST:
            new_tour_name = request.POST['tour_name']
            new_tour_desc = request.POST['tour_desc']
            new_tour = Tour.objects.create(tour_name=new_tour_name, desc = new_tour_desc)
            new_tour.created_by = request.user.username
            new_tour.save()
            id_list = request.POST.getlist('boxes')
            for id in id_list:
                ad_user = User.objects.get(pk = id)
                new_tour.users.add(ad_user)
            new_tour.save()
            messages.success(request, "Tour Created!")
            return redirect('/tour/polls/')
        
        elif 'add-ques' in request.POST:
            currtour_name = request.POST['tour']
            question = request.POST['question']
            choice1 = request.POST['choice1']
            choice2 = request.POST['choice2']
            choice3 = request.POST['choice3']
            new_ques = Question()
            current_tour = Tour.objects.get(tour_name=currtour_name)
            new_ques.trip = current_tour
            new_ques.question_text = question
            new_ques.save()
            sel_option = request.POST.get('ques_type')
            new_ques.ques_type = sel_option
            new_ques.save()
            ch1 = Choice(question=new_ques, choice_text=choice1,new_id = 'choice1')
            ch1.save()
            ch2 = Choice(question=new_ques, choice_text=choice2,new_id = 'choice2')
            ch2.save()
            ch3 = Choice(question=new_ques, choice_text=choice3,new_id = 'choice3')
            ch3.save()
            messages.success(request, "Question Added!")
            return redirect('/tour/polls/')
        else:
            return render(request, 'polls/index.html')
    else:
        return render(request, 'polls/index.html',context)


def showQues(request):
    if request.method == "POST":
        currtour_name = request.POST['search_tour']
        current_tour = Tour.objects.get(tour_name=currtour_name)
        userlist = current_tour.users.all()
        question_list = Question.objects.filter(trip=current_tour)
        context = {'question_list': question_list, 'tour': current_tour, 'userlist':userlist}
        return render(request, 'polls/showQues.html', context)

    else:
        context = {}
        return render(request, 'polls/showQues.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(  # type: ignore
            pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) # type: ignore

def editQues(request, question_id):
    ques = get_object_or_404(Question, pk=question_id)
    choice_list = Choice.objects.filter(question = ques)
    if request.method == "POST":
        if 'update_ques' in request.POST:
            q_form = ques_updater(request.POST, instance=ques)
            if q_form.is_valid():
                q_form.save()
                messages.success(request, "Successfully Updated")
                context = {'q_form': q_form,'choice_list' : choice_list,'edit':"Edit question"}
                return render(request, 'polls/editQues.html', context)
            
        elif 'choice_edit' in request.POST:
            choice1_text = request.POST['choice_edit1']
            choice2_text = request.POST['choice_edit2']
            choice3_text = request.POST['choice_edit3']
            cho1 = Choice.objects.get(question = ques, new_id = 'choice1')
            cho1.choice_text = choice1_text
            cho1.save()
            cho2 = Choice.objects.get(question = ques, new_id = 'choice2')
            cho2.choice_text = choice2_text
            cho2.save()
            cho3 = Choice.objects.get(question = ques, new_id = 'choice3')
            cho3.choice_text = choice3_text
            cho3.save()
            messages.success(request, "Successfully Updated")
            choice_list = Choice.objects.filter(question = ques)
            q_form = ques_updater(instance=ques)
            context = {'q_form': q_form,'choice_list' : choice_list,'edit':"Edit question"}
            return render(request, 'polls/editQues.html', context)
        elif 'delete_ques' in request.POST:
            ques.delete()
            messages.success(request, "Successfully Deleted! Go back to view questions page.")
            context = {}
            return render(request, 'polls/editQues.html', context)
        else:
            q_form = ques_updater(instance=ques)
            context = {'q_form': q_form,'choice_list' : choice_list,'edit':"Edit question"}
            return render(request, 'polls/editQues.html', context)

    else:
        q_form = ques_updater(instance=ques)
        
    context = {'q_form': q_form,'choice_list' : choice_list,'edit':"Edit question"}
    return render(request, 'polls/editQues.html', context)

def iti_page(request):
    if request.method == "POST":
        curtour_name = request.POST['search_iti']
        curr_tour = Tour.objects.get(tour_name=curtour_name)
        
        date_ques = Question.objects.get(trip=curr_tour, ques_type = "Date")
        max_date = Choice.objects.filter(question=date_ques).order_by('-votes').first()
        start_date = datetime.strptime(max_date.choice_text, '%d %B').date() #type: ignore
        
        venue_ques = Question.objects.get(trip=curr_tour, ques_type = "Venue")
        max_venue = Choice.objects.filter(question = venue_ques).order_by('-votes').first()
        
        duration_ques = Question.objects.get(trip=curr_tour, ques_type = "Duration")
        max_duration = Choice.objects.filter(question = duration_ques).order_by('-votes').first()
        tot_day = int(max_duration.choice_text) #type: ignore
        trip_days = []
        for i in range (1, tot_day+1):
            trip_days.append(i)
        
        dates = [(start_date + timedelta(days=i)).strftime("%d %B") for i in range(tot_day)]
        itinerary = list(zip(trip_days, dates))

        other_ques_list = Question.objects.filter(trip=curr_tour,ques_type = "Other")
        max_other_list = []
        for ques in other_ques_list:
            ch_list = Choice.objects.filter(question = ques)
            max_ch = ch_list.order_by('-votes').first()
            max_other_list.append(max_ch)
        
        activities_list = Question.objects.filter(trip=curr_tour,ques_type = "Activities")
        max_activities = []
        for ques in activities_list:
            ch_list = Choice.objects.filter(question = ques)
            max_ch = ch_list.order_by('-votes').first()
            max_activities.append(max_ch)
        context = {'other_ques_list': other_ques_list, 
                   'tour': curr_tour, 
                    'max_date':max_date,
                    'max_venue':max_venue,
                    'max_duration':max_duration,
                   'max_other_list': max_other_list,
                   'max_activities':max_activities,
                   'dates':dates,
                   'itinerary':itinerary
                   }
        return render(request, 'polls/itineraryPage.html', context)
    
    else:
        context = {}
        return render(request, 'polls/itineraryPage.html', context)
    