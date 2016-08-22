#!/usr/bin/env python
# -*- coding: utf-8 -*-


from extractFunctions import extractFunctions

import tokenize
import re
import string
import collections
import types


class lexicalanalysis():
	def __init__(self, input_file):
		file_in = open(input_file, 'r')
		funcs = extractFunctions(file_in)
		file_in = open(input_file, 'r')
		# self.record = self.lexicalAnalysis(file_in, funcs)
		self.record = {}
		self.GTP = {}
		self.record, self.GTP = self.lexicalAnalysis(file_in, funcs)
		file_in.close()

	def getAnalysisResults(self):
		return self.record, self.GTP

	def lexicalAnalysis(self, file_in, funcs):
		record = {}
		current_line = 0
		marks = ['(',')','[',']','{','}',',',':',';','.','@']
		def handle_token(type, token, (srow, scol), (erow, ecol), line):
			if tokenize.tok_name[type] == 'COMMENT':
				pass
			else:
				token = token.strip()
				if len(token) == 0:
					return
				if token[:3] == '"""' or token[:3] == "'''":
					return
				if token in marks:
					return
				if (token[0] == '"' and token[-1] == '"') or (token[0] == "'" and token[-1] == "'"):
					token = token[1:-1]
					token = token.split(' ')
					for i in token:
						t = i.strip()
						if len(t)==0:
							token.remove(i)
				if srow in record:
					if isinstance(token, types.ListType):
						for i in token:
							# print i
							record[srow].append([scol, i])
					else:
						record[srow].append([scol, token])
				else:
					record[srow] = []
					if isinstance(token, types.ListType):
						# print i
						record[srow].append([scol, i])
					else:
						record[srow].append([scol, token])
		try:
			tokenize.tokenize(file_in.readline, handle_token)

			file_in.close()
			result = {}
			GTP_result = {}
			for (start, end) in funcs:
				result[(start, end)] = []
				for line in range(start, end + 1):
					if line in record.keys():
						for part in record[line]:
							result[(start, end)].append(part[1].lower())
							GTP_result[part[1].lower()] = GTP_result.get(part[1], 0) + 1

			return result, GTP_result
		except Exception,e:
			print Exception,':',e
			return [], []


if __name__ == '__main__':
	test_input_folder = 'sort_codes'
	test_input_file = 'SmithWaterman.py'
	lAnalysis = lexicalanalysis(test_input_folder, test_input_file, True)