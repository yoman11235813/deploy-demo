import streamlit as st

# st.title("This is the title")
# st.header("This is the header")
# st.subheader("This is the subheader")
# st.markdown("**This** is the *markdown*")
# st.caption("This is the caption")
# st.code("import streamlit as st")
# st.latex(r''' MSE = \frac 1 N\sum(y - \hat y)^2 ''')

# st.checkbox('I am not a robot')
# st.radio('Do you like NLP?',['Yes','No', 'Maybe'])
# st.selectbox('Pick a school',['NTHU','NYCU'])
# st.multiselect("Favorite colors?",['Red','Blue','White'])
# st.slider('Pick a number', 0,50)

# st.text_input('Name')
# st.number_input('Age', 0,100)
# st.text_area('Description')
# st.file_uploader('Upload a file')

form = st.form(key='form-name')
name = form.text_input('What is your name?')
submit = form.form_submit_button('Submit')

if submit:
    st.write(f'Hi {name}!')











