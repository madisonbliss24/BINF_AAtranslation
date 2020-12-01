# BINF_AAtranslation_Py

#For this code, I used a genetic code file that looks like this

#AAs    = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
#Starts = ---M---------------M------------MMMM---------------M------------
#Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
#Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
#Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

#And a FASTA file with 4 DNA Sequences
    #The program makes a dictionary of AA and 3 base matches
    #gets the sequences from the FASTA filename
    #and uses the dictionary to translate the DNA sequences to amino acid sequences
##########################################################################


---------------------------FINAL OUTPUT EXAMPLE---------------------------


Original Sequence: ATGCGAGTTTTATTCATGTTTATGATGCTAATCAGCATCAACTTGCCCGCACAGGCCGAGCAGCAAACGTATTCCGACAGCGAGTTGCTCGATAGGCCATTAATGGAGAGATACATCCTTGATGAGCTCAAATCGCTAAGACAAGATCAACAAGACTTAGAAAAGCGATTAACCGTTCAGTTTACCGAGCGCGAACTCTCAGTAGCCGATAAGTCACTGAACTATGCCAATGTGACAGTGACTTACTTCTTCTACATCATTGCCGGTGTTGCTTCTCTTGTCGCCTTTGTTGGCTGGCAATCATTAAGGGAGTTAAAAAACAACACCAAAGCGATGGCCGATAAAAGGCTGGAAACCATTGCAGAAAAGTATGAGAAGAAGTTCATTGCGTTAGAAAGAGATTTGAAACGCAAAACACGCATCATCAGTGAAAACAACCGAGAGATCGAAATCATCAATGAGATTCATAACCTCTGGTTGAGAGCGCAAAGTATGCCAACCGCTGAGCAGCGTATTGATGTGTACGATGAGATTCTGGCGATAAGGCCGGGCGACTTAGAGGCCGTCACCTACAAAGCCGATGCTGCAATGGAAATCAAAGAGTACAACTGGGCACTCAGTCTTTGTAACCGCGTACTGGATATGGACAGTTCTAATGCCCCAGCGCTCTACCAAAGAGCCTGTGCATATTCTCGTCTGGGTTTGGAAGAGCAGTCGATCGAAGATCTCGAACGAGCAATCGAAGCGAGCCCATCGATACGTGACCTCATCGCCAATGAGCCCGATTTAGAACCATTACACGGTAACCCAAGCTTTGATCGCATGCTGACAAGAGGGCAAGAGAGTTAA

Translated Amino Acid Sequence: MFMMMSNQEQTDSERMEYEDKQEKLNVVYFFYWRENNAMRLKEKKFANNEENWAMEQVYELAIRPDEYMEYNWNLMDAYLEQASIDEHNSMLGE

--------------------------------------------------------------------------------------------------------------

Original Sequence: ATGCCCAAGGTAGGAATGCCAAAGATTCGCAGGCCACAATTAGTGAGTGCGACCATGACGGTCATTGACCGTGTGGGCTTGCACGGAGCCAGTGTTTCTTTGATTAGCCAAGAGGCGGGTGTCTCTAGTGGCATCATCAACCACTACTTTGGTGGTAAGCATGGACTGCTTGAAGAAACGATGCGCGATATTTTGAGGCAGTTATCTTGTGATGCAACAAAACGCTTGAATTTACTACCGAAGCAGGCGCATATGCAGAGAATCAACGCGATATTGGATGCTAATTTCGTTGGCTTTCAATCTGAAAGCAAGGTGATCAAAACATGGTTGGCGTTTTGGTCTTATTCCATGCATGACGAAGCGTTAAAGCGTTTACAGCGCGTTAATGAAAAGCGCTTGCTTTCACATTTAAAGCGAGAACTCAAAGCGTTGATGAGCAAAGAACAAGCCGACATTGTCGCCCAAGGCATTGCCGCGCTTATCGACGGGATCTGGCTGCGTGGAGCGCTTAATCCGGAAGGTATTAATGCGAACAAAGCGCGCATCATTATTAATGATTATTTAGAAAAACAGCTCACGTTTTATTCACAACAATAA

Translated Amino Acid Sequence: MFMMMSNQEQTDSERMEYEDKQEKLNVVYFFYWRENNAMRLKEKKFANNEENWAMEQVYELAIRPDEYMEYNWNLMDAYLEQASIDEHNSMLGEMKMKRVAMTDVHSEANHYKLTMRQPKQAMQNAIFSKVWAWMDAKQKKAMSDADGWLAPANAQT

--------------------------------------------------------------------------------------------------------------

Original Sequence: ATGGAAGTTACAGCACATTACATTGGAGGGAAGCCTTTCGTTGGTGACACTGGCGAATCTTTTGCGACCTTAAATCCAGCAACCGGAGAAGTGTTAGCACACATCGAGCAAGCCGACGAAAGGGTGTTAGGTCACGCCATCGAGAGCGCGAAGCTTGGCTTTTCTGTGTGGTCATCTATGAGCGCTGCCGAGCGCAGCCGATGCTTACTCAAAGCGGCGCAGCTGATTCGCGATCACAATGATGAACTAGCAGAGTTGGAAGTGCGCGATACGGGCAAACCAATTCAAGAAGCGAGTGTGGTTGACATTGCTACTGGCGCAGATGTTATCGAGTATTTTGCTGGATTAGTGAATGGCTTAGGTGGCGAGCAACAATCCCTTGGTTCCAATCAGTTTTTTTACACCAGAAGAGAACCTCTGGGCATTTGTGCCGGCATCGGCGCTTGGAATTATCCGATTCAAATTGCAATGTGGAAAGCCGCGCCTGCATTAGCAGCTGGCAACGCGATGATCTTTAAACCCTCAGAAGAAACGCCACTTTCGGCACTCAAACTGGCTGAACTCTTTACGCAAGCGGGCGTGCCTGATGGCGTGTTTAACGTTGTTCAAGGGGACTATCGTGTTGGGCAAATGCTCACCGCGCATCCTGAAATCGACAAAGTCTCATTTACCGGTGAGTCAGGCACGGGCAAGAAAGTGATGGCCGATAGTGCAGCGACACTCAAACCCGTCACCATGGAATTGGGGGGGAAATCGCCCTTGATTATTTTCGATGATGCCGATCTTGATGATGCTGTCTCGGCAGCAATGGTGGCAAATTTTTACACTCAAGGTGAGGTGTGTACCCATGGCACGCGAGTTTATGTTCAACGAGCGATGTACGACGCGTTTGTTGAACAGCTAAAAGAGCGCACGGAAAAGCTCATTGTCGGCGATCCAATGAACATGGAAACGCAAATTGGCTCACTGATTTCTAAATCGCATCTAGAAAAAGTACTCGGTGCTATTTCGAGTGCGAAAGAGAGTGGTGCAACGTTGCTCACTGGTGGTTTCCAAGTGACGGAAAGAGGGCTAGAGAAAGGGTGTTTTGTTGCGCCTACCGTCTTTGTCGATTGCCGCGATGAGATGCCTCATGTGCAAAATGAAATCTTTGGACCTGTCATGTCGGTGCTGGTGTTTGATGACGAAGATGAAGTCATTGCTCGCGCGAACAACACCCAATACGGCTTGGCCGCTGGGGTATTTACGCAGAATCTATCCAAAGCCCATAGAGTCATTCACCAACTGCAAGCGGGCATTTGCTGGATAAACACTTGGGGAAATTCACCCGCAGAGATGCCGGTGGGGGGCTACAAGTTGTCGGGCATTGGCCGCGAAAATGGCCAAGAGACGTTACTGCACTATACGCAGACCAAAAGCGTGTTTGTCGAACTGGGTGCGTTCGACTCCCCTTACGCTTAA

Translated Amino Acid Sequence: MFMMMSNQEQTDSERMEYEDKQEKLNVVYFFYWRENNAMRLKEKKFANNEENWAMEQVYELAIRPDEYMEYNWNLMDAYLEQASIDEHNSMLGEMKMKRVAMTDVHSEANHYKLTMRQPKQAMQNAIFSKVWAWMDAKQKKAMSDADGWLAPANAQTMYGKFDAVHEDRVHESAKVWMSESCAAQLHEVTAVDEVEQYLWPMWANAMTLTAVVNGDGMADETKVMAMGGFMVYEVTAMYDAQETKMNMTLAETFVTGEGACEMVMVLVDANNYGTQHLACWINWEMPVGYKETLHTQSVLAFDY

--------------------------------------------------------------------------------------------------------------

Original Sequence: ATGCAGCAACACTACGATTACATTATCGTCGGTGCGGGTTCCGCTGGCTGTGTGCTAGCGGATCGACTATCAGAGAGTGGTGATCACAGTGTTTTATTACTCGAAGCGGGCGGTTCCGACAAGAGTATTTTCATTCAAATGCCAACGGCGCTCTCTTACCCTATGAACTCAGAGAAGTACGCTTGGCAATTTGAAACCGATGCAGAAGCGGACTTAGATGGCCGCCGTTTACATTGCCCAAGAGGGAAAGTGCTCGGGGGCAGTTCCTCCATCAACGGCATGGTTTATGTTCGTGGTCACGCCTGTGATTTTGATGAATGGGAAGAGCAGGGTGCAAAAGGTTGGAATTACCAAGCGTGTCTACCGTATTTTCGCCGAGCAGAAAACTGGATTGACGGGGAAGATGAGTATCGCGGTGGCGATGGGCCATTAAGTACCTGTGCTGGCAATAAGATGACGCTGAATCCACTCTATCGCGCGTTCATTGACGCAGGTAAGGAGGCCGGATATCCAGAAACATCGGACTACAATGGCTACCAACAAGAAGGCTTTGGTCCGATGCATATGACGGTTAAAAATGGTGTGCGAGCTTCAACCTCAAACGCATACTTAAGCCGTGCCAAAAAAAGAAGCAATTTCAAACTGATCAAAGGCGTTGTGGTTCAACGTATCTTACTGGAAGAAAAGCGTGCCGTAGGGGTCGAGTTTGAACTGGCAGGCGAACTGCGTACTTGTTTTGCCAAAAATGAAGTGATTTCCAGTGCGGGTTCGATTGGTTCGGTGCAACTGTTACAGCTCTCTGGCATTGGCCCTAAAACGGTACTTGAGAAGGCGGGGGTGACGCCCGTTCACCATCTGCCAGGCGTTGGACAAAACTTACAAGACCATCTCGAAGTCTATTTCCAATACCATTGTCAAAAGCCCATCACCTTGAATGGAAAATTGGACTGGTTCAGCAAAGGGTTGATTGGAGCCGAGTGGATTTTAACGCGTAAAGGGCTTGGGGCGACCAATCACTTCGAGTCTTGCGCCTTTATTCGCTCACGTGCAGGTTTGAAATGGCCGAATATTCAGTACCACTTTTTGCCCGCGGCAATGCGTTACGATGGACAAGCCGCCTTTGATGGTCATGGCTTCCAAGTTCATGTTGGGCCAAACAAGCCTGAGAGCCGAGGCCGTGTTGAGATCGTCTCAGCCAATCCGTCGGACAAACCCAAAATTCAGTTTAACTACTTATCGACCGAGCGCGATCGTCAAGATTGGCGAGATTGTATTCGCCTTACTCGCGAAATTTTGGCGCAGCCAGCAATGGATGAGTTCCGTGGTGAAGAGATACAGCCCGGCATCAATGTCGCGACCGATGCGGAAATCGATCAATGGGTGAAAGAGAACGTCGAGAGCGCGTATCACCCTTCATGCTCATGCAAAATGGGCGCAGACGATGACCCAATGGCGGTGCTCGATGAAGAGTGTCGTGTACGAGGAATCACCAACCTGCGCGTAGTGGATTCATCCGTTTTTCCCACTATTCCTAACGGCAATCTTAATGCGCCAACCATCATGGTGGCGGAAAGAGCCGCCGATTTAATTTTGCATAAACAGCCGTTGCCTCCGCAGCGCTCAAAGGTTTGGCTAGCCCCGAGTTGGGAAACTCAGCAGCGGACTGGAGAGCCGATGAGATAA

Translated Amino Acid Sequence: MFMMMSNQEQTDSERMEYEDKQEKLNVVYFFYWRENNAMRLKEKKFANNEENWAMEQVYELAIRPDEYMEYNWNLMDAYLEQASIDEHNSMLGEMKMKRVAMTDVHSEANHYKLTMRQPKQAMQNAIFSKVWAWMDAKQKKAMSDADGWLAPANAQTMYGKFDAVHEDRVHESAKVWMSESCAAQLHEVTAVDEVEQYLWPMWANAMTLTAVVNGDGMADETKVMAMGGFMVYEVTAMYDAQETKMNMTLAETFVTGEGACEMVMVLVDANNYGTQHLACWINWEMPVGYKETLHTQSVLAFDYMQHYYAVAEHADKFMTAYMNEKYWADCGVGNMHWEQWYAPNWDGEGKMTLAFDKEDYYPMMTVNYSSFLVLKGELLVAVLQTEKAGVTHLNDFYKDWFSGEWTGGAHFECWPQYHAMYFGNKESEPDQNYEWAQMEFEIQAAWVENESAHCCMDDMAVENLVNAMVAQPPQKWPWQQEPM


