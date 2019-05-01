"""Restaurant rating lister."""

# put your code here

def get_restaurant_info(file):
	restaurant_ratings = {}
	restaurant_data = open(file)
	for restaurant in restaurant_data:
		restaurant = restaurant.rstrip().split(":")
		restaurant_ratings[restaurant[0]] = restaurant[1]
	restaurant_data.close()

	new_restaurant_name = input("Can we get the name of the restaurant?")
	restaurant_score = input("Give it a rating")
	restaurant_ratings[new_restaurant_name] = restaurant_score

	restaurants_sorted = sorted(list(restaurant_ratings.keys()))
	for restaurant_sorted in restaurants_sorted:
		print('{} is rated at {}'.format(restaurant_sorted, restaurant_ratings[restaurant_sorted]))

get_restaurant_info("scores.txt")


