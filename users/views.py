import csv
from io import TextIOWrapper
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from .serializers import UserSerializer
from .models import User


class UploadCSVView(APIView):
    def post(self, request):
        file = request.FILES.get("file")
        if not file:
            return Response({"error": "No file provided."}, status=status.HTTP_400_BAD_REQUEST)

        if not file.name.endswith(".csv"):
            return Response({"error": "Only CSV files are allowed."}, status=status.HTTP_400_BAD_REQUEST)

        decoded_file = TextIOWrapper(file.file, encoding="utf-8")
        reader = csv.DictReader(decoded_file)

        success_count, error_count = 0, 0
        errors = []

        for row_num, row in enumerate(reader, start=1):
            serializer = UserSerializer(data=row)
            if serializer.is_valid():
                try:
                    serializer.save()
                    success_count += 1
                except IntegrityError:
                    # duplicate email..
                    error_count += 1
                    errors.append({"row": row_num, "errors": {"email": "Duplicate email"}})
            else:
                error_count += 1
                errors.append({"row": row_num, "errors": serializer.errors})

        return Response(
            {
                "records_saved": success_count,
                "records_rejected": error_count,
                "errors": errors,
            },
            status=status.HTTP_200_OK,
        )
