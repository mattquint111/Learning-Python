# Optional Dictionary Exercises

# Ex.1
phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}
# #1.
# print(phonebook_dict['Alice'])
# # 2.
# phonebook_dict['Kareem'] = '938-489-1234'
# # 3.
# del phonebook_dict['Alice']
# # 4.
# phonebook_dict['Bob'] = '968-345-2345'
# # 5.
# for number in phonebook_dict.values():
#     print(number)
# print(phonebook_dict)

# Ex.2 Nested Dictionaries
ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
# # 1.
# print(ramit['email'])
# # 2.
# print(ramit['interests'][0])
# # 3.
# print(ramit['friends'][0]['email'])
# # 4.
# print(ramit['friends'][1]['interests'][1])

# Letter Summary
# def letter_histogram():
#     word = input("Enter a word: ")
#     letter_list = []
#     histogram = {}

#     for i in word:
#         letter_list.append(i)
#     sorted_list = sorted(letter_list)

#     for i in sorted_list:
#         if i in histogram:
#             histogram[i] += 1
#         else:
#             histogram[i] = 1
#     return histogram

# print(letter_histogram())

# Word Summary
def word_summary():
    sentence = input("Enter a sentence: ")
    word_list = sentence.split(' ')
    word_dict = {}

    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict

#print(word_summary())

# Bonus Challenge
word_histogram = word_summary()


def histogram_tally(dict):
    key_list = []
    value_list = []
    
    for key in dict:
        key_list.append(key)
        value_list.append(dict[key])
    print(key_list)
    print(value_list)
histogram_tally(word_histogram)
    





#Sum of digit of numbers
# def is_equal(num1, num2):
#     number_string1 = str(num1)
#     number_list1 = [int(i) for i in number_string1]
#     number_string2 = str(num2)
#     number_list2 = [int(i) for i in number_string2]
    
#     return sum(number_list1) >= sum(number_list2)

# print(is_equal(105, 42))