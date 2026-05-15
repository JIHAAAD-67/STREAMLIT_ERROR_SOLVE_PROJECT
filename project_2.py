import streamlit as st
from api_call import ErrorExp,CorrCode
from PIL import Image
st.title("AI Code Debugger Application")
st.markdown("Upload your images of code error")
st.divider()

st.header("Controls")
images=st.file_uploader(
        "Upload the photo of your code",type=['jpg','jpeg','png','webp'],accept_multiple_files=True
    )
pil_images=[]
for img in images:
        pil_image=Image.open(img)
        pil_images.append(pil_image)
if images:
    if len(images)>3:
        st.error("Upload at max 3 SS")
    else:
        st.subheader("Your uploaded ScreenShots")
        col=st.columns(len(images)) 
        for i,img in enumerate(images):
         with col[i]:
             st.image(img)      



selected_option=st.selectbox(
    "DO you want Hints to solve the error or Solutions to those Error with code",("Hints","Solution With Code"),index=None 
    )


pressed=st.button("Click the button to initiate AI",type="primary")


if pressed:
    if not images:
        st.error("You must upload a image")
    if not selected_option:
        st.error("You must say if you want Hint or soultion")

    if images and selected_option=="Hints":
        with st.container(border=True):
           st.subheader("Error Explanation")
           with st.spinner("AI is finding your errors"):
               Error_Explanation=ErrorExp(pil_images)
               st.markdown(Error_Explanation)
               
    if images and selected_option=="Solution With Code":
       with st.container(border=True):
           st.subheader("Error Explanation")
           with st.spinner("AI is finding your errors"):
               Error_Explanation=ErrorExp(pil_images)
               st.markdown(Error_Explanation)

       
       with st.container(border=True):
           st.subheader("Corrected Code")
           with st.spinner("AI is generating your correct code:)"):  
              Cor_coDe=CorrCode(pil_images,selected_option)  
              st.markdown(Cor_coDe)   