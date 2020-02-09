from symspellpy import SymSpell

sym_spell = SymSpell()
corpus_path = "word.txt"
sym_spell.create_dictionary(corpus_path)

print(sym_spell.words)
