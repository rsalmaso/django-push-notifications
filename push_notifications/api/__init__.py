# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function #, unicode_literals
from django.conf import settings

if "tastypie" in settings.INSTALLED_APPS:
    # Tastypie resources are importable from the api package level (backwards compatibility)
    from .tastypie import APNSDeviceResource, GCMDeviceResource, APNSDeviceAuthenticatedResource, GCMDeviceAuthenticatedResource

    __all__ = [
        "APNSDeviceResource",
        "GCMDeviceResource",
        "APNSDeviceAuthenticatedResource",
        "GCMDeviceAuthenticatedResource"
    ]
