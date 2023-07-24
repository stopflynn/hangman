def display_hangman(tries):
    stages = [    # hanged
        """
           --------^
           |       |
          x_x      |
          /|\      |
          / \      |
                   |
            -------o
        """,
        # head body both arms and a leg hanging
        """
           --------^
           |       |
           0       |
          /|\      |
          /        |
                   |
            -------o
        """,
        # head body and both arms hanging

        """
           --------^
           |       |
           0       |
          /|\      |
                   |
                   |
            -------o
        """,
        # head body and an arm hanging

        """
           --------^
           |       |
           0       |
           |\      |
                   |
                   |
            -------o
        """,
        # head and body hanging
        """                
           --------^
           |       |
           0       |
           |       |
                   |
                   |
            -------o
        """,
        # head hanging
        """                      
           --------^
           |       |
           0       |
                   |
                   |
                   |
            -------o
        """,
        # rope hanging
        """
           --------^
           |       |
                   |
                   |
                   |
                   |
            -------o
        """,
        # empty state

        """ 
           --------^
                   |
                   |
                   |
                   |
                   |
            -------o            
        """

    ]
    return stages[tries]