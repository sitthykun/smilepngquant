"""
Author: masakokh
Year: 2021
Version: 1.0.0
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

	def __setError(self, message: str) -> None:
		"""

		:param message:
		:return:
		"""
		self.__errorMessage	= message
		self.__isError		= True

	def __setErrorNo(self) -> None:
		"""

		:return:
		"""
		self.__errorMessage	= ''
		self.__isError		= False

	def compress(self, filename: str, quality: int= 50, removeFile: bool= True) -> None:
		"""

		:param filename:
		:param quality:
		:param removeFile:
		:return:
		"""
		try:
			# validate extension first
			if (os.path.basename(filename).split(".", 1)[1]).lower() != self.__extension:
				# error
				self.__setError('Wrong extension')

			else:
				# set default
				self.__setErrorNo()
				self.__quality	= quality
				# set new filename
				self.__filename	= f'{os.path.dirname(filename)}{os.path.basename(filename).split(".", 1)[0]}.{self.__extension}'

				# validate and set default
				if self.__quality > 100 or self.__quality < 20:
					self.__quality	= 50

				# command
				# you have to install pngquant first
				cmd			= [
					# that is the default location
					'/usr/local/bin/pngquant'
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

				#
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
