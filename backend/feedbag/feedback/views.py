from django.db.models import Q
from rest_framework import viewsets
from rest_framework import serializers

from .models import Rating, Remark, Question, Feedback
from .serializers import RatingSerializer, RemarkSerializer, QuestionSerializer, FeedbackSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class RemarkViewSet(viewsets.ModelViewSet):
    queryset = Remark.objects.all()
    serializer_class = RemarkSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows questions to be viewed or added.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        """
        Set the queryset here so it filters on user.
        """
        return super(FeedbackViewSet, self).get_queryset().filter(Q(sender=self.request.user) |
                                                                  Q(recipient=self.request.user))
