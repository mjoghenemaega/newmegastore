from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from .cart import Cart
from apps.order.views import render_to_pdf

from apps.order.models import Order
def webhook(request):
        product.num_available = product.num_available - item.quantity
        product.save()

        html = render_to_string('order_confirmation.html', {'order': order})
        send_mail('Order confirmation', 'Your order is successful!', 'noreply@saulgadgets.com', ['mail@saulgadgets.com', order.email], fail_silently=False, html_message=html)
        subject = 'Order confirmation'
        from_email = 'noreply@saulgadgets.com'
        to = ['mail@saulgadgets.com', order.email]
        text_content = 'Your order is successful!'
        html_content = render_to_string('order_confirmation.html', {'order': order})

        pdf = render_to_pdf('order_pdf.html', {'order': order})

        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")

        if pdf:
            name = 'order_%s.pdf' % order.id
            msg.attach(name, pdf, 'application/pdf')

        msg.send()

        #html = render_to_string('order_confirmation.html', {'order': order})
        #send_mail('Order confirmation', 'Your order is successful!', 'noreply@saulgadgets.com', ['mail@saulgadgets.com', order.email], fail_silently=False, html_message=html)

        return HttpResponse(status=200) 