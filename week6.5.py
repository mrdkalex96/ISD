sentence1 = input("Insert the first sentence ") #insert first sentence
sentence2 = input("Insert the second sentence ")#insert second sentence
mixed_sentence = sentence1 + " " + sentence2  #concatenating the sentences
print(mixed_sentence)

sentence_list = mixed_sentence.split() #split the sentence
print(sentence_list)

sentence_list.sort(); #sorting the sentence
print(sentence_list)
print("The lenght of the sentence is ",len(sentence_list)," words") #print the lenght

dic = {}

for i in sentence_list:  #loop to create the dictionary 


    dic.update({i: sentence_list.count(i)})
    

print(dic)




