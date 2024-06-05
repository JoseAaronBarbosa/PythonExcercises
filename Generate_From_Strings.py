from random import choice
from numpy import mean

def Generate_From_Alphabet (No_Of_Strings: int, Length_Of_Strings: int, Alphabet: list[str]):
    Words = []
    for i in range(No_Of_Strings):
        Word = ''.join(choice(Alphabet) for _ in range(Length_Of_Strings))
        Words.append(Word)
    return Words

def Check_If_Contains(Words, ToCheck):
    return ToCheck in Words

def Probability_Of_Name_From_Alphabet(name,Alphabet,samples):
    Probability = 1
    for element in name:
        Probability *= Alphabet.count(element)/len(Alphabet)
        if Probability == 0:
            print('The alphabet does not contain the necessary words')
            return 0, 0

    counter = 1
    Tries = [0 for _ in range(samples)]
    for i in range(samples):
        while True:
            if Check_If_Contains(Generate_From_Alphabet(1,len(name),Alphabet), name):
                #print(f"Name found in {counter} attempts")
                break
            else:
                counter += 1
        Tries[i] = counter
        counter = 0
    Average = 1/mean(Tries)

    return Average, Probability


#-------------------------------
samples = 10000
Alphabet = ['A','N']
name = 'ANA'
#-----------------------------------

Average, Probability = Probability_Of_Name_From_Alphabet(name,Alphabet, samples)
print(f"The probability of randomly creating {name} from the alphabet {Alphabet} is {(100*Average):.4f} %, (expected {(100*Probability):.4f} %) ")
