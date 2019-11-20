import matplotlib.pyplot as plt
import numpy as np


def GetQueryName(line):
	return line.split()[2]
		
def GetRunningTime(line):
	running_time = int(line.split()[1])
	return running_time

# return a dictionary: query_name : a list of running times
def GetDictionary(data_directories):
	ret = {}
	for data_directory in data_directories:
		file = open(data_directory, "r")

		line = file.readline()[:-1]
		while line != "":
			query_name = GetQueryName(line)
			line = file.readline()[:-1]
			while True:
				line = file.readline()[:-1]
				running_time = GetRunningTime(line)
				if query_name not in ret:
					ret[query_name] = [1.0 * running_time]
				else:
					ret[query_name].append(1.0 * running_time)
				line = file.readline()	
				
				if line == "" or line.split()[0] == "Running":
					break

	return ret

def main():
	hash_file = "./scripts/data/hash_enum"
	lip_file = "./scripts/data/lip_enum"
	xiating_file = "./scripts/data/xiating_enum"


	hash_dict = GetDictionary([hash_file])
	lip_dict = GetDictionary([lip_file])
	xiating_dict = GetDictionary([xiating_file])


	lip_time = []
	hash_time = []
	xiating_time = []
	index = []
	cnt = 1

	for q in lip_dict:
		index.append(cnt)
		# lip_time.append(sum(lip_dict[q]) / len(lip_dict[q]))
		lip_time.append(min(lip_dict[q]))
		hash_time.append(min(hash_dict[q]))
		xiating_time.append(min(xiating_dict[q]))

		cnt += 1
	lip_plot = plt.plot(index, lip_time, '-o')
	hash_plot = plt.plot(index, hash_time, '-o')
	xiating_plot = plt.plot(index, xiating_time, '-o')
	
	plt.gca().legend(('LIP Standard', 'Hash-join', 'Xiating'))

	plt.show()

if __name__ == "__main__":
	main()

