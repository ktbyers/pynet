file_name = "show_ver.out"
with open(file_name, "r") as f:
    output = f.read()

if 'Cisco' in output:
    print "Found Cisco string"
