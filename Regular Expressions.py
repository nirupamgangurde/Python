import re

pattern = r"[A-Z]+yclone"
text = '''During the first part of your life, you only become aware of happiness once you have lost it. Then an age comes,
a second one, in which you already know, at the moment when you begin to experience true happiness, that you are, 
at the end of the day, going to lose it. When I met Belle, I understood that I had just entered this second age. 
I also understood that I hadn’t reached the third age, in which anticipation of the loss of happiness prevents you from 
living Cyclone, Dyclone.'''

matches= re.finditer(pattern, text)
for match in matches:
    print(match)