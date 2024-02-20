from django.shortcuts import render
from ai_chatbot_app.forms import AskQuestionForm
from .forms import DocumentForm
from .utils import convert_to_vector
from .langchain import langchain_pdfChat
from .models import Document
from PyPDF2 import PdfReader

# from langchain.document_loaders import PyPDFLoader
# ============================Create your Views for Ask Qustion===========================
def question_view(request):
    if request.method == 'POST':
        form = AskQuestionForm(request.POST)
        if form.is_valid():
                
                # Extract question from form data
                question = form.cleaned_data['question']
                # print(question)
                #Extract data from save pdf in DB
                pdf=Document.objects.filter(title='India')
                print("================")
                for i in pdf:
                    pdf_path=i.file

                #Create pdf file path    
                pdf_path = f"media/{pdf_path}" 

                #Extract text 
                # Open the PDF file
                # creating a pdf reader object 
                reader = PdfReader(pdf_path) 
                
                # printing number of pages in pdf file 
                # print(len(reader.pages)) 
                
                # getting a specific page from the pdf file 
                page = reader.pages[0] 
                
                # extracting text from page 
                text = page.extract_text() 
                # print(text) 

                pdf_read=PdfReader(pdf_path)
                print(pdf_read)
                
                # Invoke OpenAI with the question
                # response=langchain_pdfChat(question)
                # Debugging: Print response to console3
                
                
                ai_answer=langchain_pdfChat(question,text)
                print("Response from OpenAI:", ai_answer)
                
                # Render the response to the template
                response={"text":text,"pdf_path":pdf_path,"ai_answer":ai_answer}
                return render(request, 'ai_chatbot_app/index.html', {'question': question, 'response': response})          
    else:
        form = AskQuestionForm()
    return render(request, 'ai_chatbot_app/index.html', {'form': form})



#Create view for uploading Document.Only Admin use
def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.vector = convert_to_vector(document.file)  # Implement this function
            document.save()
            return render(request, 'ai_chatbot_app/upload_success.html')
    else:
        form = DocumentForm()
    return render(request, 'ai_chatbot_app/upload_document.html', {'form': form})
