class Executive:
    def __init__(self, file_path):
        self.file_path = file_path
        self.board_games = []

    def run(self):
        self.download_board_games()
        self.display_menu()
    
def download_board_games(self):
    try:
        with open(self.file_name, 'r') as file:
            file_lines = file.readlines() 
            for line in file_lines:  
                game_info = line.strip().split('\t')
                board_game = BoardGame(
                    name = game_info[0],
                    genre = game_info[1],
                    year = int(game_info[2]),  # Assuming year is an integer
                    weight = float(game_info[3]),  # Assuming weight is a float
                    gibbons_rating = float(game_info[4]),  # Assuming ratings are floats
                    people_rating = float(game_info[5]),
                    player_counts = list(map(int, game_info[6].split(',')))  # Assuming player counts are comma-separated integers
                )
                board_games.append(board_game)
    except FileNotFoundError:
        print(f"File not found: {self.file_name}")
def display_menu(self):
    while True:
        print('User Menu:')
        print('1 Print all games highest Gibbons rating to lowest')
        print('2 Print all games from a year')
        print('3 Print all games with a weight equal to or lower than a provided weight')
        print('4 The People VS Dr. Gibbons')
        print('5 Print based on player count')
        print('6 Exit the program')
        user_choice = int(input('Enter your choice: '))
        
        if user_choice == '1':
            self.rating_highest_to_lowest()

        elif user_choice == '2':
            year = int(input('Enter a year: '))
            self.games_year()

        elif user_choice == '3':
            weight = int(input('Enter a weight: '))
            self.compare_weight()

        elif user_choice == '4':
            self.people_vs_gibbons()
            number = float(input('Enter a number: '))
        elif user_choice == '5':
            player_count = int(input('Enter the player count: '))
            self.player_count()

        
        elif user_choice == '6':
            print('Bye Bye!')
        
        else:
            print('Invalid choice. Please enter a number between 1 and 6. ')
