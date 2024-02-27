from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request,'index.html')

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        # Process the image here (e.g., save it to the file system, perform some analysis, etc.)
        image_name = image.name  # Extract the image name
        print(image_name)
        # Pass the processed data to the other function
        return handle_get_request(request, image_name) 
    else:
        return JsonResponse({'error': 'No image file provided.'}, status=400)

def handle_get_request(request,image_name):
    # Process the received data and prepare the response
    # print(image_name)
    if image_name:
        
        return JsonResponse({'message': 'Received filename: {}'.format(image_name)})
    else:
        return JsonResponse({'error': 'No filename provided.'}, status=400)