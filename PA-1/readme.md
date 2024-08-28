## PA-1 Documentation
### **ALPHABET SOUP PROBLEM**: Create a function that takes a string and returns a string with its letters in alphabetical order.
##### Example:
##### alphabet_soup(“hello”) ➞ ehllo
##### alphabet_soup(“hacker”) ➞ acehkr
##### **Code**:
![image](https://github.com/user-attachments/assets/848f6fe8-2303-4724-b0b7-fc5535c45227)
- ##### **line2**: Function named "alphabet_soup" is defined. It accepts an argument named "str."
- ##### **line4**: String "str" is sorted and at the same time converted to list using the "sorted()" function. The string at hand is also lowercased through the ".lower()" function.
- ##### **line6-7**: The while loop goes through the converted list to check and remove for any whitespaces. This would be helpful in cases where strings have whitespaces.
- ##### **line9**: List is converted back to string by ajoining individual elements using the ".join()" function. String is returned and printed at the same time.
- ##### **line12-14**: The function is called three times, each having different arguments.
##### **Output**:
![image](https://github.com/user-attachments/assets/7661fc5c-a07e-471a-9afc-a5ca9e4957b2)

### **EMOTICON PROBLEM**: Create a function that changes specific words into emoticons. Given a sentence as a string, replace the words smile, grin, sad and mad with their corresponding emoticon:
##### Example:
##### emotify(“Make me smile”) ➞ Make me :)
##### emotify(“I am mad”) ➞ I am >:(
##### **Code**:
![image](https://github.com/user-attachments/assets/ea220c73-5245-4d71-95da-693df483d5e1)
- ##### **line2**: Function named "emotify" is defined. It accepts an argument named "words."
- ##### **line4-9**: Dictionary named "emoticons" is initialized. The keys are in the form of words, while the values correspond to each of the word's respective emotes.
- ##### **line11-14**: A "for" loop goes through the dictionary's items then performs the condition whether a key is present in the string "words". If condition is true, a replacement between key and value is done through the ".replace()" function.
- ##### **line16**: The original statement is returned if previous condition is evaluated to false.
- ##### **line19-20**: The function is called two times, each having different arguments.
##### **Output**:
![image](https://github.com/user-attachments/assets/d68793d8-afe8-474e-92f8-286dacd26bf2)

### **UNPACKING LIST PROBLEM**: Unpack the list writeyourcodehere into three variables, being first, middle, and last, with middle being everything in between the first and last element. Then print all three variables
##### Example: lst = [1, 2, 3, 4, 5, 6]
##### Output: first: 1  middle: [2, 3, 4, 5]  last: 6
##### **Code**:
![image](https://github.com/user-attachments/assets/fe547d2b-5198-4ed4-8346-c0f820a8e3dc)
- ##### **line2**: A list named "lst" is initialized with values 1 to 6.
- ##### **line5**: A variable named "first" is initialized with the first value in "lst" through indexing.
- ##### **line6**: A variable named "middle" is initialized in the same way, but instead holds the values of "lst" between the first and last index.
- ##### **line7**: A variable named "last" is initialized with the last value in "lst."
- ##### **line10-12**: The three variables are printed in order.
##### **Output**:
![image](https://github.com/user-attachments/assets/1ff89db3-5dee-4111-9569-1c3bd477492a)
