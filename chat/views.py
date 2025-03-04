from django.http import StreamingHttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from chat.ask import rag_ask


class RagAPIView(APIView):
    def post(self, request):
        question_request = request.data["question"]
        if not question_request:
            return Response({"error": "Question is required"}, status=400)
        response = StreamingHttpResponse(rag_ask(question_request), status=200, content_type="text/event-stream")
        response['Cache-Control'] = 'no-cache'
        return response
