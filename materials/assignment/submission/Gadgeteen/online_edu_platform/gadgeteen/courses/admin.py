from django.contrib import admin
from .models import Subject, Course, Module, CourseSummary
from django.db.models import Count, Min, Max, DateTimeField
from django.db.models.functions import Trunc

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]


@admin.register(CourseSummary)
class CourseSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'courses_summary_change_list.html'
    
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)

        # self.get_queryset would return the base queryset. ChangeList
        # apply the filters from the request so this is the only way to
        # get the filtered queryset.

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            # See issue #172.
            # When an invalid filter is used django will redirect. In this
            # case the response is an http redirect response and so it has
            # no context_data.
            return response
        
        # List view
        metrics = {
            'total': Count('id'),
            'total_students': Count('students'),
        }

        response.context_data['summary'] = list(
            qs
            .values('title')
            .annotate(**metrics)
            .order_by('-total_students')
        )

        # List view summary
        response.context_data['summary_total'] = dict(qs.aggregate(**metrics))

        return response

