import streamlit as st
import pickle as pkl

# Import your machine learning model

def main():
    st.title("Find your item category!")
    
    # Get input from the user
    item_desc = st.text_input("Enter your item description here:")
    
     # Add a button to clear the text box  
    if st.button("Clear Text"):
          input_text = ""
    if st.button("Get item category"):
        # Call your machine learning model to process the input
          category = get_category(item_desc)
         
    
          # Display the output
          st.write("Output:", category[0])
        

#     if st.button("Reset"):
#           # Use JavaScript to refresh the page
#           st.write("<script type='text/javascript'>window.location.reload();</script>", unsafe_allow_html=True)

def get_category(item_desc):
   
   with open('text_classification_model','rb') as f:
     model = pkl.load(f)
   input = []
   input.append(item_desc)
   reverse_label = {0:'Electronics', 1:'Household', 2:'Books', 3:'Clothing & Accessories'}
   return [reverse_label.get(x) for x in model.predict(input)]

if __name__ == "__main__":
    main()
