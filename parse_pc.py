import sys

if len(sys.argv) != 2:
	print 'usage: python %s input_file' % sys.argv[0]
	exit(1)

input_file = open(sys.argv[1])
lines = input_file.readline().rstrip().split('\r')
input_file.close()

pc_list = []
for line in lines:
	words = line.rstrip().split(',')
	if len(words) != 4:
		print 'Wrong format ' + line
		continue
	
	last_name = words[0].split()[-1]
	pc = []
	pc.append(last_name)
	pc.extend(words)
	
	# pc format: last name, full name, affiliation, region, website
	pc_list.append(pc)

pc_list.sort()

for pc in pc_list:	
	print '<p><a href=\"%s\">%s</a> (%s, %s)</p>' % (pc[4], pc[1], pc[2], pc[3])
	
