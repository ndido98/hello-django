from django.shortcuts import render, get_object_or_404
from django.db import models

from polls.models import Poll

# Create your views here.
def index(request):
    polls = Poll.objects.order_by('-id')
    return render(request, 'polls/list.html', {'polls': polls})


def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    options_with_votes = poll.options.annotate(vote_count=models.Count('votes'))
    return render(request, 'polls/detail.html', {'poll': poll, 'options': options_with_votes})