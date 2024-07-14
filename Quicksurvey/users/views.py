from django.shortcuts import render
from rest_framework import generics
from .models import Forms, Questions, QuestionsInForms, Responses
from .serializers import FormSerializers, QuestionsInFormsSerializers, ResponsesSerializers, QuestionsSerializers

def login(request):
    return render(request, 'users/login.html')

class FormsCreateView(generics.ListCreateAPIView):
    queryset = Forms.objects.all()
    serializer_class = FormSerializers
    # permission_classes = [IsAuthenticated, IsSuperUser]


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class QuestionsCreateView(generics.ListCreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializers


class QuestionsInFormsCreateView(generics.ListCreateAPIView):
    queryset = QuestionsInForms.objects.all()
    serializer_class = QuestionsInFormsSerializers



class ResponsesCreateView(generics.ListCreateAPIView):
    queryset = Responses.objects.all()
    serializer_class = ResponsesSerializers



# ---Forms---
class FormsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Forms.objects.all()
    serializer_class = FormSerializers
    # permission_classes = [IsAuthenticated, IsSuperUser]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# ---Question---#
class QuestionsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializers


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# ---QuestionsInForms---
class QuestionsInFormsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsInFormsSerializers
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# ---Responses---
class ResponsesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Responses.objects.all()
    serializer_class = ResponsesSerializers
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# --- Handling Submission----

