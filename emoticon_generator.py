#emoticon_generator.py
import random
eyes_list = [':', ';']
noses_list = ['-', '+']
mouths_list = [')', '(']
eyes = random.choice(eyes_list)
nose = random.choice(noses_list)
mouth = random.choice(mouths_list)
print(eyes + nose + mouth)
