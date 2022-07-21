
from unicodedata import name
from classes.animal import Animal
from classes.dog import Dog
from classes.cat import Cat

max = Animal( "Max", "Alex" )
max.print_info()

jagger = Dog( "Jagger", "Alfredo", "Golden Retriever", "Golden" )
jagger.print_info()
jagger.walk_animal()

chester = Cat( "Chester", "Alfredo", "Yellow", 6 )
chester.print_info()
chester.walk_animal()

first-name = input( "Please                                                                                                                                                                                                                                                                                                             ")
