NONE = -1

#================================================================
class Cell:
#================================================================
# Methods:
	#--------------------------------------------------------
	# - Cell Constructor
	#--------------------------------------------------------
	# * solution : The correct answer for this cell.
	# * mutable : is this cell read-only or to-be-solved?
	#--------------------------------------------------------
	def __init__(self, solution, mutable = True):
		self.solution_ = solution
		self.mutable_ = mutable

		self.answer_ = NONE if mutable else solution

	#--------------------------------------------------------
	# - Get Current Given Answer
	#--------------------------------------------------------
	# returns the current answer for this cell, as given by
	# the user or provided by default.
	#--------------------------------------------------------
	def getAnswer(self):
		return self.answer_

	#--------------------------------------------------------
	# - Submit Answer
	#--------------------------------------------------------
	# sets the answer for this cell to the provided argument
	# IF the cell is mutable.
	#--------------------------------------------------------
	def submitAnswer(self, answer):
		if(self.mutable_):
			self.answer_ = max(NONE, min(answer, 9))
		return self.isCorrect()			

	#--------------------------------------------------------
	# - Is This Cell Mutable ?
	#--------------------------------------------------------
	# returns True if this cell is to be solved by the user,
	# and False if it is a provided answer.
	#--------------------------------------------------------
	def isMutable(self):
		return self.mutable_

	#--------------------------------------------------------
	# - Is This Cell Correct ?
	#--------------------------------------------------------
	# returns True if the answer given and the true solution
	# match, and False otherwise.
	#--------------------------------------------------------
	def isCorrect(self):
		return self.answer_ == self.solution_

	#--------------------------------------------------------
	# - Get Correct Solution
	#--------------------------------------------------------
	# returns the true solution to this cell.
	#--------------------------------------------------------
	def getSolution(self):
		return self.solution_

# Members:
	answer_ = NONE
	solution_ = NONE
	mutable_ = False
#================================================================
