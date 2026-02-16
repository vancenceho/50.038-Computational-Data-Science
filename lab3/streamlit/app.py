import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

# Text/Title
st.title("Streamlit Tutorials")

# Header/Subheader
st.header("This is a header")
st.subheader("This is a subheader")

# Text
st.text("Hello Streamlit")

# Markdown
st.markdown("### This is a Markdown")

st.success("Successful")

st.info("Information!")

st.warning("This is a warning")

st.error("This is an error Danger")

st.exception("NameError('name three not defined')")


# Checkbox
if st.checkbox("Show/Hide"):
	st.text("Showing or Hiding Widget")


# Radio Buttons
status = st.radio("What is your status",("Active","Inactive"))

if status == 'Active':
	st.success("You are Active")
else:
	st.warning("Inactive, Activate")

# SelectBox
occupation = st.selectbox("Your Occupation",["Programmer","DataScientist","Doctor","Businessman"])
st.write("You selected this option ",occupation)


# MultiSelect
location = st.multiselect("Where do you work?",("London","New York","Accra","Kiev","Nepal"))
st.write("You selected",len(location),"locations")

# Slider
level = st.slider("What is your level",1,5)


# Buttons
st.button("Simple Button")

if st.button("About"):
	st.text("Streamlit is Cool")
 
 
 # Receiving User Text Input
firstname = st.text_input("Enter Your Firstname","Type Here..")
if st.button("Submit"):
	result = firstname.title()
	st.success(result)


# Text Area
message = st.text_area("Enter Your message","Type Here..")
if st.button("Submit2"):
	result = message.title()
	st.success(result)

# Date Input
import datetime
today = st.date_input("Today is",datetime.datetime.now())

# Time
the_time = st.time_input("The time is",datetime.time())




# Images
from PIL import Image
img = Image.open("mustango.jpg")
st.image(img,width=300,caption="Simple Image")


# Videos
vid_file = open("output.mov","rb").read()
# vid_bytes = vid_file.read()
st.video(vid_file)

# Audio
audio_file = open("techno.wav","rb").read()
st.audio(audio_file,format='audio/wav')


# Writing Text/Super Fxn
st.write("Text with write")

st.write(range(10))


# Displaying Raw Code
st.text("Display Raw Code")
st.code("import numpy as np")

# Display Raw Code 
with st.echo():
    # This will also show as a comment
    print('test')


data = [[1, 2, 3], [4, 5, 6]]
columns = ['Column_1', 'Column_2', 'Column_3']
df = pd.DataFrame(data, columns=columns)


# Displaying JSON
st.text("Display JSON")
st.json({'name':"Jesse",'gender':"male"})


# Progress Bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)


# Spinner
with st.spinner("Waiting .."):
     time.sleep(5)
     st.success("Finished!")


# Balloons
st.balloons()


# Plot
# Generate some random data for the plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a Matplotlib plot
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sin Wave Plot')

# Display the plot using st.pyplot()
st.pyplot(plt)

# Additional content in the Streamlit app
st.write("This is additional content below the plot.")


# DataFrames
st.dataframe(df)

# Tables
st.table(df)


# SIDEBARS
st.sidebar.header("About")
st.sidebar.text("This is Streamlit Tut")



# Normal Function
def run_fxn():
    return range(100)

st.write(run_fxn())

