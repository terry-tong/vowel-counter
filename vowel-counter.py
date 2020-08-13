def vowel_counter():
    sentence = input("Type your sentence here: ")
    count = 0
    vowel = 0
    while count < len(sentence):
        if sentence[count] in 'aeiouAEIOU':
            vowel += 1
        count += 1
    if vowel == 1:
        print('Your sentence has {} vowel.'.format(vowel))
    else:
        print('Your sentence has {} vowels.'.format(vowel))

vowel_counter()