# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas

df = pandas.read_csv("Day 26 - NATO Alphabet Project/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter : row.code  for (index, row) in df.iterrows()}
 
word = input("Enter a word: ").upper()


output_list = [phonetic_dict[letter] for letter in word]
print(output_list)

