from django.contrib import admin
from .models import QuoteRequest

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('broker_name', 'pickup', 'dropoff', 'equipment', 'pickup_date', 'submitted_at')
    search_fields = ('broker_name', 'pickup', 'dropoff', 'email')
    list_filter = ('equipment', 'pickup_date')
