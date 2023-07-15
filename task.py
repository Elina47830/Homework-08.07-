import googletrans

TRANSLATOR = googletrans.Translator()

with open('original.txt', 'w',  encoding='utf-8') as my_file:
    my_file.write('''Привіт! Зараз не можу точно сказати яка моя улюблена гра, але мені подобаються Honkai Star Rail та Valorant.
Хонкай припадає до душі користувачам своєю різноманітністю. В цій грі добре пророблені персонажі, гарна озвучка, цікаві квести, відкритий світ та ще дуже багато чого.
У Валоранті ж є крутим те, що потрібно завжди бути пильним, прислуховуватися і швидко діяти. Також, там є багато персонажів(агентів) з різними уміннями, що дозволяє урізноманітнювати гру і захоплювати гравців ще більше.
Дякую за увагу!''')

with open('original.txt', 'r',  encoding='utf-8') as my_file:
    original_text = my_file.read()
    en_translate = TRANSLATOR.translate(original_text, dest='en').text
    pl_translate = TRANSLATOR.translate(original_text, dest='pl').text
    de_translate = TRANSLATOR.translate(original_text, dest='de').text

with open('en_translate.txt', 'w', encoding='utf-8') as en_file:
    en_file.write(f'Англійська \n{en_translate}')
with open('pl_translate.txt', 'w', encoding='utf-8') as pl_file:
    pl_file.write(f'Польська \n{pl_translate}')
with open('de_translate.txt', 'w', encoding='utf-8') as de_file:
    de_file.write(f'Німецька \n{de_translate}')