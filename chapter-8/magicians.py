def show_magicians(magicians):
    print("Here are the name of the top 5 world famous magicians in the world: ")
    for magician in magicians:
            print(magician.title())

def make_great(magicians):
    for magician in magicians:
         print("Great " + magician.title())
      

top_magicians = ["david copperfield", "criss angel", "derren brown", "harry houdini", "ricky jay"]
show_magicians(top_magicians)
make_great(top_magicians)