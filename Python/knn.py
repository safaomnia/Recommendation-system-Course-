def recommend(self, user):

	"""Give list of recommendations"""
	recommendations = {}
	nearest = self.computeNearestNeighbor(user) # first get list of users ordered by nearness
	userRatings = self.data[user] # now get the ratings for the user

	# determine the total distance
	totalDistance = 0.0
	for i in range(self.k):
	totalDistance += nearest[i][1]

	# now iterate through the k nearest neighbors
	# accumulating their ratings
	for i in range(self.k):
		weight = nearest[i][1] / totalDistance
		name = nearest[i][0] # get the name of the person
		neighborRatings = self.data[name] # get the ratings for this person

		# now find bands neighbor rated that user didn't
		for artist in neighborRatings:

			if not artist in userRatings:

				if artist not in recommendations:
				recommendations[artist] = (neighborRatings[artist] * weight)
				else:
				recommendations[artist] = (recommendations[artist] + neighborRatings[artist] * weight)

	# now make list from dictionary
	recommendations = list(recommendations.items())
	recommendations = [(self.convertProductID2name(k), v)
						for (k, v) in recommendations]
	# finally sort and return
	recommendations.sort(key=lambda artistTuple: artistTuple[1],
	reverse = True)
	return recommendations[:self.n]
