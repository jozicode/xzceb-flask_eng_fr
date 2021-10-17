import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('5wXMaUmTXxkXcJiTwYVplrrs72eNwrSDUnmp-Lujj90g')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com')

#translate english to french

def englishToFrench(englishText):
    translation=language_translator.translate(text=englishText,model_id='en-fr').get_result() 

    frenchText=translation['translations'][0]['translation']
    return frenchText

#translate french to english

def frenchToEnglish(frenchText):
    translation=language_translator.translate(text=frenchText,model_id='fr-en').get_result() 

    englishText=translation['translations'][0]['translation']
    return englishText