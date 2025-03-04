from django.http import StreamingHttpResponse
from rest_framework.views import APIView

from chat.ask import rag_ask


class RagAPIView(APIView):
    def post(self, request):
        question_request = request.data["question"]
        response = StreamingHttpResponse(rag_ask(question_request), status=200, content_type="application/json")
        response['Cache-Control'] = 'no-cache'

        print("Returning response.")

        return response
