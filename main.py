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
    text = recognizer.recognize_assembly(path)
    print("\nQuery:",text)

    should_proceed = text != None

    if not should_proceed:
        print("An error occurred, you should retry")
    else:
        # Get the source, destination and schedule from the text
        source, destination, schedules = compute_spacy(text, nlp)

        # Print out the results
        print("\nSource: ", source)
        print("Destination: ", destination)
        print("Schedules: ", schedules)

        # Call to the lohce api
        data = fetch_lohce(source, destination, schedules.strftime("%d-%m-%Y"))
        json_str = json.dumps(data.json(), indent=4, sort_keys=True)

        print("\nResponse:\n")
        print(json_str)
