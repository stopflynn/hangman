def display_hangman(attempts):
    stages = [  # hanged
        """
           --------^
           |       |
          x_x      |
          /|\      |
          / \      |
                   |
            _______o
        """,
        # head body both arms and a leg hanging

        """
           --------^
           |       |
           0       |
          /|\      |
          /        |
                   |
            _______o
        """,
        # head body and both arms hanging

        """
           --------^
           |       |
           0       |
          /|\      |
                   |
                   |
            _______o
        """,
        # head body and an arm hanging

        """
           --------^
           |       |
           0       |
           |\      |
                   |
                   |
            _______o
        """,
        # head and body hanging
        """                
           --------^
           |       |
           0       |
           |       |
                   |
                   |
            _______o
        """,
        # head hanging
        """                      
           --------^
           |       |
           0       |
                   |
                   |
                   |
            _______o
        """,
        # rope hanging
        """
           --------^
           |       |
                   |
                   |
                   |
                   |
            _______o
        """,
        # empty state

        """ 
           --------^
                   |
                   |
                   |
                   |
                   |
            _______o
        """

    ]
    return stages[attempts]