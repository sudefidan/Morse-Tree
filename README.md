# **WORKSHEET2 - MORSE TREE**

A python module that creates a binary tree for morse code. By using that module you can do translation between morse code and sentence. 

The Morse tree is a binary tree where each node represents a symbol in Morse code, either a dot or a dash. The root node represents the null character, and the left child of each node represents a dot, while the right child represents a dash.
 
This is what a binary tree morse code looks like:

![Morse Tree](https://user-images.githubusercontent.com/47689166/57795916-d0c1e300-774f-11e9-8989-7d2dc6b7e531.png) 

## **Implementations**
**Morse Tree Implementation :** * Tree is implemented with is_empty(), is_not empty(), insert(), find(), decode(), encode(), print_tree() functions.*

**Unit Test Implementation:** *Test are done using assertIn(), assertNotIn(), assertEqual(), assertNotEqual(), assertCountEqual(), assertTrue(), assertFalse(), assertIs(), assertIsNot().*


## **Usage**
* Translation from morse code to text and text to mrose code under main.py.
* Printing morse tree with each node's position under main.py.
* Unit testing under morseunit.py.

## **Example Usage**

### **Main.py**

**User can translator from text to morse and morse to text:**
```python
#messages
print('--------TEXT TO MORSE-------------')
text_message = input(('Enter text to encode ==> '))
encoded = morse.encode(text_message)
print('Encoded message: ' + encoded)

print('--------MORSE TO TEXT-------------')
morse_message = input(('Enter morse to decode ==> '))
decoded = morse.decode(morse_message)
print('Decoded message: ' + decoded) 
```
Expected Output:

![printing morse tree](images/translator_terminal.jpg)

Here is some other examples with their expected output to try:
Text  | Morse
------------- | -------------
Sude Fidan  | ... ..- -.. . / ..-. .. -.. .- -.
2023 + 2017 | ..--- ----- ..--- ...-- / .-.-. / ..--- ----- .---- --..
WE LOVE PC ! | .-- . / .-.. --- ...- . / .--. -.-. / -.-.--


**User can also print morse tree with their position:**
```python

#printing morse tree
morse.print_tree(morse.root)
```
Expected Output:

![printing morse tree](images/print_tree_terminal.jpg)

### **Morseunit.py**
**Program has some unit testing if user wants to test. There are 7 tests available:**

1. Testing for encode() function:

Assert Function | Message         | Encoded Version     | Message 2   | Comparision
-------------   | ------------- | ------------- | ------------- | ------------- 
assertIn() | here | .... . .-. . | .. / .- -- / .... . .-. . | True 
assertEqual() | Sude Fidan | ... ..- -.. . / ..-. .. -.. .- -. |... ..- -.. . / ..-. .. -.. .- -.| True
assertCountEqual() | 2023 | ..--- ----- ..--- ...-- | ..--- ----- ..--- ...-- | True
assertEqual() | 2023 + 2017 | ..--- ----- ..--- ...-- / .-.-. / ..--- ----- .---- --... | ..--- ----- ..--- ...-- / .-.-. / ..--- ----- .---- --... | True
assertEqual()| FIDAN | ..-. .. -.. .- -. | ..-. .. -.. .- -.| True
assertEqual()| WE LOVE PC ! | .-- . / .-.. --- ...- . / .--. -.-. / -.-.-- | .-- . / .-.. --- ...- . / .--. -.-. / -.-.--| True
assertNotIn() | benedict |-... . -. . -.. .. -.-. - | -... . -. . -.. | False
assertNotEqual() | internet of the things | .. -. - . .-. -. . - / --- ..-. / - .... . / - .... .. -. --. ... | .. -. - . .-. -. . - / --- ..-. / - .... . / - .... .. -. --. | False

1. Testing for decode() function

Assert Function | Message         | Decoded Version     | Message 2   | Comparision
-------------   | ------------- | ------------- | ------------- | ------------- 
assertIn() | ... ..-. | SF| SF IS MY CAPITALS | True 
assertEqual()| ...- ... -.-. --- -.. . | VSCODE |VSCODE|True
assertCountEqual() |- .... . / . -. -.. | THE END | THE END| True
assertEqual() | ..--- ----- ..--- ...-- / -....- / ..--- ----- ..--- ....- | 2023 - 2024 | 2023 - 2024| True
assertNotEqual() | .. -. - . .-. -. | INTERN | INTERNET| False
assertNotIn() | - .... .. -. --. . | THINGE | I WAS BORN IN 2002 |False


1. Testing for is_empty() function

Assert Function | Function | True/False
-------------   | ------------- | -------------  
assertFalse() | tree.is_empty() | True 

4. Testing for is_not_empty() function
   
Assert Function | Function | True/False
-------------   | ------------- | -------------  
assertTrue() | tree.is_not_empty() | True 

5. Testing for find() function

Assert Function | Char | Decoded Version | Location | True/False
-------------   | ------------- | -------------  | ------------- | -------------
assertIn() | .- | A | *morse.dictionary* | True 
assertIn() | ...| S | SUDE| True 

6. Testing for insert() function
   
Assert Function | Symbol | Morse | Is Inserted ?| True/False
-------------   | ------------- | -------------  | ------------- | ------------- 
assertNotIn() | @ | .--.-. |No | True 
assertIn() | @| .--.-.| Yes | True
assertNotIn() | *Not Valid* | .........| No | True 

1. Testing for additional symbols
   
Assert Function | Message         | Translation     | Message 2   | Comparision
-------------   | ------------- | ------------- | ------------- | ------------- 
assertEqual() | .-.-.- | . | . | True
assertEqual() | ..--.- | _ | _ | True
assertIs() | -....- | - | - | True 
assertIs() | --...- | ¡ | ¡| True
assertEqual() | ..--.. -.-.-- | ?! | ?!| True
assertEqual() | -.--. / -.--.- | ( ) | ( )| True
assertIn() | ...-..- | $| $€£ | True
assertIn() | .----.| ’| ’| True
assertIn() | ---...| : | *morse.dictionary* | True
assertIn() | + | .-.-. | *morse.dictionary* | True
assertCountEqual() | & | .-... | .-... | True
assertCountEqual() | - | -....- | -....- | True
assertNotIn() | ¿¿¿ | ..-.- ..-.- ..-.- | *morse.dictionary* | False
assertNotEqual() | -.-.-. | ;| A | False
assertNotEqual() | -.-.-. | *Not Valid* | ” | False
assertIsNot() | , | --..-- | ..--.- | False




After running all tests expected output:

![printing unit testing](images/unit_testing_terminal.jpg)


## **Installation** 📚
❗ User does not need to install any packages.

## **Maintainers** 🤓
Sude Fidan(@s2-fidan)
## **Referencing**

