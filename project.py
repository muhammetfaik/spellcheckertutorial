from itertools import islice
import pkg_resources
from symspellpy import SymSpell

sym_spell = SymSpell()

dictionary_path = pkg_resources.resource_filename( "symspellpy", "frequency_dictionary_en_82_765.txt")
sym_spell.load_dictionary(dictionary_path, 0, 1)
print(list(islice(sym_spell.words.items(), 5)))
