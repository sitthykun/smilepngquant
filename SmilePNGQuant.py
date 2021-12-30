"""
Author: masakokh
Year: 2021
Version: 1.0.1
Package: project
"""
import os
import subprocess


class SmilePNGQuant:
	"""

	"""
	def __init__(self):
		"""

		"""
		self.__errorMessage	= ''
		self.__extension	= 'png'
		self.__filename		= ''
		self.__isError		= False
		self.__quality		= 0
		self.__pngquantPath	= '/usr/local/bin/pngquant'

	def __setError(self, message: str) -> None:
		"""

		:param message:
		:return:
		"""
		self.__errorMessage	= f'{message}'
		self.__isError		= True

	def __setErrorNo(self) -> None:
		"""

		:return:
		"""
		self.__errorMessage	= ''
		self.__isError		= False

	def compress(self, filename: str, quality: int= 50, removeFile: bool= True, newFilename: str= '_new') -> None:
		"""

		:param filename:
		:param quality:
		:param removeFile:
		:param newFilename:
		:return:
		"""
		try:
			# validate extension first
			if not os.path.exists(filename):
				# error
				self.__setError(f'File not found: {filename}')

			# double-check
			elif (os.path.basename(filename).split('.', 1)[1]).lower() != self.__extension:
				#
				self.__setError('Wrong extension')

			#
			else:
				# set default
				self.__setErrorNo()
				self.__quality	= quality

				# need removing
				if removeFile:
					# set new filename and keep it
					self.__filename = f'{os.path.dirname(filename)}/{newFilename}.{self.__extension}'

				else:
					# override current file
					self.__filename = f'{filename}'

				# validate and set default
				# maximum
				if self.__quality > 100:
					self.__quality	= 100

				# minimum is 10
				elif self.__quality < 10:
					self.__quality	= 10

				# command
				# you have to install pngquant first
				cmd			= [
					# that is the default location
					self.__pngquantPath
					# it's able to set in range 60 to 80
					# but below, it sets fix
					, f'--quality={self.__quality}-{self.__quality}'
					, filename
					, '--output'
					, self.__filename
				]

				# run a process
				process		= subprocess.run(
					cmd
					, stdout= subprocess.PIPE
					, stderr= subprocess.PIPE
				)

				# no error
				if process.returncode == 0:
					# remove old if it's true
					if removeFile:
						# no regret
						os.remove(filename)

				else:
					# got the new error message
					self.__setError(str(process.stderr))

		except Exception as e:
			self.__setError(str(e))

	def getErrorMessage(self) -> str:
		"""

		:return:
		"""
		return self.__errorMessage

	def getFilename(self) -> str:
		"""

		:return:
		"""
		return self.__filename

	def getQuality(self) -> int:
		"""

		:return:
		"""
		return self.__quality

	def getPath(self) -> str:
		"""

		:return:
		"""
		return f'{os.path.dirname(self.__filename)}/'

	def isError(self) -> bool:
		"""

		:return:
		"""
		return self.__isError

	# def setFilename(self, filename: str) -> None:
	# 	"""
	#
	# 	:param filename:
	# 	:return:
	# 	"""
	# 	self.__filename		= filename

	def setPngQuant(self, path: str) -> None:
		"""

		:param path:
		:return:
		"""
		self.__pngquantPath	= path
