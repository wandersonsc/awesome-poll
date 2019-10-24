from django.contrib import admin

from .models import Question


class CustomQuestionAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the Exams model.

    model = Question
    list_display = (
        'title',
        'slug',
        'body',
        'approved_question',
        'author',
        'created_at',
        'updated_at',

    )
    list_select_related = (
        'author',
    )
    list_filter = (
        'title',
        'approved_question',
        'author'
    )

    fieldsets = (
        ("Question's title:", {
            'fields': ('title',),
            'description': "Designates a title to this question",
        }),
        ('Content:', {
            'fields': ('body',),
            'description': "Designates a body of exam to question",
        }),
        ('Question status:', {
            'fields': ('approved_question',),
            'description': "Switch between approved or unapproved question",
        }),

    )

    search_fields = (
        'title',
        'approved_question'
    )
    ordering = (
        'created_at',

    )
    filter_horizontal = ()
    empty_value_display = 'None'
    list_per_page = 8

    def save_model(self, request, obj, form, change):
        #  required to add user's name to the author field

        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Question, CustomQuestionAdmin)
