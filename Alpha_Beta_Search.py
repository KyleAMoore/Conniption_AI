from Conniption import Conniption
import time

## Global dictionary to save states and their evaluations
visited = {}

class AlphaBeta:

	##Parameters:
	#   board - Conniption object which holds the state of the board
	#   max_depth - a integer representing the depth the min-max search
	#	
	#	Outputs - a Conniption object with the best next move based on the max search depth
	def alpha_beta_search(self, board, max_depth):
		self.max_depth = max_depth
		infinity = float('inf')
		alpha = -infinity
		beta = infinity

		depth = 0
		best_state = None
		board.genChildStates()

		value = 0
		for state in board.children:
			value = self.min_value(state, depth+1, alpha, beta)
			if value > alpha:
				alpha = value
				best_state = state
		#print("alpha: "+str(alpha)) #For testing purposes
		return best_state, value

	##Parameters:
	#	state - Conniption object that contains future state of the board
	#	depth - Integer that holds the current depth of the search
	#	alpha - holds the max value
	#	beta - holds the min value
	# 	
	#	Note: recursion helper method of finding the max value for a given depth
	def max_value(self, state, depth, alpha, beta):
		if depth >= self.max_depth:
			global visited
			if state in visited:
				#print("found in dict")
				return visited.get(state)
			else:
				eval = state.evalBoard()
				visited[state]= eval
				return eval

		infinity = float('inf')
		value = -infinity
		state.genChildStates()

		for s in state.children:
			value = max(value, self.min_value(s, depth+1, alpha, beta))
			if value >= beta:
				return value
			alpha = max(alpha, value)
			#print("alpha: "+str(alpha)) #For Testing purposes
		return value

	##Parameters:
	#	state - Conniption object that contains future state of the board
	#	depth - Integer that holds the current depth of the search
	#	alpha - holds the max value
	#	beta - holds the min value
	# 	
	#	Note: recursion helper method of finding the max value for a given depth
	def min_value(self, state, depth, alpha, beta):
		if depth >= self.max_depth:
			global visited
			if state in visited:
				#print("found in dict")
				return visited.get(state)
			else:
				eval = state.evalBoard()
				visited[state] = eval
				return eval

		infinity = float('inf')
		value = infinity
		state.genChildStates()

		for s in state.children:
			value = min(value, self.max_value(s, depth+1, alpha, beta))
			if value <= alpha:
				return value
			beta = min(beta, value)
			#print("beta: "+str(beta)) #For testing purposes
		return value

##Generate a random board for testing purposes
if __name__ == "__main__":
	t, f  = True, False
	b = ((t,f),(f,t),(t,f),(f,t),(t,f),(f,t),(t,f))
	testBoard = Conniption(b, True, (4,4), True)
	search = AlphaBeta()
	start = time.time()
	result = search.alpha_beta_search(testBoard,6)
	print(time.time() - start)
	print(result[0],'\nScore for player is',result[1])
