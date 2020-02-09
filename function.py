
    def load_dictionary(self, corpus, term_index, count_index,
                        separator=" ", encoding=None):
        """Load multiple dictionary entries from a file of
        word/frequency count pairs.

        **NOTE**: Merges with any dictionary data already loaded.

        Parameters
        ----------
        corpus : str
            The path+filename of the file.
        term_index : int
            The column position of the word.
        count_index : int
            The column position of the frequency count.
        separator : str, optional
            Separator characters between term(s) and count.
        encoding : str, optional
            Text encoding of the dictionary file

        Returns
        -------
        bool
            True if file loaded, or False if file not found.
        """
        if not os.path.exists(corpus):
            return False
        with open(corpus, "r", encoding=encoding) as infile:
            for line in infile:
                line_parts = line.rstrip().split(separator)
                if len(line_parts) >= 2:
                    key = line_parts[term_index]
                    count = helpers.try_parse_int64(line_parts[count_index])
                    if count is not None:
                        self.create_dictionary_entry(key, count)
        return True