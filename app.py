import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


# Function
def generatellamaresponse(input_text,no_words,blog_style):
    
    # Lllam model calling here
    llm=CTransformers(model='model/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                                'temperature':0.01})

    # Llama Templete
    template = """
            write a blog for {blog_style} job profile for a topic {input_text} with {no_words} words.
            """
    # Creating the prompt template
    prompt = PromptTemplate(input_variables=['style','text','n_words'],
                            template=template)

    # Now we Generate the response form Llama model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response


st.set_page_config(page_title="Blog Generation",
            page_icon="|°0°|)",
            layout="centered",
            initial_sidebar_state='collapsed')

st.header("\t\t+++++++============================++++++++++\n")
st.title("\t+🤖      \tBlog Contents Generator   \t+🤖\n")
st.text("\t\t\t----------------------\tcopyright © AI Engineer Eid ----------------------")
st.header("\t\t+++++++============================++++++++++\n")

input_text = st.text_input("Enter the Blog Topic Here")

# Creating two columns for paramaters
col1, col2=st.columns([5,5])
with col1:
    no_words = st.text_input("Number of Words")
with col2:
    blog_style=st.selectbox('Writing the Blog For:',
                            ('APKs', 'Games', 'marketing'), index=0)

submit_btn=st.button("Generate")

# Geting the response of the Prompt
if submit_btn:
    st.write(generatellamaresponse(input_text,no_words,blog_style))