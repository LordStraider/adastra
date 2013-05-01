from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from dataManager.models import Choice, Poll, Menu
from django.utils import simplejson
from django.core.context_processors import csrf


def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll': p},
                               context_instance=RequestContext(request))

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))

def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/results.html', {'poll': p})

def menu(request):
    if request.is_ajax():
        string = '['
        for item in Menu.objects.all():
            string +=  '{"menu": "'
            string += item.text
            string += '"}, '
        string.pop()
        string += ']'
        print string
        line = '[ {"TEST1":45,"TEST2":23,"TEST3":"DATA1"}, {"TEST1":46,"TEST2":24,"TEST3":"DATA2"}, {"TEST1":47,"TEST2":25,"TEST3":"DATA3"}]'
        input_map = simplejson.loads(line)
        print input_map
        return HttpResponse(simplejson.dumps(input_map), mimetype='application/javascript')
