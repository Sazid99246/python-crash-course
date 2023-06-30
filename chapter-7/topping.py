prompt = 'Please tell me about some of your favorite toppings to add on the pizza:'
prompt += "\nEnter 'quit' when you are done. "

active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print("I will add " + topping + " on the pizza.")
