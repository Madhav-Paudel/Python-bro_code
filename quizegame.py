# python quiz game
# python quiz game
questions=(
    "What is the capital of France?: ",
    "What is the chemical symbol for water?: ",
    "Which planet is known as the Red Planet?: ",
    "What is the largest mammal in the world?: ",
    "Which programming language is known as the 'language of the web'?: ",
    "Who discovered penicillin?: ",
    "What is the hardest natural substance on Earth?: ",
    "What is the smallest prime number?: ",
    )

options=(
    ("A.Rome","B.Madrid","C.Paris","D.Berlin"),
    ("A.CO2","B. H2O","C.NaCl","D.O2"),
    ("A.Venus","B.Mars","C.Jupiter","D.Saturn"),
    ("A.African Elephant","B.Blue Whale","C.Giraffe","D.Hippopotamus"),
    ("A.Python","B.C++","C.Java","D.JavaScrip"),
    ("A.Marie Curie","B.Louis Pasteur","C.Alexander Fleming","D.Gregor Mendel"),  
    ("A.Gold","B.Diamond ","C.Steel","D.Quartz"),
    ("A.0","B.1","C.2","D.3"),
   
    



    )
answers=("C","B","B","B","D","C","B","C")

guesses=[]
score=0
question_number=0
 

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_number]:
        print(option)
    guess=input("enter (A,B,C,D):\n").upper()
    guesses.append(guess)
    if guess== answers[question_number]: 
       score+=1
       print("correct")
    else: 
       print("incorrect\n")
       print(f"{answers[question_number]} is correct answer")
    question_number+=1