import random

subjects = ["Ankit","Amitabh Bachan","shahrukh Khan","price william","Donald trump ","PM Modi",
            "CM of Haryana","A crowd","A Group of Women","A big monkey is","An Elephant",
            "A Cat from delhi","Ur DAD","Ur Uncle","An Astronaut","Students"]

actions = ["doing the chicken dance with", "pretending to be a secret agent with ", "talking to plants ", "trying to high five ",
           "arguing with ", "misplacing their glasses ", "sneaking midnight snacks with ", "dramatically narrating their own life", 
           "speaking in rhyme with ", "inventing new dance moves with","mismatching shoes", "having staring contests",
           "making up silly songs on", "giving pep talks", "juggling fruit while", "attempting to moonwalk",
           "randomly bursting into", "naming every object on ", "tickling himself (and pretending it worked)", "trying to wink "]

objects = ["banana phone", "dancing toaster", "singing lamp", "invisible umbrella", "wobbly chair", 
          "sneezing cactus", "giggle box", "sock puppet", "wobbly table leg", "dinosaur slippers", 
          "talking pillow", "fluffy dragon plush", "wiggling toothbrush", "bouncing stapler", 
          "mischievous remote", "hat with googly eyes","jumping pen", "laughing kettle", "sleepy desk fan",
          "winking coffee mug"]

while(True) :
    subject =random.choice(subjects)
    action =random.choice(actions)
    object= random.choice(objects)
    
    headline =f'breaking news :{subject} {action} {object} '
    print(headline)

    user =input("do u want to continue ").strip().lower()
    if user=="no" :
        break;