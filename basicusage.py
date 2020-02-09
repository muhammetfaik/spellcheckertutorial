import pkg_resources
from symspellpy import SymSpell,Verbosity

sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
dictionary_path = pkg_resources.resource_filename("symspellpy","frequency_dictionary_en_82_765.txt")
sym_spell.load_dictionary(dictionary_path,term_index=0,count_index=1)
input_term = "members"
suggestions = sym_spell.lookup(input_term,Verbosity.CLOSEST,max_edit_distance=2)
for suggestions in suggestions:
    print(suggestions)