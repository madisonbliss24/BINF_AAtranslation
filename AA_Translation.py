#Makes a dictionary, matching up each amino acid "letter" from the bacterial code file with its 3 bases
def makeAAdict(filename):
    #get information from file
    with open(filename,"r") as bactFile:
        baseLists = []
        AAs = []
        AADict = {}
        for line in bactFile:
            if line.strip()[0] == "A":
                AAs.append(line[11::].strip())
            if line.strip()[0] == "B":
                baseLists.append(line[11::].strip())
    AAs = list(AAs[0])

    #make dictionary
    i = 0
    for char in AAs:
        AADict[char] = baseLists[0][i] + baseLists[1][i] + baseLists[2][i]
        i += 1
    return AADict



#Returns a list of sequences from a fastq file
def seqListfromFQfile(filename):
    seq = ""
    counter = 0
    seqList = []
    with open(filename) as fqfile:
        for line in fqfile:
                if line[0] == ">":
                    if counter != 0:
                        seqList.append(seq)
                    seq = ""
                    counter += 1
                    pass
                else:
                    seq += line.strip()
    return seqList

#Takes in the amino acid dictionary and the list of proetin sequences, then returns a list of translated sequences
def translateSeqs(AADict, seqList):
    #temp list and permanent list
    TranslatedSeqs = []
    tempProteinList = []

    #iterate through seqs
    for seq in seqList:
        #put together codons and identify protein from dict
        for i in range(0,len(seq) - 2,3):
            codon = seq[i:i+3]
            for pro,co in AADict.items():
                if co == codon:
                    proteinMatch = pro
                    tempProteinList.append(proteinMatch)

        #join list together and add to master protein seq list before iteration ends
        TranslatedSeqs.append("".join(tempProteinList))
    return TranslatedSeqs


#---------------------------------MAIN------------------------
#Body of the program where all 3 functions above are called and used to translate protein sequences from the fastq file

#Then a report is printed

#create dictionary
AADict = makeAAdict("bacterialcode.txt")

#get sequences
proteinSeqList = seqListfromFQfile("test.fna")

#translate seqs
AASeqList = translateSeqs(AADict, proteinSeqList)

i = 0
while i < 4:
    print("Original Sequence: " + proteinSeqList[i] + '\n')
    print("Translated Amino Acid Sequence: " + AASeqList[i] + '\n')
    print("-"*110 + '\n')
    i += 1


