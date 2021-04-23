# importing csv package
import csv

# creating an empty dictionary
dict = {}

# writing our dictionary with given csv file

with open('french_dictionary.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        dict[row[0]] = row[1]
    #print(dict)

# opening input file in read mode
fin = open("t8.shakespeare.txt", "rt")

# opening output file in write mode
fout = open("out.txt", "wt")

# translation
for line in fin:
    words = line.split()

    # handling sentences with no words
    if(len(words)==0):
        fout.write(line)
        continue

    # handling sentences with 1 number in center alignment
    if(len(words)==1):
        if(words[0].isnumeric()):
            fout.write(line)
            continue

    # handling other cases
    sentence = ""
    for word in words:
        lower_case_word = word.lower()

        # handling if word present in french dictionary
        if(lower_case_word in dict.keys()):
            # handling if word is in upper case
            if(word.isupper()):
                sentence+=dict[lower_case_word].upper()+" "
            # handling if word is capitalized
            elif(word[0].isupper()):
                sentence += dict[lower_case_word].capitalize() + " "
            # handling other cases
            else:
                sentence += dict[lower_case_word] + " "

        # handling if word present in french dictionary
        else:
            sentence += word + " "

    #last space character is ignored
    fout.write(sentence[:-1])
    fout.write("\n")

#close input and output files
fin.close()
fout.close()