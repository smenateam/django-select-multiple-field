# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import widgets
from django.utils.safestring import mark_safe

from django.forms.utils import flatatt

from django.utils.html import format_html

HTML_ATTR_CLASS = 'select-multiple-field'


class SelectMultipleField(widgets.SelectMultiple):
    """Multiple select widget ready for jQuery multiselect.js"""

    allow_multiple_selected = True

    def render(self, name, value, attrs=None, choices=()):
        if attrs is None:
            attrs = {}

        rendered_attrs = {'class': HTML_ATTR_CLASS}
        rendered_attrs.update(attrs)
        if value is None:
            value = []

        final_attrs = self.build_attrs(rendered_attrs)
        # output = [u'<select multiple="multiple"%s>' % flatatt(final_attrs)]
        output = [format_html('<select multiple="multiple"{0}>', flatatt(final_attrs))]
        options = self.render_options(choices, value)
        if options:
            output.append(options)

        output.append('</select>')
        return mark_safe('\n'.join(output))

    def value_from_datadict(self, data, files, name):
        """
        SelectMultipleField widget delegates processing of raw user data to
        Django's SelectMultiple widget

        Returns list or None
        """
        return super(SelectMultipleField, self).value_from_datadict(data, files, name)
