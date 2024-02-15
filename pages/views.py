from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'index.html'
    extra_context = {
        'title': 'Villa Agency - Real Estate',
    }

class ContactPageView(TemplateView):
    template_name = 'contact.html'
    extra_context = {
        'title': 'Villa Agency - Contact Page',
        'page_heading': 'Contact Us'
    }

class PropertiesPageView(TemplateView):
    template_name = 'properties.html'
    extra_context = {
        'title': 'Villa Agency - Property Listing',
        'page_heading': 'Properties'
    }

class PropertyDetailsPageView(TemplateView):
    template_name = 'property-details.html'
    extra_context = {
        'title': 'Villa Agency - Property Detail Page',
        'page_heading': 'Single Property'
    }
