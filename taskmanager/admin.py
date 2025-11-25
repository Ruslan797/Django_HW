from django.contrib import admin
from .models import Task, SubTask, Category


class SubTaskTabularInline(admin.TabularInline):
    model = SubTask
    extra = 1
    fields = ['title', 'description', 'deadline']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [SubTaskTabularInline]
    list_display = ('short_title', 'status', 'deadline', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'categories')
    filter_horizontal = ('categories',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)


    def short_title(self, obj):
        if len(obj.title) > 10:
            return f"{obj.title[:10]}..."
        return obj.title
    short_title.short_description = 'Title'


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'status', 'deadline', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'task')
    date_hierarchy = 'created_at'
    ordering = ('title',)
    actions = ['mark_as_done']


    def mark_as_done(self, request, queryset):
        updated = queryset.update(status='Done')
        self.message_user(request, f"{updated} subtask(s) updated to 'Done' status.")
    mark_as_done.short_description = "Mark selected as Done"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

