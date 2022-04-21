'''this translates english to french and french to english'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'LUQ5OaaiRypJEsbXH0Dpt63ZmTaE7DY5kzJeYcubf1ZP'
url = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/ac2803e7-bf7b-499d-8575-9232564bd2e6'

'''functions used to translate english to french'''

def english_to_french(english_text):
    '''uses IBM watson to translate'''
    if english_text is None:
        return 'Input is null'
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url(url)

    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').result['translations'][0]['translation']
    return french_text

'''functions used to translate french to english'''

def french_to_english(french_text):
    '''uses IBM watson to translate'''
    if french_text is None:
        return 'l entrée est nulle'
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(url)

    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').result['translations'][0]['translation']
    return english_text
