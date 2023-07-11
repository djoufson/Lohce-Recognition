import json
import spacy
from recognizers.fr.frenchrecognizer import FrenchRecognizer
from recognizers.en.englishrecognizer import EnglishRecognizer
from utilities.scrapengine import compute_spacy, compute_openai

# Get inputs from user
path = input("Enter the path of the audio file: ")
culture = input("Enter the culture (en, fr): ")

supported = False
# Initialize recognizer and nlp based on the specified culture
if culture == "fr":
    print("This culture is not supported yet")
    recognizer = FrenchRecognizer()
    nlp = spacy.load("en_core_web_sm")

else:
    culture = "en"
    supported = True
    recognizer = EnglishRecognizer()
    nlp = spacy.load("fr_core_news_sm")

if supported:
    # Transcript the audio file
    result = recognizer.recognize(path)
    text = json.loads(result)['text']
    print(text)
    # text = "Is there a bus departure from Douala to Yaounde tomorrow?"
    # text = "I want to travel from New York to Los Angeles on January 1st, 2022 at 9am."

    # Get the source, destination and schedule from the text
    source, destination, schedules = compute_spacy(text, nlp, language=culture)

    # Print out the results
    print("Source: ", source)
    print("Destination: ", destination)
    print("Schedules: ", schedules)
