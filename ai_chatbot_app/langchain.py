import openai
from langchain_openai import ChatOpenAI
from langchain.prompts import SystemMessagePromptTemplate,HumanMessagePromptTemplate,ChatPromptTemplate
from django.conf import settings  # Import Django settings module

# ============================Create your Views for Ask Qustion===========================
def langchain_pdfChat(question,sourece):
         # Initialize OpenAI client with the API key
        print(question," :",sourece)
        openai.api_key = settings.OPENAI_API_KEY
        # pass
        # Extract question from form data
    
        # print(question)
                
        # Instantiate OpenAI client
        # llm = OpenAI(openai_api_key=openai.api_key)
        llm = ChatOpenAI(openai_api_key=openai.api_key)
        
        # System Prompt for Trending Topic

        systemMessagePrompt = SystemMessagePromptTemplate.from_template(f'Only you give answer from this text: "{sourece}" , if asked question not on the this text so you say only "I dont know." in one line ')

        #Ask Question agest given text Trending to Human prompt:

        humanMessagePrompt = HumanMessagePromptTemplate.from_template('{ask_question}')
        
        chat_prompt = ChatPromptTemplate.from_messages([systemMessagePrompt,humanMessagePrompt])


        #Formatted Chat Prompt:
        formatted_chat_prompt = chat_prompt.format_messages(ask_question = question)
        print(formatted_chat_prompt)

        # Invoke OpenAI with the question
        response = llm.invoke(formatted_chat_prompt)
        
        # print("=========try=Invoke OpenAI with the question=")
       
        # Render the response to the template
        return response        
 


