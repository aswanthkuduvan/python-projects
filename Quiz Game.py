# Add question, options and answer to a list

questions = [{"prompt" : "1. Which country has won the most FIFA World Cup titles?",
              "options" : ["A. Argentina", "B. Germany", "C. Brazil", "D. Italy"],
              "answer" : "C"},

             {"prompt" : "2. Who holds the record for the most Grand Slam tennis titles in men's singles?",
              "options" : ["A. Novak Djokovic", "B. Roger Federer", "C. Rafael Nadal", "D. Pete Sampras"],
              "answer" : "A"},

             {"prompt" : "3. In which year did the first modern Olympic Games take place?",
              "options" : ["A. 1896", "B. 1904", "C. 1912", "D. 1920"],
              "answer" : "A"},

             {"prompt": "4. Which NBA player is known for the nickname 'King James'?",
              "options": ["A. Kobe Bryant", "B. Michael Jordan", "C. LeBron James", "D. Stephen Curry"],
              "answer": "C"},

             {"prompt": "5. Which sport is the Tour de France associated with?",
              "options": ["A. Swimming", "B. Cycling", "C. Running", "D. Skiing"],
              "answer": "B"}]


def run_question(questions): # Define a function
    score = 0 # Set score to zero
    for question in questions: # Define a loop to iterate all the dictionary inside the list
        print(question["prompt"]) # Print the question from the first dictionary
        for options in question["options"]: # define an inner loop for iterating the options
            print(" ", options) # Print the options
        answer = input("Enter your answer A, B, C or D: ").upper() # Tell the user to enter answer
        if answer == question["answer"]: # Check the answer is right or wrong
            print("Right answer. 🎉🎉")
            score += 1 # Update the score
        else:
            print("Wrong answer. 😔😔, Right answer is" , question["answer"], "\n")
        print()
    print(f'You have scored {score} out of {len(questions)} 😊😊') # print the total mark


run_question(questions) # Call the function