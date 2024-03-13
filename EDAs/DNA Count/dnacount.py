import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# Importing a header image in streamlit
# For more Streamlit functions see its documentation
image = Image.open("header.jpg")
st.image(
    image, use_column_width=True
)  # To fill in almost the whole page width. We could also use: width = 80%

# *** creates a line. **...** makes the text bold.

st.write(
    """
         # DNA Surge X Count Web Application
         
         This web app counts the nucleotide composition of DNA!
         *** 
         """
)

st.header("Enter DNA sequence")

sequence_input = "> DNA Query\nCATTATTGATATTTAAATGCTATCTTGAAGAAACCACTTAAAAATATCTATAATTAATTTATTAAAATTGATTAAATTAATTCCTAAATCTGCGCGATAGGGTATTAAAGGTTTAATTTTGTATAACAAGATACTTCCGATCTTAATGAA"

# We use text_input for one-line text and text_area for multi-line. Moreover, number_input for numbers

sequence = st.text_area("Input your DNA sequence:", sequence_input, height=200)
sequence = sequence.splitlines()
sequence = sequence[
    1:
]  # Skips the sequence name (first line) because it's the actual sequence name 'DNA Query' (not to be analysed)
sequence = " ".join(sequence)  # Concatenates list to string

st.write(
    """
         *** 
         """
)

# Prints the input DNA sequence
st.header("INPUT (DNA Query)", sequence)

# After the UI design we proceed to give our web app the required functionality
st.header("OUTPUT (DNA Nucleotide Count)")

#  1. Count the number of nucletoides
st.subheader("1. Nucletoide count")


def DNA_nucleotide_count(seq):
    # Review dictionary creation in Python
    # We pass the parameter to count. We don't need to define it as it can be passed as something else
    d = dict(
        [
            ("A", seq.count("A")),
            ("T", seq.count("T")),
            ("G", seq.count("G")),
            ("C", seq.count("C")),
        ]
    )
    return d


X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())
# No need to make a print statement in streamlit 'cause it's autommatically displayed

# We need to turn the count to strings in order to being able to add it
st.write("There are " + str(X["A"]) + " adenine (A)")
st.write("There are " + str(X["T"]) + " thymine (T)")
st.write("There are " + str(X["G"]) + " guanine (G)")
st.write("There are " + str(X["C"]) + " cytosine (C)")

# 2. Display DataFrame
# We use pandas as long as we need to display any kind of data in a table (basic Data Science)
# We need to rename them to replace default names
st.subheader("2. Display DataFrame")
df = pd.DataFrame.from_dict(X, orient="index")
df = df.rename({0: "COUNT"}, axis="columns")
df.reset_index(inplace=True)
df = df.rename(columns={"index": "NUCLEOTIDE"})
st.write(df)

# 3. Display Bar Chart using Altair library
# For more displayable data, read Altair documentation
st.subheader("3. Bar Chart")
barChart = (
    alt.Chart(df)
    .mark_bar()
    .encode(x="NUCLEOTIDE", y="COUNT")
    # .configure_axisX(orient="left")
)
# barChart = barChart.orient("left", x)

# To control width of Bar Chart
barChart = barChart.properties(width=alt.Step(100))

st.write(barChart)
