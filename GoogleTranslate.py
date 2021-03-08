from googletrans import Translator, LANGUAGES

langs = {'bengali': 'bn',
         'hindi': 'hi',
         'spanish': 'es',
         'french': 'fr',
         'italian': 'it',
         'portuguese': 'pt'
}


def trans(txt, dst):
    global langs

    try:
        t = Translator().translate(txt, src='en', dest=langs[dst])
        return t.text
    except Exception:
        return 'Can\'t understand! Would you please repeat?'


'''
for lang in LANGUAGES:
    print(lang, LANGUAGES[lang])
'''

'''
print(t.extra_data['possible-mistakes'])
print(t.extra_data['possible-translations'])
'''

# print(trans('I am a disco dancer'))
