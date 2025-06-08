from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import QuoteRequestForm

def index_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def quote_view(request):
    if request.method == 'POST':
        # Book a Truck form
        if 'broker_name' in request.POST:
            form = QuoteRequestForm(request.POST)
            if form.is_valid():
                instance = form.save()

                broker_email = form.cleaned_data.get('email')
                broker_name = form.cleaned_data.get('broker_name')

                # Email to Broker
                subject_broker = "ProTrans Logistics - Quote Request Received"
                message_broker = (
                    f"Dear {broker_name},\n\n"
                    "Thank you for your quote request. Your request has been sent to our drivers. "
                    "A driver will confirm the load shortly.\n\n"
                    "Best regards,\n"
                    "ProTrans Logistics Team"
                )

                send_mail(
                    subject_broker,
                    message_broker,
                    settings.DEFAULT_FROM_EMAIL,
                    [broker_email],
                    fail_silently=False,
                )

                # Email to Driver
                subject_driver = f"New Quote Request from {broker_name}"
                message_driver = (
                    f"New quote request details:\n\n"
                    f"Broker Name: {broker_name}\n"
                    f"Email: {broker_email}\n"
                    f"Pickup: {form.cleaned_data.get('pickup')}\n"
                    f"Dropoff: {form.cleaned_data.get('dropoff')}\n"
                    f"Equipment: {form.cleaned_data.get('equipment')}\n"
                    f"Weight: {form.cleaned_data.get('weight')} lbs\n"
                    f"Pickup Date: {form.cleaned_data.get('pickup_date')}\n"
                    f"Notes: {form.cleaned_data.get('notes')}\n\n"
                    "Please respond to the broker as soon as possible."
                )

                send_mail(
                    subject_driver,
                    message_driver,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.COMPANY_EMAIL],  # this should be the driver's email or mailing list
                    fail_silently=False,
                )

                return redirect('quote_success')

        # Contact Us form
        elif 'contact_email' in request.POST:
            contact_email = request.POST.get('contact_email')
            message = request.POST.get('message')

            subject = "New Contact Us Message - ProTrans Logistics"
            full_message = f"From: {contact_email}\n\nMessage:\n{message}"

            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.COMPANY_EMAIL],
                fail_silently=False,
            )
            return redirect('quote_success')
    else:
        form = QuoteRequestForm()
    return render(request, 'raq.html', {'form': form})



def quote_success_view(request):
    return render(request, 'quote_success.html')
