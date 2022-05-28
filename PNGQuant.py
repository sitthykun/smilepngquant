"""
Author: masakokh
Year: 2021
Version: 1.1.1
Package: project
"""
import os
import subprocess
# internal
from .Error import Error


class PNGQuant:
	"""

	"""
	def __init__(self, pngquantPath: str= ''):
		"""

		:param pngquantPath:
		"""
		# private
		self.__extension	= 'png'
		self.__filename		= ''
		self.__quality		= 0
		self.__pngquantPath	= pngquantPath
		# public
		self.error			= Error()

	def __foundPngQuantSDKPath(self) -> bool:
		"""

		:return:
		"""
		# the default path in ubuntu
		defaultPath	= '/usr/local/bin/pngquant'

		# verify
		if self.__pngquantPath and os.path.isfile(self.__pngquantPath):
			return True

		elif os.path.isfile(defaultPath):
			# set default
			# but nonsense to set here, but, it saves some process
			self.setPngQuant(path= defaultPath)
			return True

		else:
			# set error
			self.error.setError('The pngquant sdk path\'s not found.')
			return False

	def compress(self, filename: str, quality: int= 50, newFilename: str= '', dirname: str= '') -> None:
		"""

		:param filename:
		:param quality:
		:param newFilename:
		:param dirname:
		:return:
		"""
		# verify sdk path
		if self.__foundPngQuantSDKPath():
			# put in try catch
			try:
				# if no newFilename and dirname
				needRemove      = False
				tempFileMove    = ''

				# validate extension first
				if not os.path.exists(filename):
					# error
					self.error.setError(f'File not found: {filename}')

				# double-check
				elif (os.path.basename(filename).split('.', 1)[1]).lower() != self.__extension:
					#
					self.error.setError('Wrong extension')

				# found file
				else:
					# set default
					self.error.setErrorNo()
					self.__quality	= quality

					# need removing
					if newFilename and dirname:
						# make sure no backslash at the end
						self.__filename = f'{os.path.dirname(dirname)}/{newFilename}.{self.__extension}'

					elif newFilename:
						# set new filename and keep it
						self.__filename = f'{os.path.dirname(filename)}/{newFilename}.{self.__extension}'

					elif dirname:
						# the same directory
						if os.path.dirname(dirname) == os.path.dirname(filename):
							# name with extension
							self.__filename = f'{os.path.dirname(dirname)}/{os.path.basename(filename)}_new.{self.__extension}'
							# remove the exist
							needRemove      = True
							# move the exist file
							if os.path.exists(self.__filename):
								# move to temp
								tempFileMove    = f'/tmp/{os.path.basename(self.__filename)}'
								#
								os.rename(
									self.__filename
									, tempFileMove
								)

						else:
							# name with extension
							self.__filename = f'{os.path.dirname(dirname)}/{os.path.basename(filename)}'

					else:
						# override current file
						needRemove      = True
						self.__filename = f'/tmp/123456ABCDEF789_ukLepAeSeceSe3fsaEF_HnesieceS2_seq.{self.__extension}'

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
						if needRemove:
							# remove the old and rename new file to old name
							os.remove(filename)

							# rename
							os.rename(
								self.__filename
								, filename
							)

							# name the filename to the file
							self.__filename = filename

					else:
						# file has been moving to tmp for a while
						if tempFileMove:
							# move back the file
							os.rename(
								tempFileMove
								, f'{os.path.dirname(self.__filename)}/{os.path.basename(tempFileMove)}'
							)
						# got the new error message
						self.error.setError(str(process.stderr))

			except Exception as e:
				self.error.setError(str(e))
				print(str(e))

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

	def setPngQuant(self, path: str) -> None:
		"""

		:param path:
		:return:
		"""
		self.__pngquantPath	= path
