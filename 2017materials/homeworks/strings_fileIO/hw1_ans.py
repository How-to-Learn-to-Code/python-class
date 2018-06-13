#Open File
my_file = open("virus.txt")
#Read in sequence
sequence = my_file.read()
size = len(sequence)
sequence_list = list(sequence)
#Calculate nucleotide composition
fraction_a = sequence_list.count('A')/size
fraction_c = sequence_list.count('C')/size
fraction_g = sequence_list.count('G')/size
fraction_t = sequence_list.count('T')/size
#Ouput to console
print("G: " + str(fraction_g))
print("C: " + str(fraction_c))
print("A: " + str(fraction_a))
print("T: " + str(fraction_t))
print("GC: " + str(fraction_g+fraction_c))
print("Based on nucleotide sequence, the virus is most similar to: Dengue virus type 3")
#Output to file
output_file = open("output.txt","w")
output_file.write("G: " + str(fraction_g) + "\n")
output_file.write("C: " + str(fraction_c) + "\n")
output_file.write("A: " + str(fraction_a) + "\n")
output_file.write("T: " + str(fraction_t) + "\n")
output_file.write("GC: " + str(fraction_g+fraction_c) + "\n")
output_file.write("Based on nucleotide sequence, the virus is most similar to: Dengue virus type 3")

#Close Files
my_file.close()
output_file.close()












#%%
#My script

with open("virus.txt") as my_file:
    sequence = my_file.readline()
    size = len(sequence)
    a = list(sequence).count('A')/size
    c = list(sequence).count('C')/size
    g = list(sequence).count('G')/size
    t = list(sequence).count('T')/size
    gc = g+c
    print("Percent G: " + str(round(g,4)*100) + "%") 
    print("Percent C: " + str(round(c,4)*100) + "%")
    print("Percent A: " + str(round(a,4)*100) + "%")
    print("Percent T: " + str(round(t,4)*100) + "%")
    print("Percent GC: " + str(round(gc,4)*100) + "%")
    
with open("output.txt","w") as out_file:
    output_file.write("G: " + str(round(g,4)*100) + "\n")
    output_file.write("C: " + str(round(c,4)*100) + "\n")
    output_file.write("A: " + str(round(a,4)*100) + "\n")
    output_file.write("T: " + str(round(t,4)*100) + "\n")
    output_file.write("GC: " + str(round(gc,4)*100) + "\n")
    output_file.write("Based on nucleotide sequence, the virus is most similar to: Dengue virus type 3")

