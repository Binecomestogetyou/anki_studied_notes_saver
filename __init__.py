from aqt import mw
from aqt import gui_hooks


def save_studied_words() -> None:

    col = mw.col

    studiedtoday = col.find_cards("rated:1")

    if studiedtoday:

        englishwords = open('ankipalavras/estudadas/englishwords.txt', 'w')
        frenchwords = open('ankipalavras/estudadas/frenchwords.tx', 'w')
        japanesewords = open('ankipalavras/estudadas/japanesewords.txt', 'w')
        latinwords = open('ankipalavras/estudadas/latinwords.txt', 'w')
        greekwords = open('ankipalavras/estudadas/greekwords.txt', 'w')

        for card in studiedtoday:

            notes = []

            if col.get_card(card).note().id not in notes:
                notes.append(col.get_card(card).note().id)
                word = col.get_note(col.get_card(card).note().id).fields[0]
            else:
                continue

            deckid = col.get_card(card).did

            for deck in col.decks.all_names_and_ids():
                if deckid == deck.id:
                    # Deck names were hardcoded. If you renamed any deck, you'll have to update this code
                    if deck.name == 'All in One Kanji' or deck.name == 'Adjetivos japoneses' or deck.name == 'kana' or deck.name == 'japanese verbs':
                        japanesewords.write(word + '\n')
                    elif deck.name == 'English words' or deck.name == 'English Verbs':
                        englishwords.write(word + '\n')
                    elif deck.name == 'greek':
                        greekwords.write(word + '\n')
                    elif deck.name == 'latin words':
                        latinwords.write(word + '\n')
                    elif deck.name == 'mots françaises':
                        frenchwords.write(word + '\n')


def make_appends() -> None:
    gui_hooks.reviewer_will_end.append(save_studied_words)
    gui_hooks.sync_did_finish.append(save_studied_words)


gui_hooks.main_window_did_init.append(make_appends)
