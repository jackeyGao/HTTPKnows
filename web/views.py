import csv
import json
from collections import defaultdict
from collections import OrderedDict
from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.


def index(request):
    from web.methods import methods
    maps = {
            '1xx': "Informational",
            '2xx': "Success",
            "3xx": "Redirection",
            "4xx": "Client Error",
            "5xx": "Server Error"
        }
    with open('statusCodes.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        status_codes = []
        for row in spamreader:
            value = row[0]
            description = row[1]
            reference = row[2]
            references = reference.split('][')
            status_codes.append((value, description, references))

    category = 	defaultdict(list)		
    for row in status_codes:
        category["%sxx" % row[0][0]].append(row)

    category = OrderedDict(sorted(category.items(), key=lambda t: t[0]))
    return render_to_response('index.html', locals())

