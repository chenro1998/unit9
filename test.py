# Kevin Chen
# 11/16/17
# This file will use others commands from others files

import dog
import pack

mydog = dog.Dog("Abby")

mydog2 = dog.Dog("Ace")

mydog3 = dog.Dog("Pepper")

mydog4 = dog.Dog("Frisco")

mydog5 = dog.Dog("Happy")

mydog3.laydown()

mydog.print_name()

mydog.sit()

code = pack.Pack(mydog)

code.add_member(mydog2)

code.add_member(mydog3)

code.add_member(mydog4)

code.add_member(mydog5)

code.new_leader(3)

print(code.get_leader_name())

code.all_sit()

code.all_print_tricks()
