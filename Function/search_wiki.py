import threading
import wikipedia
from Head.Mouth import speak
from Head.brain import  qa_dict, save_qa_data, qa_file_path, google_search


def wiki_search(prompt):
    search_prompt = prompt.replace("jarvis", "")
    search_prompt = search_prompt.replace("wikipedia", "")

    try:
        wiki_summary = wikipedia.summary(search_prompt, sentences=2)
        speak_thread = threading.Thread(target=speak, args=(wiki_summary,))

        speak_thread.start()

        speak_thread.join()


        qa_dict[search_prompt] = wiki_summary
        save_qa_data(qa_file_path, qa_dict)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There is a disambiguation page for the given query. Please provide more specific information.")
        print("There is a disambiguation page for the given query. Please provide more specific information.")
    except wikipedia.exceptions.PageError:
        google_search(prompt)

