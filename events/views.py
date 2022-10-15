from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect, HttpResponse
import calendar
from calendar import HTMLCalendar
from datetime import datetime

from .models import Event, Venue

from .forms import VenueForm, EventForm, EventFormAdmin

import csv

from django.contrib import messages

# pdf generating
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Import Pagination
from django.core.paginator import Paginator


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = request.user
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(year, month_number)

    now = datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M %p')
    return render(request,
                  'events/home.html',
                  {
                    'name': name,
                    'year': year,
                    'month': month,
                    'month_number': month_number,
                    'cal': cal,
                    'current_year': current_year,
                    'time': time,

                  })


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html', {'event_list': event_list})


def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            venue = form.save(commit=False)
            venue.owner = request.user.id
            venue.save()
            return HttpResponseRedirect('/add-venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/venue.html', {'form': form, 'submitted':submitted})


def list_venue(request):
    # venue_list = Venue.objects.all().order_by('?')
    venue_list = Venue.objects.all()

    p = Paginator(Venue.objects.all(), 3)
    page = request.GET.get('page')
    venues = p.get_page(page)

    return render(request, 'events/venues.html', {'venue_list': venue_list,
                                                  'venues': venues})


def venue_detail(request, pk):
    venue = Venue.objects.get(id=pk)
    return render(request, 'events/venue_detail.html', {'venue':venue})


def search_venue(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        venues = Venue.objects.filter(name__icontains=searched)
        return render(request, 'events/search_venues.html', {'searched':searched, 'venues':venues})
    else:
        return render(request, 'events/search_venues.html', {})


def update_venue(request, pk):
    venue = Venue.objects.get(id=pk)

    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list_venue')
    return render(request, 'events/venue_update.html', {'venue': venue, 'form': form})


# add event

def add_event(request):
    submitted = False
    if request.method == 'POST':
        if request.user.is_superuser:
            form = EventFormAdmin(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/add-event?submitted=True')
        else:
            form = EventForm(request.POST)
            if form.is_valid():
                # form.save()
                event = form.save(commit=False)
                event.manager = request.user
                event.save()
                return HttpResponseRedirect('/add-event?submitted=True')

    else:
        if request.user.is_superuser:
            form = EventFormAdmin
        else:
            form = EventForm

        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_event.html', {'form': form, 'submitted': submitted})

# update event

def update_event(request, pk):
    event = Event.objects.get(id=pk)
    if request.user.is_superuser:
        form = EventFormAdmin(request.POST or None, instance=event)
    else:
        form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('event-list')
    return render(request, 'events/update_event.html', {'event': event, 'form': form})

# delete event

def delete_event(request, pk):
    event = Event.objects.get(id=pk)
    if request.user == event.manager:
        event.delete()
        messages.success(request, ("Event Deleted Successfully!"))
        return redirect('event-list')
    else:
        messages.success(request, ("You Are Not Authorithed To Delete This Event!"))
        return redirect('event-list')


def delete_venue(request, pk):
    event = Venue.objects.get(id=pk)
    event.delete()

    return redirect('list_venue')



def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=venues.txt'

    # lines = ["Tis is line 1\n line2\n line3\n"]
    venues = Venue.objects.all()

    lines = []

    for venue in venues:
        lines.append(f'{venue.name}\n{venue.address}\n{venue.phone}\n{venue.web}\n\n')
    response.writelines(lines)
    return response



# csv

def venue_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=venues.csv'

    # create csv writer
    writer = csv.writer(response)

    venues = Venue.objects.all()

    # add column headings
    writer.writerow(['Venue name', 'Address', 'Zipcode', 'Phone', 'Web', 'email address'])


    for venue in venues:
        writer.writerow([venue.name, venue.address, venue.zip_code, venue.phone, venue.web, venue.email])
    return response

# Generate Pdf file

def venue_pdf(request):
    buf = io.BytesIO()
#     create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
#     create text object
    text_object = c.beginText()
    text_object.setTextOrigin(inch, inch)
    text_object.setFont("Helvetica", 14)
    venues = Venue.objects.all()
#     add some lines of text
    lines = []

    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.zip_code)
        lines.append(venue.phone)
        lines.append(venue.web)
        lines.append(venue.email)
        lines.append('############')

    for line in lines:
        text_object.textLine(line)

    c.drawText(text_object)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='Venue.pdf')

