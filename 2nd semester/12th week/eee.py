from google.cloud import api_keys_v2
from google.cloud import dialogflow


def create_api_key(project_id):
    client = api_keys_v2.ApiKeysClient()

    key = api_keys_v2.Key()
    key.display_name = "My first API key"

    request = api_keys_v2.CreateKeyRequest()
    request.parent = f"projects/{project_id}/locations/global"
    request.key = key

    response = client.create_key(request=request).result()
    return response


def detect_intent_text(project_id, session_id, message_to_dialogflow, language_code='ru'):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=message_to_dialogflow, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    serialized_answer = {
        'intention': response.query_result.intent.display_name,
        'confidence': response.query_result.intent_detection_confidence,
        'answer': response.query_result.fulfillment_text
    }
    return serialized_answer

if __name__ == '__main__':
    project_id = 'cool_test_xson'
    session_id = 'test'
    message_to_dialogflow = 'привет'

    token = create_api_key(project_id)
    print("Successfully created an API key")
    serialized_answer = detect_intent_text(project_id, session_id, message_to_dialogflow)
    print(f"Вопрос: {message_to_dialogflow}")
    print("Намерение: {}, (вероятность: {})".format(
            serialized_answer['intention'],
            serialized_answer['confidence'],
        )
    )
    print(f'Ответ: {serialized_answer["answer"]}')