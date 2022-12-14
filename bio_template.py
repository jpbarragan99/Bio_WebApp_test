#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import streamlit as st
import altair as alt
from scipy.spatial.distance import hamming


# In[ ]:


st.header('Enter the DNA sequence')

seq_input = ">DNA Query\nCGTATGGTCTCATTGGGCAAGATCGTGGCGCACCTACGTGTATCGGGGTACCCGCCGATAAGATGACCCGCCGTCTACAGAGTGTGCATTCATTTAACTAAATCCAACTGGTAGCTAAATCTTTTGAACGATATACTCACTTAGGACTAACGTCCCGACGGAAACTACGCAGTAAGGTATTAGCAGGAGTGGAGTTCCTGCTTATACCAAGTGACCCGTGGTACACTATAATAAGATAGATTGCTTTGGTCCATAGAGAGGTTACTGGATTGGTTGGAGCGACATTCGCACCTATTACGAAGTTCTAGACACAATGACCCTCACGTCGATTCGCTATGTTGTCTTCTGCTCTGCGCTAGGAGCCGACGCGCGGATAGGGACCTTACTCCGCCAGTCATTCATAAGGAACCTCGATTGCGGTAGTCTCAGTCCCGCATCCGTCCTATGAAGGCCAAAGGGCGTAGGCGTGCGTAACCTGTCATGCAAAGCCCCGGCACTAAATACGGAATAATTCTCGATGAAGGATCGCACATCCCCCTCAGCGCGCGCTAGACGGAGTAACAATAGGTGCGCGTCGCCGTGTAGAGCTAGCGGTTCGATCAGTAATAGCGCCAATCAAAAATTAGGCAGTGGATCAGAATCCACCATCCGTGAGCCTACTGCCGCGTGCTGATCATCTGCCTTCCGTTTCGTAGCGTACAGGCTAAGGTTGTCATATAGCAATTGCGGTTCGTAACTGATGATTACCCGACCCAGTTATCTCTAGTTGTTGTACGTCAGTATCAACGGAGACGGAGTGCCACTAGACGTATCTGAGATGCTGAGGATACAGAAACCCATAAGCGGGACTGCCGTTGCCGGCGGGCTTATTGACTAGCGATGAGCCCAATACGGTCAGACCATACTGACCCCCACACAAGAAGTCTCACCGGCTCCCCA\nCCGGGGACCAGACATGCCGCTAGTCATTACTGCGGATCATACCCTCTACCAGCGCCACAAAAGTAAATAACGGGGCCGATGCTTCATAACCCTTTTGCATTCTCCATTGTAACGTATGCTTTAGATAGACTTGACCGAACAGA\nCTATATCGGATGGTCCTTATATCCAATGGAGCCTGCATTATCTTCGTGCCGAAACTGTAGCAAGCACTCCGTAGACTCAGAACCCGCCTGGCAAAAGGGTAAGTGCTCGATATTGCTCGACCCCCGGGCTACAGCTTACAAACAAAGTAGGGGTCGGACTCAAGACCTAATTCCTGGATTCAGTACCATCCCCCATTAAAAGTTGTTCCGTTCCGTCTTCAATTAATATAGTATTAAATGATAACTAGGATTTTAGTCTCCTCTATCCCTGTCAATCGGTGGTTACCCCCGCACGGATTGTACTACGCAAT\nATATTACTGCCGCGAGGTAGAGATCCCTGAGGCTTGCTAGCTCGTAGGTCGTCAGTCGCCCACTTAACACATTTCGCCTTAAGAACCATTATACTTGCTGTGGGCCGTGCCCGGCGATTTTTGTCGGCGACTACTTGTGATAAGGGCCTTTTGCCCGGGACAGATACGGTACATCACGGGATACCATATTAAAAAGCTGGCATGTATGGTACATAGCATATTCTTGCCTGCAATAGACGATCCTAACACACACACAATGTATAAACTGATTTAGCTGTTCCTACTTTCCCAACGTCTTAATACCCACCGATAATCGTGCGTCTACTAGCAAGCGATAGTAGTGTAAATGGCGTGGGTACACCT"


# In[ ]:


#sequence = st.sidebar.text_area("Sequence input", sequence_input,height=250)
sequence = st.text_area("Sequence input", seq_input, height=220)
sequence = sequence.splitlines()
sequence = sequence[1:] #Skips the name
sequence = ''.join(sequence) #Concatenation of list to string

st.write("""
***
""")


# In[ ]:


st.header('INPUT (DNA Query)')
sequence

st.header ('OUTPUT (DNA Nucleotide Count)')


# In[ ]:


#Printing the dictionary

st.subheader('Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict ([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X


# In[ ]:


#Printing in Text

st.subheader('Print Text')
st.write ('There are ' + str(X['A']) + 'adenine (A)')
st.write ('There are ' + str(X['G']) + 'guanine (G)')
st.write ('There are ' + str(X['T']) + 'thymine (T)')
st.write ('There are ' + str(X['C']) + 'cytosine (C)')


# In[ ]:


#Displaying the DataFrame

st.subheader ('Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename ({0: 'count'}, axis = 'columns')
df.reset_index(inplace = True)
df = df.rename (columns = {'index':'nucleotide'})
st.write(df)


# In[ ]:


#Displaying Bar Chart

st.subheader('Display Bar chart')
p = alt.Chart(df).mark_bar().encode (
    x = 'nucleotide',
    y = 'count'
)

p = p.properties(
    width = alt.Step(80) #bar width
)

st.write(p)


# In[ ]:


#Haming Distance

string1 = 'CGTATGGTCTCATTGGGCAAGATCGTGGCGCACCTACGTGTATCGGGGTACCCGCCGATAAGATGACCCGCCGTCTACAGAGTGTGCATTCATTTAACTAAATCCAACTGGTAGCTAAATCTTTTGAACGATATACTCACTTAGGACTAACGTCCCGACGGAAACTACGCAGTAAGGTATTAGCAGGAGTGGAGTTCCTGCTTATACCAAGTGACCCGTGGTACACTATAATAAGATAGATTGCTTTGGTCCATAGAGAGGTTACTGGATTGGTTGGAGCGACATTCGCACCTATTACGAAGTTCTAGACACAATGACCCTCACGTCGATTCGCTATGTTGTCTTCTGCTCTGCGCTAGGAGCCGACGCGCGGATAGGGACCTTACTCCGCCAGTCATTCATAAGGAACCTCGATTGCGGTAGTCTCAGTCCCGCATCCGTCCTATGAAGGCCAAAGGGCGTAGGCGTGCGTAACCTGTCATGCAAAGCCCCGGCACTAAATACGGAATAATTCTCGATGAAGGATCGCACATCCCCCTCAGCGCGCGCTAGACGGAGTAACAATAGGTGCGCGTCGCCGTGTAGAGCTAGCGGTTCGATCAGTAATAGCGCCAATCAAAAATTAGGCAGTGGATCAGAATCCACCATCCGTGAGCCTACTGCCGCGTGCTGATCATCTGCCTTCCGTTTCGTAGCGTACAGGCTAAGGTTGTCATATAGCAATTGCGGTTCGTAACTGATGATTACCCGACCCAGTTATCTCTAGTTGTTGTACGTCAGTATCAACGGAGACGGAGTGCCACTAGACGTATCTGAGATGCTGAGGATACAGAAACCCATAAGCGGGACTGCCGTTGCCGGCGGGCTTATTGACTAGCGATGAGCCCAATACGGTCAGACCATACTGACCCCCACACAAGAAGTCTCACCGGCTCCCCA'
string2 = 'ATTTGGCCTCAAGTAGGCAAAGTCGGTGTGGATCTATGAGTTCGGAACTACCCCCTTAGGAGAAGTCGAGTCACCCCCACCGCGTGGATCTATAAGATTAGCCCCTATTGCTAGCATGAGGTCTTCATCTCCACATTCACTTACAGTTTGATTCCTGGTAGGTCGTATTAGAGATCGCATCTATGTAGGTGGTTTGGCGACTAATAGTGGGAGCCTACTGGGAATGTTCGATATAAGGAAATCCTTCGTGCCTTTAGCTTCATCACAACCTGCCTCGGGGGACAGTAGCATTTATATCCCTGCTTGACATAGTCTACCTGTTAGATCTCCATGCTATGTTGTCTTCTGCATTCTGATAACAGCTAGCCCGTGCGTAGGTGCCTGATCTTCTCTTTCACCGACTAGCACCGTCGGTCTCACTAGTTGCAGTCCCGCAAGCCTGCGGGTCAGGCGCAACGGTGGTAGTGAACGCAACGTTTAAGGCTCGGTAGAGTTATTGACCACTGATGCTCGGGCGGGGGCGTCTCGCTTCTCACCTCCGGGTCGACGTAGATAGACGAACAATGGGTGAACACTTCCGCGTTTATCACGCGGTTCACTCAGTAATAGAGCTAGTAGCTTATAATCTAATGAGTCAGAATCCGCGAACATGCCGCATAATTCCGACTGGTGCACGTGATATGATCGATTCGAGTAATTTCGGCTTAGAAGTTCCAAATCTAAACGCAGGCCGCCAGTGTGGGCGCCACGTCCTTGAGCTCTGTGTCTGTTGTGCGGTACTAGCTACGTGCCAGTAATTCTTAGATCAGTATATCAGACGCCTACAATATAGATGCCAATAATGGGGAATGACAATCTGGGCCGCTATGATGGGTGGCGATGAGAAAAGTACGCACATACGTAGAGGAGTGCCAGAGAAAGTCGCTCTGAAAGTCACGA'

hamming_distance = hamming(list(string1), list(string2)) * len(string1)

st.write(hamming_distance)


# In[ ]:




