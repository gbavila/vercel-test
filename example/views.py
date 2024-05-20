from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }. Vercel deploy working</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
