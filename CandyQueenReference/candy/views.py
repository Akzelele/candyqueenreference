from django.shortcuts import render, get_object_or_404

from candy.forms.candy_form import CandyCreateForm
from candy.models import Candy


# Create your views here.
def index(request):
    context = {'candies': Candy.objects.all().order_by('name')}
    return render(request, 'candy/index.html', context)


def get_candy_by_id(request, id):
    return render(request, 'candy/candy_details.html', {
        'candy': get_object_or_404(Candy, pk=id)
    })


def create_candy(request):
    if request.method == 'POST':
        print()
    else:
        form = CandyCreateForm()
        # TODO: Instance CandyCreateForm
    return render(request, 'candy/create_candy.html', {
        'form': form
    })
