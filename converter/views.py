from django.shortcuts import render
from .forms import MoneySum

def index(request):
    submitbutton = request.POST.get('submit')

    new_amount = ''

    form = MoneySum(request.POST or None)

    if form.is_valid():
        amount = form.cleaned_data.get('amount')
        new_amount = form.exchange(amount)

    rate = form.get_current()

    return render(request, 'converter/converter.html', {'form': form, 'amount': new_amount, 'submitbutton': submitbutton, 'rate': rate})
