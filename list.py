from collections import Counter
sentence = "This is a common question in interviews"
# Removing spaces to count only the characters
sentence = sentence.replace(" ", "")
# Using Counter to count the frequency of each character.e
char_count = Counter(sentence)
# Finding the most common character
max_frequency = max(char_count.values())
most_common_chars = [char for char, count in char_count.items() if count == max_frequency]
print(f"The most common character(s) is/are: {', '.join(most_common_chars)} with a frequency of {max_frequency}.")