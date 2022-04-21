from machinetranslation import translator
from flask import Flask, render_template, request
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = os.environ['apikey']
url = os.environ['url']

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench(english_text):
    '''uses IBM watson to translate'''
    return render_template('index.html')
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

@app.route("/frenchToEnglish")
def frenchToEnglish(french_text):
    '''uses IBM watson to translate'''
    return render_template('index.html')
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

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
