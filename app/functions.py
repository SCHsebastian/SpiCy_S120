import pandas as pd

import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector


def get_lang_detector(nlp, name):
    return LanguageDetector()


nlp = spacy.load("en_core_web_sm")
Language.factory("language_detector", func=get_lang_detector)
nlp.add_pipe('language_detector', last=True)


def get_entities(choice, text):
    nlp_processed = nlp(text)
    d = []
    results = []
    num_of_results = 0
    for entity in nlp_processed.ents:
        d.append((entity.label_, entity.text))
        df = pd.DataFrame(d, columns=('named entity', 'output'))
        print(df['named entity'].unique())
        entidad_organizacion = df.loc[df['named entity'] == 'ORG']['output']
        entidad_persona = df.loc[df['named entity'] == 'PERSON']['output']
        entidad_ubicacion = df.loc[df['named entity'] == 'LOC']['output']
        entidad_cardinal = df.loc[df['named entity'] == 'CARDINAL']['output']
        entidad_producto = df.loc[df['named entity'] == 'PRODUCT']['output']
        entidad_fecha = df.loc[df['named entity'] == 'DATE']['output']
        entidad_cantidad = df.loc[df['named entity'] == 'QUANTITY']['output']
        indefinido = df.loc[df['named entity'] == 'MISC']['output']
    if choice == 'organization':
        results = entidad_organizacion
        num_of_results = len(results)
    elif choice == 'person':
        results = entidad_persona
        num_of_results = len(results)
    elif choice == 'location':
        results = entidad_ubicacion
        num_of_results = len(results)
    elif choice == 'cardinal':
        results = entidad_cardinal
        num_of_results = len(results)
    elif choice == 'product':
        results = entidad_producto
        num_of_results = len(results)
    elif choice == 'date':
        results = entidad_fecha
        num_of_results = len(results)
    elif choice == 'quantity':
        results = entidad_cantidad
        num_of_results = len(results)
    elif choice == 'misc':
        results = indefinido
        num_of_results = len(results)

    return results, num_of_results
