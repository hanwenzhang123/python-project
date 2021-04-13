# create a new empty list named shopping_list
shopping_list = []


def show_help():
  print('what should we pick up at the store?')
  print("""
Enter "DONE" to stop adding itmes.
Enter "HELP" for this help.
Enter "SHOW" for showing the list.
""")
  
  
# create a function named add_to_list that declares a parameter named item
def add_to_list(item):
    # add the item to the list
     shopping_list.append(item)
      #notify user that the item was added, and state the number in the list currently
      print('Added! List has {} items.".format(len(shopping_list)))
 
            
# define a function named show_list that prints all the items in the list
def show_list():
     print("Here is your list: ")
      for item in shopping_list:
      print(item)
            
            
show_help() # first thing shown on the application

while True:   # while true - always true. this loop will run forever unless something interrupt
  new_item = input ('>')
  
  if new_item == 'DONE':
    break   # when we use break, this loop done
  elif new_item == 'HELP':
    show_help()
    continue  # continue as while true
# Enable the SHOW command to show the list. Update the HELP document. Make sure to run it. 
   elif new_item == 'SHOW':  
    show_list()
    continue
            
    # call add_to_list with new_item as an argument
    add_to_list(new_item)

 show_list() #when you done, you show the list
    
    
    
