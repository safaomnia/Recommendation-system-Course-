""" After calculate Distance with manhattan, euclidiean, kiwinskoski or cos 
we define the these functions """
def computeNearestNeighbor(username, users):
	 
	"""creates a sorted list of users based on their distance to
	username"""
	distances = []
	 
	for user in users:
	 
		if user != username:
		 	distance = manhattan(users[user], users[username])
		 	distances.append((distance, user))
	# sort based on distance -- closest first
	distances.sort()
	return distances

def recommend(username, users):
 
 	nearest = computeNearestNeighbor(username, users)[0][1] # first find nearest neighbor
	recommendations = []
	neighborRatings = users[nearest] # now find bands neighbor rated that user didn't
	userRatings = users[username]
	 
	for artist in neighborRatings:
	 
		if not artist in userRatings:
		    recommendations.append((artist, neighborRatings[artist]))
		 
	# using the fn sorted for variety - sort is more efficient
	return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)