from django.http import HttpResponse
from django.shortcuts import render
from PyPDF2 import PdfFileMerger
import os
from django.conf import settings

# Create your views here.

def upload_and_merge(request):
    if request.method == 'POST' and request.FILES.getlist('pdf_files'):
        # Get the uploaded PDF files
        pdf_files = request.FIles.getlist('pdf_files')

        # Merge the PDF files
        merger = PdfFileMerger()

        for pdf_file in pdf_files:
            merger.append(pdf_file)

        # Save the merged PDF to a file

        output_path = os.path.join(settings.MEDIA_ROOT, 'merged.pdf')
        with open(output_path, 'wb') as output_file:
            merger.write(output_file)
        merger.close()


        with open(output_path, 'rb') as output_file:
            response = HttpResponse(output_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="merged.pdf"'
            return response

    return render(request, 'merger/upload.html')