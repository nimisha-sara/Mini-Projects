import pandas as pd
from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

SCOPES = "https://www.googleapis.com/auth/forms.body"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

store = file.Storage("token.json")
creds = None

if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets("client_secret.json", SCOPES)
    creds = tools.run_flow(flow, store)

form_service = discovery.build(
    "forms",
    "v1",
    http=creds.authorize(Http()),
    discoveryServiceUrl=DISCOVERY_DOC,
    static_discovery=False,
)

def create_google_form_from_excel(excel_file, num_rows):
    df = pd.read_excel(excel_file, nrows=num_rows)

    NEW_FORM = {
        "info": {
            "title": " Quiz",
        }
    }

    question_requests = []
    
    question_requests.append({
        "updateSettings": {
                "settings": {
                    "quizSettings": {
                        "isQuiz": True
                        }
                    },
                "updateMask": "quizSettings.isQuiz",
            }
        }
    )

    for index, row in df.iterrows():
        question = row['Question']
        options = [row[f'Option {i+1}'] for i in range(4)]  # Extract options dynamically
        correct_answer = row['Answer']

        question_request = {
            "createItem": {
                "item": {
                    "title": question,
                    "questionItem": {
                        "question": {
                            "required": True,
                            "grading": {
                                "pointValue": 1,
                                "correctAnswers": {
                                    "answers": [{"value": options[correct_answer - 1]}]  # Convert answer number to option value
                                }
                            },
                            "choiceQuestion": {
                                "type": "RADIO",
                                "options": [{"value": option} for option in options],
                                "shuffle": True,
                            },
                        }
                    },
                },
                "location": {"index": index},  # Specify index to maintain order
            }
        }
        question_requests.append(question_request)

    # Creating initial form
    result = form_service.forms().create(body=NEW_FORM).execute()

    question_setting = form_service.forms().batchUpdate(
        formId=result["formId"], body={"requests": question_requests}
    ).execute()

    get_result = form_service.forms().get(formId=result["formId"]).execute()
    print(f"Form created successfully! \nForm ID: {result['formId']}\nURL: {result['responderUri']}")

create_google_form_from_excel("questions.xlsx", num_rows=50)  # Change the filename and number of rows as needed
