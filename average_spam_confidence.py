# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
list = []
count = 0
total = float(0)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line[20:]
    count = count + 1
    total = total + float(line)
    avg = total / count
print('Average spam confidence:', avg)
