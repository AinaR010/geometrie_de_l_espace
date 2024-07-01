import json

def addition(a, b):
    return a + b

def lambda_handler(event, context):
    try:
        # Récupérer les valeurs de a et b depuis l'événement
        a = int(event.get('queryStringParameters', {}).get('a', 0))
        b = int(event.get('queryStringParameters', {}).get('b', 0))

        # Effectuer l'addition en utilisant la fonction
        result = addition(a, b)

        # Créer la réponse JSON
        response = {
            "statusCode": 200,
            "body": json.dumps({
                "result": result
            })
        }

    except Exception as e:
        response = {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }

    return response
