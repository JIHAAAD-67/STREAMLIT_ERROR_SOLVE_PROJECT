from google import genai
from dotenv import load_dotenv
import os
import streamlit as st
import io
load_dotenv()
my_api_key=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=my_api_key)




def ErrorExp(images):
    prompt="""Find out the errors from the screenshots of the code and explain them in details, make sure every error is explained properly"""
    response=client.models.generate_content(
       model="gemini-3-flash-preview",
       contents=[images,prompt]
    )
    return response.text


def CorrCode(images,Solution):
    prompt=f"Write the corrected code only when {Solution} is selected"
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images,prompt]
    )
    return response.text