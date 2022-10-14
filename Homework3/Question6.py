import cv2 
  
# Read the image. 
img = cv2.imread('you_image.jpg') 
  
# Apply bilateral filter
bilateral = cv2.bilateralFilter(img, 15, 75, 75)
  
# Save the output. 
cv2.imwrite('bilateral.jpg', bilateral) 
