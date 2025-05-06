from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from django.contrib.auth import authenticate, login as auth_login

from polls.models import Poll, PollOption, Vote

# Create your views here.
def index(request):
    polls = Poll.objects.order_by('-id')
    return render(request, 'polls/list.html', {'polls': polls})


def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    options_with_votes = poll.options.annotate(vote_count=models.Count('votes'))
    return render(request, 'polls/detail.html', {'poll': poll, 'options': options_with_votes})


def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    options_with_votes = poll.options.annotate(vote_count=models.Count('votes'))
    if request.method == "POST":
        try:
            selected_option = poll.options.get(pk=request.POST['option'])
        except (KeyError, PollOption.DoesNotExist):
            return render(request, 'polls/detail.html', {
                'poll': poll,
                'options': options_with_votes,
                'error': 'You did not select a valid option.'
            })
        else:
            Vote.objects.update_or_create(
                poll=poll,
                user=request.user,
                defaults={'option': selected_option}
            )
    return redirect('polls:detail', poll_id=poll_id)


def login(request):
    if request.method == "GET":
        return render(request, 'polls/login.html')
    elif request.method == "POST":
        try:
            username, password = request.POST['username'], request.POST['password']
        except KeyError:
            return render(request, 'polls/login.html', {'error': 'Please enter username and password.'})
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('polls:index')
        else:
            return render(request, 'polls/login.html', {'error': 'Invalid username or password.'})