from django.conf import settings

def custom_settings(request):
    # Create fixed data structures to pass to template
    return {'cdts_version': settings.CDTS_VERSION}
