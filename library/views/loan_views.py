from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.loan import Loan
from ..serializers import LoanSerializer, LoanReadSerializer

# Create your views here.
#localhost:8000/library/loans/ get post
class LoansView(APIView):
    """View class for loans/ for viewing all and creating"""
    serializer_class = LoanSerializer
    def get(self, request):
        loans = Loan.objects.all()
        serializer = LoanReadSerializer(loans, many=True)
        return Response({'loans': serializer.data})

    def post(self, request):
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#localhost:8000/library/loans/:id get delete update
class LoanDetailView(APIView):
    """View class for loans/:pk for viewing a single loan, updating a single loan, or removing a single loan"""
    serializer_class = LoanSerializer
    def get(self, request, pk):
        loan = get_object_or_404(Loan, pk=pk)
        serializer = LoanReadSerializer(loan)
        return Response({'loan': serializer.data})

    def patch(self, request, pk):
        loan = get_object_or_404(Loan, pk=pk)
        serializer = LoanSerializer(loan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        loan = get_object_or_404(Loan, pk=pk)
        loan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)