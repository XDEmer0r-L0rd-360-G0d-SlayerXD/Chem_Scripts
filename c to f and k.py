number = (8.13, 8.64, 5.62, 18.21, 22.82, 32.98, 9.13, 25.39)
out = []
for a in number:
   out.append(f"kg: {a/1000}\n")
#input()
with open("num.txt", 'w') as f:
   f.writelines(out)
#input()