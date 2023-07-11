import openai

def compute_spacy(text, nlp, language = "en"):
    doc = nlp(text)
    source = ""
    destination = ""
    schedules = ""
    
    if language == "fr":
        for ent in doc.ents:
            if ent.label_ == "LOC":
                if not source:
                    source = ent.text
                elif not destination:
                    destination = ent.text
            elif ent.label_ == "DATE":
                schedules = ent.text

    else:
        for ent in doc.ents:
            if ent.label_ == "GPE":
                if not source:
                    source = ent.text
                elif not destination:
                    destination = ent.text
            elif ent.label_ == "DATE":
                schedules = ent.text

    return source, destination, schedules

def compute_openai(text, language = "en"):
    source = ""
    destination = ""
    schedule = ""

    if language == "fr":
        query = "The text I will provide is in french and I want you to extract the Source, Destination and Schedule from this text"
        queue = "The output should only be those three informations separated by commas"
    else:
        query = "I want you to extract the Source, Destination and Schedule from this text"
        queue = "The output should only be those three informations separated by commas"

    API_KEY = open('utilities/api_key.txt', 'r').read()
    openai.api_key = API_KEY
    response =openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"{query}: '{text}' \n{queue}"}
        ]
    )

    print(response)
    return (source, destination, schedule)
