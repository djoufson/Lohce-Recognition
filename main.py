import spacy
from recognizers.fr.frenchrecognizer import FrenchRecognizer
from recognizers.en.englishrecognizer import EnglishRecognizer
from utilities.scrapengine import compute_spacy, compute_openai
from utilities.lohce import fetch_lohce

# Get inputs from user
path = input("Enter the path of the audio file: ")
culture = input("Enter the culture (en, fr): ")

supported = False
# Initialize recognizer and nlp based on the specified culture
if culture == "fr":
    print("This culture is not supported yet")
    recognizer = FrenchRecognizer()
    nlp = spacy.load("fr_core_news_sm")

else:
    culture = "en"
    supported = True
    recognizer = EnglishRecognizer()
    nlp = spacy.load("en_core_web_sm")

if supported:
    # Transcript the audio file
    result = recognizer.recognize_assembly(path)
    text = result
    print(text)

    text = "Is there a bus departure from Yaounde to Douala tomorrow?"
    # Get the source, destination and schedule from the text
    source, destination, schedules = compute_spacy(text, nlp)

    # Print out the results
    print("Source: ", source)
    print("Destination: ", destination)
    print("Schedules: ", schedules)

    # source = "Yaounde"
    # destination = "Douala"
    # schedules = "12-07-2023"

    # Call to the lohce api
    response = fetch_lohce(source, destination, schedules.strftime("%d-%m-%Y"))
    print(response.status_code)
