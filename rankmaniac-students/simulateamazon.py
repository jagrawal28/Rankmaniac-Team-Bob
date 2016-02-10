




import os
import subprocess


def is_ended():
	output_file = open("output.txt")

	for line in output_file:
		if not line.startswith("FinalRank:"):
			return False

	return True


def copy_from_to(filename1, filename2):

	file1 = open(filename1, "r")
	file2 = open(filename2, "w")

	for line in file1:
		file2.write(line)

	file1.close()
	file2.close()


def run_on_datafile(filename):



	copy_from_to(filename, "input.txt")

	num_iters = 0

	while True:
		
		num_iters += 1
		mapreduce_process = subprocess.Popen("python data/pagerank_map.py < input.txt | sort | python data/pagerank_reduce.py | python data/process_map.py | sort | python data/process_reduce.py > output.txt", shell=True)
		mapreduce_process.wait()

		if is_ended():
			break

		copy_from_to("output.txt", "input.txt")

	print "Ran MapReduce on", filename
	print num_iters, "iterations"
	print "Output:"

	output_file = open("output.txt")

	for line in output_file:
		print line[:-1]



if __name__ == "__main__":
	run_on_datafile("local_test_data/EmailEnron")
	run_on_datafile("local_test_data/GNPn100p05")



