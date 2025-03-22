import os
import json
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from PyPDF2 import PdfMerger

def upload_and_merge(request):
    if request.method == 'POST' and request.FILES.getlist('pdf_files'):
        # Step 1: Get the uploaded files
        pdf_files = request.FILES.getlist('pdf_files')

        # Step 2: Initialize PdfMerger
        merger = PdfMerger()

        # Step 3: Merge the PDFs
        for pdf in pdf_files:
            merger.append(pdf)

        # Step 4: Ensure the media directory exists
        media_root = settings.MEDIA_ROOT
        if not os.path.exists(media_root):
            os.makedirs(media_root)

        # Step 5: Save the merged PDF to a temporary file
        output_filename = 'merged.pdf'
        output_path = os.path.join(media_root, output_filename)
        with open(output_path, 'wb') as output_file:
            merger.write(output_file)
        merger.close()

        # Step 6: Return the URL of the merged file as a JSON response
        merged_file_url = os.path.join(settings.MEDIA_URL, output_filename)
        return JsonResponse({'merged_file_url': merged_file_url})

    # Step 7: Render the upload form for GET requests
    return render(request, 'merger/upload.html')