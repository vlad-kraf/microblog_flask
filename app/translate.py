from flask_babel import _
from app import app


def translate(text, target_language):
    from google.cloud import translate_v2 as translate

    if 'GOOGLE_APPLICATION_CREDENTIALS' not in app.config or \
            not app.config['GOOGLE_APPLICATION_CREDENTIALS']:
        return _('Error: the translation service is not configured.')
    try:
        # Instantiates a client
        translate_client = translate.Client()

        # Translates some text into target_language
        translation = translate_client.translate(
            text,
            target_language=target_language)
    except:
        return (text, target_language, 'Error: the translation service failed.')

    return str(translation['translatedText'])
