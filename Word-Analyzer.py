def countVowels(): #Counting Vowels
    vowels = 0
    for ch in sentence.lower():
        if ch in "aeiou":
            vowels += 1
    print(f"{vowels} Vowels")
    
def countWords(): #Couting Words
    words = sentence.split()
    words_count = 0
    for ch in words:
        words_count += 1
    print(f"{words_count} words")

def checkWords(): #Short/Long Words
    words = sentence.split()
    words_list = [] 
    for ch in words:
        words_list.append(ch)
        longest = max(words_list, key = len)
        shortest = min(words_list, key = len)
    print(f"The longest word is '{longest}'")
    print(f"The shortest word is  '{shortest}'")  

def countWord(): #Highest Character
    characters = {}
    for ch in sentence:
        if ch not in characters:
            characters[ch] = 1 
        else:
            characters[ch] += 1
    print(f"{characters} ")  

def frequencyCounter(): #FrequencyCounter
    words = sentence.split() 
    frequency = {}
    for word in words:
        if word not in frequency:
            frequency[word] = 1
        else: 
            frequency[word] += 1
    print(f"{frequency}")            


sentence = input("Input your sentence")
countVowels()
countWords()
checkWords()
countWord()
frequencyCounter()




