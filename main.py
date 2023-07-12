import spacy
import simplejson as json
from recognizers.fr.frenchrecognizer import FrenchRecognizer
from recognizers.en.englishrecognizer import EnglishRecognizer
from utilities.scrapengine import compute_spacy, compute_openai
from utilities.lohce import fetch_lohce

# Get inputs from user
# path = ""
# culture = ""
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
    should_proceed = False
    # Transcript the audio file
    # result = recognizer.recognize_assembly(path)
    # text = result
    text = "Is there a bus departure from Duala to Yangi tomorrow ?"
    print(text)

    should_proceed = text != None

    if not should_proceed:
        print("An error occurred, you should retry")
    else:
        # text = "Is there a bus departure from Yaounde to Douala tomorrow?"
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
        data = fetch_lohce(source, destination, schedules.strftime("%d-%m-%Y"))
        json_str = json.dumps(data.json(), indent=4, sort_keys=True)
        print(json_str)