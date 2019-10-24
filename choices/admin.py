from django.contrib import admin

from .models import Choice
from polls.models import Question


class CustomChoiceAdmin(admin.ModelAdmin):
    """ The fields to be used in displaying the choice model """

    model = Choice

    list_display = (
        'text',
        'question',
        'created_at',
        'updated_at',
    )
    list_select_related = (
        'question',
    )
    list_filter = (
        'text',
        'question',
        'created_at'
    )

    fieldsets = (
        ("Question's title:", {
            'fields': ('text',),
            'description': "Designates a title to this text",
        }),
        ('Content:', {
            'fields': ('question',),
            'description': "Designates a question",
        }),
    )

    search_fields = (
        'text',
        'question'
    )
    ordering = (
        'created_at',

    )
    filter_horizontal = ()
    empty_value_display = 'None'
    list_per_page = 8


admin.site.register(Choice, CustomChoiceAdmin)
