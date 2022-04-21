'''this translates english to french and french to english'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

'''functions used to translate english to french'''

def englishToFrench(english_text):
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

def frenchToEnglish(french_text):
    '''uses IBM watson to translate'''
    if french_text is None:
        return 'l entree est nulle'
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

