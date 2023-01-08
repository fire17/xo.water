import pytesseract
from PIL import Image
from google.cloud import vision

class DocumentEditor:
    def __init__(self, document_path):
        self.document_path = document_path
        self.image = Image.open(document_path)
        self.client = vision.ImageAnnotatorClient()

    def FindAndReplace(self, text_to_find, new_text):
        # Use Tesseract to find the text in the image
        text = pytesseract.image_to_string(self.image)
        if text_to_find not in text:
            print("Text not found in document")
            return
        
        # Use Google Cloud Vision API to detect the location and font of the text
        response = self.client.text_detection(image=self.image)
        text_annotations = response.text_annotations
        for annotation in text_annotations:
            if annotation.description == text_to_find:
                x1, y1, x2, y2 = annotation.bounding_poly.vertices[0].x, annotation.bounding_poly.vertices[0].y, annotation.bounding_poly.vertices[2].x, annotation.bounding_poly.vertices[2].y
                font = annotation.font.family
                font_size = annotation.font.size
                break
        
        # Pass the cropped image and new text to the Replace method
        self.Replace((x1, y1, x2, y2), new_text)

    def Replace(self, crop_coords, new_text):
        # Crop the image to the selected area
        cropped_image = self.image.crop(crop_coords)

        # Use PIL to draw the new text on the original image
        draw = PIL.ImageDraw.Draw(self.image)
        draw.text(crop_coords[:2], new_text, font=font, fill=(0, 0, 0), font_size=font_size)

        # Save the edited image
        self.image.save('edited_document.jpg')
