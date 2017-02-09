from random import choice
from string import ascii_lowercase

def rollout_proctor():
	 proctor = ''.join(choice(ascii_lowercase)for i in range(12))
	 return proctor


	
