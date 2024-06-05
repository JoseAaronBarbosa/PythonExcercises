from random import choice

def Form_Suffix_Strings(Array):
    Suffix_Strings = []
    for i in range(len(Array[0])):
        Suffix_Strings.append(Array[0][i:])
    return Suffix_Strings

def Longest_CP(string_1,string_2):
    for i in range(min(len(string_1),len(string_2))):
        if string_1[i] != string_2[i]:
            return string_1[:i]

def Check_Among_Adjacent_Entries(SSS):
    Longest = 0
    for i in range(len(SSS)-1):
        Common = Longest_CP(SSS[i],SSS[i+1])
        if Common:
            x = len(Common)
        else:
            x = 0

        if x > Longest:
            Longest = x
            Longest_String = Common
    return Longest_String

def Generate_From_Alphabet (No_Of_Strings: int, Length_Of_Strings: int, Alphabet: list[str]):
    Words = []
    for i in range(No_Of_Strings):
        Word = ''.join(choice(Alphabet) for _ in range(Length_Of_Strings))
        Words.append(Word)
    return Words

def Return_Index(Array,L_String):
    Indexes = []
    Taille = len(L_String)
    for i in range(len(Array[0])-Taille):
        if(Array[0][i:i+Taille] == L_String):
            Indexes.append(i)
    return Indexes

def Display(Array,Indexes,L_String):
    Taille = len(L_String)
    D_Array = Array[0]
    offset = 0
    for Idx in Indexes:
        D_Array = D_Array[:Idx+offset] + '-' + D_Array[Idx+offset:Idx+offset+Taille] + '-' + D_Array[Idx+Taille+offset:]
        offset += 2
    return D_Array

Array = Generate_From_Alphabet(1,100000,['a','c','g','t'])
Suffix_Strings = Form_Suffix_Strings(Array)
Sorted_SS = sorted(Suffix_Strings)
L_String = Check_Among_Adjacent_Entries(Sorted_SS)
Indexes = Return_Index(Array,L_String)
D_Array = Display(Array,Indexes,L_String)

#print(Array[0])
print(f'The longest common string is {L_String}.')
print(f'At indexes {Indexes}')
#print(D_Array)

