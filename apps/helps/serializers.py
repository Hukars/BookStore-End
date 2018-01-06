from rest_framework import serializers
from .models import CommonProblem,SystemRule

class CommonProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonProblem
        fields = ('questionId','questionName','questionSolution')
class SystemRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemRule
        fields = ('ruleId','ruleDetail')