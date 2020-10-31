from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def__init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a genereic/unknown/unexpected webhook events
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )