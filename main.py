#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lexicalAnalysis_function import lexicalanalysis
from getRepresentations import getReps
from detectLinks import detectLinks

import os
from os import listdir
from os.path import isfile, join
import collections
import time


class linkDetect(object):
	def __init__(self, input_folder, threshold):
		start = time.time()
		self.threshold = threshold
		self.coderecords, self.GTPrecords, self.majortoken = self.lexiAnalysis(input_folder)
		self.codereps = {}
		self.codeminorreps = {}
		self.minortokens = {}
		self.coderepmanager = {}
		self.links = {}
		self.GTP = self.getGTP()
		print 'total tokens recorded: %d' %len(self.GTPrecords)
		print 'total major tokens recorded: %d' %len(self.majortoken)
		self.saveGTP(input_folder)
		self.getRep()
		self.saveRep(input_folder)
		self.saveMinorToken(input_folder)
		self.initManager()
		print 'manager initiated'
		self.detectLink()

		end = time.time()
		timelength = end - start
		print 'time spent: %f' % timelength

	def lexiAnalysis(self, input_folder):
		coderecords = {}
		GTPrecords = {}
		files = self.getFiles(input_folder)
		for f in files:
			path = input_folder + '/' + f
			lexianalysis = lexicalanalysis(path)
			record, GTP = lexianalysis.getAnalysisResults()
			if len(record) == 0:
				# print f
				continue
			coderecords[f[:f.rfind('.')]] = {}
			file_out = open('test_results' + input_folder[input_folder.find('/'):] + '/lexi_results/' + f[:f.rfind('.')] + '_lexi.txt','w')
			for line in record.keys():
				out = ''
				for part in record[line]:
					out += part + ' '
				file_out.write(out + '\t\t' + str(line[0]) + ' ' + str(line[1]) + '\n')
				coderecords[f[:f.rfind('.')]][line] = record[line]
			file_out.close()
			# for line in record.keys():
			# 	coderecords[f[:f.rfind('.')]][line] = record[line]
			for token in GTP:
				GTPrecords[token] = GTPrecords.get(token, 0) + GTP[token]

		# L = sorted(GTPrecords.iteritems(), key = lambda (k, v): (v, k))
		# x = [key for (key, value) in L]
		# count = 0
		# for i in x:
		# 	print i, GTPrecords[i]
		# 	if GTPrecords[i]>4:
		# 		count += 1
		# print count
		L = sorted(GTPrecords.iteritems(), key = lambda (k, v): (v, k))
		x = [key for (key, value) in L]
		n = int(len(x) * 0.7)
		limit = GTPrecords[x[n]]
		print n
		print limit
		# for i in x:
		# 	print i, GTPrecords[i]
		majortoken = set()
		for token in GTPrecords.keys():
			if GTPrecords[token]>limit:
				majortoken.add(token)
		return coderecords, GTPrecords, majortoken

	def saveGTP(self, input_folder):
		path_out = 'test_results' + input_folder[input_folder.find('/'):] + '/GTP.txt'
		file_out = open(path_out, 'w')
		L = sorted(self.GTPrecords.iteritems(), key = lambda (k, v): (v, k))
		x = [key for (key, value) in L]
		for i in x:
			file_out.write(i + ' ' + str(self.GTPrecords[i]) + '\t\t')
		file_out.write('\n')
		for i in self.majortoken:
			file_out.write(i + ' ')
		file_out.close()

	def getGTP(self):
		L = sorted(self.GTPrecords.iteritems(), key = lambda (k, v): (v, k))
		x = [key for (key, value) in L]
		return x

	def getRep(self):
		count = 0
		for code in self.coderecords.keys():
			count += 1
			if count % 50 == 0:
				print count
			# print 'start', code
			self.codereps[code], self.codeminorreps[code] = getReps(self.coderecords[code], self.majortoken, self.threshold, self.GTP)
			for line in self.codeminorreps[code]:
				for token in self.codeminorreps[code][line]:
					if token in self.minortokens.keys():
						self.minortokens[token].append((code, line))
					else:
						self.minortokens[token] = []
						self.minortokens[token].append((code, line))

	# def saveRep(self, input_folder):
	# 	path_prefix = 'test_results' + input_folder[input_folder.find('/'):] + '/rep_results/'
	# 	for f in self.codereps.keys():
	# 		fout = open(path_prefix + f + '_rep.txt', 'w')
	# 		for line in self.codereps[f]:
	# 			out = ''
	# 			for token in self.codereps[f][line]:
	# 				out += token + ' '
	# 			out += '\t\t' + str(line[0]) + ' ' + str(line[1]) + '\n'
	# 			fout.write(out)
	# 		fout.close()
	def saveRep(self, input_folder):
		path_prefix = 'test_results' + input_folder[input_folder.find('/'):] + '/rep_results/'
		for f in self.codereps.keys():
			fout = open(path_prefix + f + '_rep.txt', 'w')
			for line in self.codereps[f]:
				fout.write(str(line[0]) + ' ' + str(line[1]) + ':\n')
				for T in self.codereps[f][line]:
					out = ''
					out += T[0] + '\t' + str(T[1]) + '\t' + str(T[2]) + '\t' + str(T[3]) + '\t' + str(T[4]) + '\n'
					fout.write(out)
				fout.write('\n')

			fout.close()

	def saveMinorToken(self, input_folder):
		path = 'test_results' + input_folder[input_folder.find('/'):] + '/minortokens.txt'
		fout = open(path, 'w')
		for token in self.minortokens.keys():
			out = token + '\t:\t'
			for location in self.minortokens[token]:
				temp = location[0] + '  ' + str(location[1][0]) + ' ' + str(location[1][1]) + '\t'
				out += temp
			out += '\n'
			fout.write(out)
		fout.close()

	def initManager(self):
		for code in self.codereps.keys():
			for line in self.codereps[code].keys():
				for (token, ml, maxLeft, minLeft, maxRight, minRight) in self.codereps[code][line]:
					if token in self.coderepmanager.keys():
						self.coderepmanager[token].append((code, line, ml, maxLeft, minLeft, maxRight, minRight))
					else:
						self.coderepmanager[token] = []
						self.coderepmanager[token].append((code, line, ml, maxLeft, minLeft, maxRight, minRight))


	def detectLink(self):
		out_path_prefix = 'test_results' + input_folder[input_folder.find('/'):] + '/link_results/'
		count = 0
		for code in self.codereps.keys():
			count += 1
			print code
			print count
			start = time.time()
			links, sameraretoken = detectLinks(code, self.codereps[code], self.coderepmanager, self.coderecords, self.minortokens, self.codeminorreps[code], self.threshold)
			# print '%d direct links detected' %len(links)
			# if len(links) != 0:
			# 	self.links[code] = links
			# if len(sameraretoken) != 0:
			# 	if code not in self.links.keys():
			# 		self.links[code] = {}
			# 	for line in sameraretoken.keys():
			# 		if line in self.links[code].keys():
			# 			self.links[code][line].extend(sameraretoken[line])
			# 		else:
			# 			self.links[code][line] = []
			# 			self.links[code][line].extend(sameraretoken[line])
			# end = time.time()
			# if code in self.links.keys():
			# 	print '%d links detected' % len(self.links[code])
			# else:
			# 	print 'no links detected'
			# print 'time spent: %f' %(end - start)
			self.links[code] = {}
			self.links[code]['D'] = {}
			self.links[code]['T'] = {}
			if len(links) != 0:
				self.links[code]['D'] = links
			if len(sameraretoken) != 0:
				self.links[code]['T'] = sameraretoken
				# for line in sameraretoken.keys():
				# 	if line in self.links[code].keys():
				# 		self.links[code][line].extend(sameraretoken[line])
				# 	else:
				# 		self.links[code][line] = []
				# 		self.links[code][line].extend(sameraretoken[line])
			end = time.time()
			print '%d links detected' % (len(self.links[code]['D']) + len(self.links[code]['T']))
			print 'time spent: %f' %(end - start)
			nd = len(self.links[code]['D'])
			nt = len(self.links[code]['T'])
			if nd != 0 or nt != 0:
				fout = open(out_path_prefix + code + '.txt', 'w')
			else:
				continue
			if nd != 0:
				fout.write('Direct links:\n')
				for line in self.links[code]['D'].keys():
					fout.write(str(line[0]) + ' - ' + str(line[1]) + ' links:\n')
					for link in self.links[code]['D'][line]:
						fout.write(link[0] + '\t:\t' + str(link[1][0]) + ' - ' + str(link[1][1]) + '\n')
					fout.write('\n')
			if nt != 0:
				fout.write('\nWith same rare tokens:\n')
				for line in self.links[code]['T'].keys():
					fout.write(str(line[0]) + ' - ' + str(line[1]) + ' links:\n')
					for link in self.links[code]['T'][line]:
						fout.write(link[0] + '\t:\t' + str(link[1][0]) + ' - ' + str(link[1][1]) + '\n')
					fout.write('\n')
			fout.close()


	def saveLinks(self):
		path_prefix = 'test_results' + input_folder[input_folder.find('/'):] + '/link_results/'
		for code in self.links.keys():
			nd = len(self.links[code]['D'])
			nt = len(self.links[code]['T'])
			if nd != 0 or nt != 0:
				fout = open(path_prefix + code + '.txt', 'w')
			else:
				continue
			if nd != 0:
				fout.write('Direct links:\n')
				for line in self.links[code]['D'].keys():
					fout.write(str(line[0]) + ' - ' + str(line[1]) + ' links:\n')
					for link in self.links[code]['D'][line]:
						fout.write(link[0] + '\t:\t' + str(link[1][0]) + ' - ' + str(link[1][1]) + '\n')
					fout.write('\n')
			if nt != 0:
				fout.write('\nWith same rare tokens:\n')
				for line in self.links[code]['T'].keys():
					fout.write(str(line[0]) + ' - ' + str(line[1]) + ' links:\n')
					for link in self.links[code]['T'][line]:
						fout.write(link[0] + '\t:\t' + str(link[1][0]) + ' - ' + str(link[1][1]) + '\n')
					fout.write('\n')
			fout.close()


	def getFiles(self, folder):
		target_path = folder
		target_files = [f for f in listdir(target_path) if isfile(join(target_path, f))]
		if '.DS_Store' in target_files: 
			target_files.remove('.DS_Store')
		return target_files

if __name__ == '__main__':
	# input_folder = 'test_input/CodeJam/2A/python'
	# input_folder = 'test_input/sort_codes'
	# input_folder = 'test_input/test'
	# input_folder = 'test_input/CJ_16_1'
	# input_folder = 'test_input/CJ'
	input_folder = 'test_input/CJ_0'
	threshold = 0.4
	linkdetect = linkDetect(input_folder, threshold)