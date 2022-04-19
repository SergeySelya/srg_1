from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .forms import InputForm
from .models import Input
import json


def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():

            # Take data from "inputs" and saving in db
            for count in range(len(request.POST) - 1):
                query = 'name' + str(count)
                input_value = request.POST[query]
                if input_value:
                    data = json.dumps(input_value, ensure_ascii=False)
                    field = json.dumps(query)
                    Input.objects.create(data=data, field=field)
                count += 1
        return redirect('/second_page/')
    else:
        # first input
        form = InputForm()
    return render(request, 'my_site/index.html', {'form': form})


def second_page(request):
    # data from the db
    json_list = list(Input.objects.all().values('id', 'field', 'data'))
    return render(request, 'my_site/second_page.html', {'json_list': json_list})
