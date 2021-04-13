SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100

# create the calculate_price function. it takes number of tickets and returns
# num_tickets * TICKET_PRICE
def calculate_price(number_of_tickets):
  # create a new constant for $2 service charge and add the servicce charge to the result
 return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

# run this code continuously until we run out of ticket, more than 0 is true
while tickets_remaining >= 1:

  # output how many tickets are remaining using the tickets_remaning variable
  print('there are {} tickets remaining.'.format(tickets_remaining))

  # gather the user's name and assign it to a new variable
  name = input(' what is your name?' )

  #prompt the user by name and ask how many tickets they would like
  num_tickets = input ('how many tickets would you like, {}?'.fomat(name))
  
  # expect a ValueError to happen and handle it apprropriately
  try:
      num_tickets = int(num_tickets)
      # raise a ValueError if the requests is for more tickets than are available
      if num_tickets > tickets_remaining:
          raise ValueError ('there are only {} tickets remaining'.format(tickets_remaining))
  except ValueError as err:
      # include the error text in the output
      print('oh no, we ran into an issue. {}. Please try again.'.format(err))
  else:
    #calculate the price (number of tickets multiplie by the price) and assign it to a variable
 .   amount_due = calculate_price(num_tickets)

    #output the price to the screen
    print('the total due is ${}'.format(amount_due))

    # prompt user if they want to proceed. Y/N?
    should_proceed = input ('Do you want to proceed? Y/N ')

    # if they want to proceeed
    if should_proceed.lower() === 'y':
      # print out to the screen 'SOLD!' to confirm purchase
      # TODO: gather cc information and process it.
      print('SOLD!')
      # and then decrement the tickets remaining by the number of tickets purchased
      tickets_remaining -= num_tickets
    # otherwise...
    else:
      # thank them by name
      print('Thank you anyways, {}!'.format(name))
      
# notify the user that the tickets are sold out
print('sorry the tickets are all sold out!!! :(')
