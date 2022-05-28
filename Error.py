"""
Author: masakokh
Year: 2022
Version: 1.0.0
Package: project
"""


class Error:
	"""

	"""
	def __int__(self):
		"""

		"""
		self.__errorMessage	= ''
		self.__isError		= False

	def getErrorMessage(self) -> str:
		"""

		:return:
		"""
		return self.__errorMessage

	def isError(self) -> bool:
		"""

		:return:
		"""
		return self.__isError

	def setError(self, message: str) -> None:
		"""

		:param message:
		:return:
		"""
		self.__errorMessage	= f'{message}'
		self.__isError		= True

	def setErrorNo(self) -> None:
		"""

		:return:
		"""
		self.__errorMessage	= ''
		self.__isError		= False
