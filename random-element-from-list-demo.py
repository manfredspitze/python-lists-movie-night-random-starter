# Abe Lincoln
# 28 AUG 20XX
# Select Random Element from List


# Example 1
# Import the random module first
import random

# Define your list
movie_list = ['The Godfather', 'The Wizard of Oz', 'Top Gun', 'The Shawshank Redemption', 'Pulp Fiction']

# Select a movie at random from list
movie = random.choice(movie_list)

# Display the randomly selected movie title
print(movie)


# Example 2
# We've already imported the random module, so we don't need
# to import it again for this example
us_states = ['Missouri', 'Oklahoma', 'Nevada', 'Arizona', 'California', 'Texas']

# Use random.choice() method to select a state at random from the list of states
state = random.choice(us_states)

# Remove the state from the list if the list of states is not empty
if len(us_states) > 0:
  print(f'Removed the state of {state} from the list of states.')
  us_states.remove(state)
else:
  print('Sorry, but the list of U.S. states was empty!')
  print(f'Cannot remove {state} from the list of states.')
  print('Goodbye!)
