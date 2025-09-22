from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class UploadCSVTests(APITestCase):
    def test_upload_valid_csv(self):
        csv_content = b"name,email,age\nAkshay,akshay@gmail.com,30\nSurya,surya@example.com,25"
        uploaded_file = SimpleUploadedFile(
            "test.csv",
            csv_content,
            content_type="text/csv"
        )
        response = self.client.post(
            reverse("upload-csv"),
            {"file": uploaded_file},
            format="multipart"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["records_saved"], 2)
