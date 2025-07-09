from django.conf import settings
from django.urls import translate_url
from django.utils.translation import get_language, get_language_info


def languages(request):
    current_language = get_language()
    
    # Sobrescribe el idioma si es diferente al configurado
    if current_language != settings.LANGUAGE_CODE and settings.DEBUG:
        current_language = settings.LANGUAGE_CODE
    
    languages = []
    for code, name in settings.LANGUAGES:
        lang_info = get_language_info(code)
        languages.append({
            'code': code,
            'name': name,
            'name_local': lang_info['name_local'],
            'url': request.path,  # O usa translate_url si tienes i18n_patterns
            'is_current': (code == current_language),
        })
    
    return {'LANGUAGES': languages, 'CURRENT_LANGUAGE': current_language}