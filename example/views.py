from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>FLEX?</h1>
            <p>The current time is { now }. Vercel deploy working. fazul</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
