#!/usr/bin/env python3
import random
import re
import sys
import os

custom_uwu_words = {
    'toaster': 'pwotogen', 'dog': 'pup~', 'cat': 'kitteh~', 'fish': 'fwish~', 'bird': 'biwd~',
    'apple': 'awpple~', 'banana': 'bananaw~', 'car': 'caww~', 'train': 'twain~', 'plane': 'pwane~',
    'mouse': 'mewse~', 'keyboard': 'keebwawd~', 'computer': 'compuwter~', 'phone': 'fone~', 'tablet': 'tabwet~',
    'coffee': 'caffi~', 'tea': 't-t-twa~', 'book': 'buwk~', 'pencil': 'penciw~', 'paper': 'papew~',
    'laptop': 'waptop~', 'camera': 'camawe~', 'television': 'tewevision~', 'doggos': 'pups~', 'puppy': 'pup~',
    'kitten': 'kitteh~', 'lion': 'wion~', 'tiger': 'tigeh~', 'elephant': 'ewwephant~', 'giraffe': 'giwaf~',
    'monkey': 'munky~', 'bear': 'baww~', 'wolf': 'woof~', 'rabbit': 'wabbit~', 'chicken': 'chikkun~',
    'cow': 'cowww~', 'horse': 'howsie~', 'sheep': 'sheepie~', 'goat': 'goaty~', 'fishies': 'fishes~',
    'snake': 'snewke~', 'bat': 'bawt~', 'doggy': 'doggiewog~', 'pizza': 'pizzaw~', 'burger': 'buwga~',
    'sandwich': 'sandi~', 'cheese': 'cheesy~', 'chocolate': 'chocowate~', 'ice cream': 'ice cwweam~',
    'cookie': 'cookiewookie~', 'candy': 'candywandy~', 'popcorn': 'poppycown~', 'cake': 'cakey~',
    'cupcake': 'cupcawy~', 'donut': 'doughnutty~', 'muffin': 'muffinny~', 'cookie': 'cookiewooki~',
    'soda': 'sodeh~', 'water': 'watwah~', 'juice': 'juicywicy~', 'milk': 'miwk~', 'beer': 'beew~',
    'wine': 'winn~', 'whiskey': 'whisky~', 'vodka': 'vodkaw~', 'margarita': 'margawita~',
    'salt': 'sawt~', 'pepper': 'peppaw~', 'sugar': 'shuga~', 'honey': 'honeybuns~', 'sweet': 'sweety~',
    'spicy': 'spiccy~', 'sour': 'souw~', 'bitter': 'bittew~', 'salty': 'sawty~', 'delicious': 'dewiciwous~',
    'delightful': 'dewightfuw~', 'yummy': 'yummyyy~', 'gross': 'gwooss~', 'food': 'fud~', 'meal': 'meoww~',
    'chicken wings': 'chikkun wings~', 'steak': 'stweak~', 'pasta': 'pastaw~', 'salad': 'salawd~',
    'soup': 'soop~', 'sandwiches': 'sandiwichew~', 'taco': 'tacow~', 'burrito': 'buwwito~',
    'tortilla': 'towtilla~', 'fries': 'fwiwes~', 'potato': 'potatow~', 'onion': 'onyon~', 'tomato': 'tomatow~',
    'mushroom': 'mushwom~', 'spinach': 'spiwach~', 'carrot': 'cawwot~', 'broccoli': 'bwocowiw~',
    'cucumber': 'cukumbew~', 'lettuce': 'wettuce~', 'spinach': 'spiwach~', 'green beans': 'gween beans~',
    'corn': 'cown~', 'peas': 'peaww~', 'apple pie': 'awpple pye~', 'pie': 'pwie~', 'pudding': 'puddingwuddy~',
    'cake': 'cakey~', 'donut': 'donuty~', 'chocolate cake': 'chocowate cake~', 'ice cream': 'ice cwweam~',
    'burger': 'buwga~', 'grilled cheese': 'gwilled cheezy~', 'pasta': 'pastaw~', 'bacon': 'baconny~',
    'chicken nugget': 'chikkun nugget~', 'chicken sandwich': 'chikkun sandwich~', 'fries': 'fwiwes~',
    'steak': 'stweak~', 'hot dog': 'hot doggy~', 'french fries': 'fwench fwiwes~', 'bread': 'bwead~',
    'butter': 'butteh~', 'cheese': 'cheesy~', 'hot chocolate': 'hot chocowate~', 'whipped cream': 'whipped cwweam~',
}

furry_replacements = {
    r'\bnot\b': "k'not",
    r'\bno\b': "nuu",
    r'\byes\b': "yurr!",
    r'\bme\b': "m-me >//<",
    r'\byou\b': "u",
    r'\bthis\b': "dis",
    r'\bthat\b': "dat",
    r'\bthe\b': "da",
    r'\bhi\b': "haii~",
    r'\bhello\b': "hewwo",
    r'\bhey\b': "haiii",
    r'\blove\b': "wuv",
    r'\bhate\b': "hewt ;~;",
    r'\bfurry\b': "fuwwy~",
}

suffixes = ["~", " x3", " >w<", " nya~", " UwU", " owo", " :3", " *notices you*", " rawr~", " *glomps*", " *pounces on u*"]

def uwuify_word(word):
    punct = ''
    if word[-1] in '.,!?':
        punct = word[-1]
        word = word[:-1]

    word = re.sub(r'[rl]', 'w', word)
    word = re.sub(r'[RL]', 'W', word)
    word = re.sub(r'n([aeiou])', r'ny\1', word)
    word = re.sub(r'N([aeiouAEIOU])', r'Ny\1', word)

    for word_key, uwu_word in custom_uwu_words.items():
        word = re.sub(rf'\b{word_key}\b', uwu_word, word, flags=re.IGNORECASE)

    for pattern, repl in furry_replacements.items():
        word = re.sub(pattern, repl, word, flags=re.IGNORECASE)

    if len(word) > 2 and random.random() < 0.15:
        word = f"{word[0]}-{word}"

    return word + punct

def uwuify_text(text):
    words = text.split()
    uwuified = [uwuify_word(word) for word in words]
    text = ' '.join(uwuified)

    text = re.sub(r'([.!?])', lambda m: m.group(1) + random.choice(suffixes), text)

    return text

def process_file(input_filename):
    with open(input_filename, 'r') as file:
        content = file.read()

    uwuified_content = uwuify_text(content)

    output_filename = f"uwuified_{os.path.basename(input_filename)}"
    with open(output_filename, 'w') as file:
        file.write(uwuified_content)

    print(f"UwUified file saved as {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 uwuifier.py 'Your text here' or python3 uwuifier.py <filename>")
        sys.exit(1)

    input_arg = sys.argv[1]

    if input_arg.endswith(".txt"):
        process_file(input_arg)
    else:
        input_text = ' '.join(sys.argv[1:])
        output = uwuify_text(input_text)
        print(output)
