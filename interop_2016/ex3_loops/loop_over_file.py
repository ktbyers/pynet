file_name = "show_ver.out"
with open(file_name, "r") as f:
    output = f.readlines()

print
for line in output:
    line = line.strip()
    if 'Cisco 881' in line:
        print line
print
