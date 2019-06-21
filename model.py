class Model:
    def predict(self, user_input):
        """Returns input string."""
        characters =['mia',
            'brian',
            'brixton',
            'deckard',
            'gisele',
            'han',
            'hattie',
             'hobbs',
            'jesse',
             'letty',
            'megan',
             'monica',
             'one_77',
             'owen',
             'rico',
             'roman',
             'tej',
             'vince']
        import random
        return random.choice(characters)