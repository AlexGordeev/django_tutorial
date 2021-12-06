from ckeditor_uploader.widgets import CKEditorUploadingWidget

from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, News


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'views', 'created_at', 'updated_at')
    form = NewsAdminForm
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published')
    readonly_fields = ('created_at', 'updated_at', 'views', 'get_photo')
    save_on_top = True
    search_fields = ('title', 'content')

    def get_photo(self, obj: News) -> str:
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        return '-'

    get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_header = 'Управление новостями'
admin.site.site_title = 'Управление новостями'
