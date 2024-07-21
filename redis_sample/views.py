from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Event, Ticket
from .lua_scripts import purchase_ticket

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'redis_sample/event_detail.html', {'event': event})

def purchase_ticket_view(request, event_id):
    if request.method == 'POST':
        customer_username = request.POST.get('customer_username')
        success = purchase_ticket(event_id, customer_username)
        
        if success:
            event = Event.objects.get(pk=event_id)
            Ticket.objects.create(event=event, customer_username=customer_username)
            event.available_tickets -= 1
            event.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'failed', 'message': 'No tickets available'})