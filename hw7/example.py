import hw7

d1 = hw7.Directory("cs141")
f1 = hw7.File("notes.txt", "CS 141 notes")
f2 = hw7.File("hw7.py", "import hw7")

d1.add_file(f1)
d1.add_file(f2)
d2 = hw7.Directory("math151")
f3 = hw7.File("notes.txt", "Calc 1")
d2.add_file(f3)

d3 = hw7.Directory("chem101")
f4 = hw7.File("Lab1.pdf", "Lab 1: Displacement")
f5 = hw7.File("Lab2.pdf", "Lab 2: Bunsen Burners")
d3.add_file(f4)
d3.add_file(f5)

fs = hw7.FileSystem()
fs.add_directory(d1)
fs.add_directory(d2)
fs.add_directory(d3)
