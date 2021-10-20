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

def english_to_french(englishText): #function englishToFrench

    french_Translation = language_translator.translate(
        text = englishText, model_id = 'en-fr'
        ).get_result()

    return french_Translation.get("translations")[0].get("translation")



def french_to_english(frenchText): #function frenchToEnglish

    english_Translation = language_translator.translate(
        text = frenchText,model_id = 'fr-en'
    ).get_result() 

    return english_Translation.get("translations")[0].get("translation")
