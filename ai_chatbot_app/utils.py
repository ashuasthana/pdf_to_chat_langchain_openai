def convert_to_vector(file):
    # Implement document to vector conversion here based on the file type
    # For text files (txt), you can use libraries like spaCy, gensim, or scikit-learn
    # For images (img), you can use libraries like OpenCV or TensorFlow

    # Example for text files (assuming you have spaCy installed)
    import spacy

    # Load spaCy's English model
    nlp = spacy.load('en_core_web_sm')

    # Read the content of the file using 'latin-1' encoding
    text = file.read().decode('latin-1')

    # Process the text using spaCy
    doc = nlp(text)

    # Convert spaCy's Doc object to a list for storage
    vector = doc.vector.tolist()

    return vector
