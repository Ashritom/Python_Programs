#Hungman game is a very popular game where you have 6 chances to guess the letters of a random word(HERE PROVIDED WITH 200 WORDS). 
#Here the program is based on the same game.Whenever you guess a correct letter of a word then it will replace the blank  
#if not the you will lose one of your 6 lives."TRY NOT TO HUNGMAN".....GOOD LUCK.....!!!




import random

logo = '''

 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    


'''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list =  [
    "program", "battery", "chicken", "elephant", "airplane", "library", "victory", "station", "honesty", "journey",
    "manager", "monster", "blanket", "diamond", "freedom", "package", "kitchen", "silence", "tension", "accident",
    "penguin", "keyboard", "desktop", "machine", "present", "pattern", "vampire", "student", "balance", "quality",
    "village", "country", "alcohol", "episode", "garbage", "harmony", "insight", "justice", "morning", "officer",
    "printer", "rescue", "session", "traffic", "athlete", "bachelor", "channel", "feature", "history", "install",
    "laptop", "machine", "novelty", "program", "quarter", "regret", "storage", "uniform", "balance", "capture",
    "desire", "exhibit", "fortune", "install", "journal", "library", "machine", "outline", "partner", "quarrel",
    "resolve", "segment", "teacher", "upgrade", "version", "weather", "awesome", "balance", "comment", "decision",
    "example", "fortune", "gravity", "holiday", "inspire", "justify", "library", "measure", "network", "opinion",
    "popular", "quality", "resilient", "society", "transfer", "upgrade", "variant", "wildlife", "amusement", "balance",
    "comfort", "delivery", "external", "friendly", "headline", "identify", "junction", "knowledge", "landscape",
    "medicine", "objective", "platform", "quantity", "resource", "schedule", "tradition", "universe", "variation",
    "wilderness", "achievement", "background", "celebration", "development", "efficiency", "foundation", "generation",
    "hospitality", "innovation", "leadership", "maintenance", "navigation", "opportunity", "performance", "reputation",
    "satisfaction", "technology", "understanding", "visualization", "administration", "communication", "demonstration",
    "entertainment", "flexibility", "imagination", "jurisdiction", "manufacturing", "notification", "organization",
    "perspective", "qualification", "recognition", "sustainability", "transformation", "utilization", "verification",
    "acknowledgment", "collaboration", "determination", "experimentation", "implementation", "justification",
    "maintenance", "organization", "participation", "qualification", "representation", "sustainability", "transformation",
    "utilization", "verification", "acknowledgment", "collaboration", "determination", "experimentation",
    "implementation", "justification", "maintenance", "organization", "participation", "qualification", "representation",
    "sustainability", "transformation", "utilization", "verification", "acknowledgment", "collaboration", "determination",
    "experimentation", "implementation", "justification", "maintenance", "organization", "participation", "qualification",
    "representation", "sustainability", "transformation", "utilization", "verification"
]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    
    if guess in display:
        print(f"You've already guessed {guess}")

    
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    
    if guess not in chosen_word:
       
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        print("Number of lives remaining are",lives)
        if lives == 0:
            end_of_game = True
            print("YOU ARE LEFT WITH NO LIVES >>>>> YOU LOSE....!!!!.")
            

    
    print(f"{' '.join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])

print(f"The chosen word was {chosen_word}")
