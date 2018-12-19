# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import widgets

HTML_ATTR_CLASS = 'select-multiple-field'


class SelectMultipleField(widgets.SelectMultiple):
    """Multiple select widget ready for jQuery multiselect.js"""

    def __init__(self):
        super(SelectMultipleField, self).__init__(attrs={'class': HTML_ATTR_CLASS})
