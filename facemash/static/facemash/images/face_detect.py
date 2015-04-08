
import os 
import cv2,cv
import sys
import math
import django
django.setup()
from facemash.models import User

# Get user supplied values


def findFace(image):
	cascPath = 'haarcascade_frontalface_default.xml'
	faceCascade = cv2.CascadeClassifier(cascPath)
	faces = faceCascade.detectMultiScale(
	    image,
	    scaleFactor=1.1,
	    minNeighbors=5,
	    minSize=(30, 30),
	    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	)

	print "Found {0} faces!".format(len(faces))

	# Draw a rectangle around the faces
	if len(faces) > 0:
		return faces[0]
	else:
		return None

def makeSquares(l):
	for u in l:
		img = cv2.imread('{0}.jpg'.format(u.user_id))
		face = findFace(img)
		print u.user_id
		width, height = cv.GetSize(cv.fromarray(img))
		#img[y: y + h, x: x + w]
		#face[x,y,w,h]
		print 'Face: ',face

		if face != None:
			center = (face[0]+float(face[2])/2,face[1]+float(face[3])/2)
			if width > height:
				if center[0]+height/2 < width:
					img = img[(0):(height),(0):(height)]
				elif center[0]+height/2 > width:
					img = img[(0):(height),(width-height):(width)]
				else:
					img = img[(0):(height),(max(center[0]-height/2,0)):(min(center[0]+height/2,height))]
			elif height > width:
				if center[1]+width/2 < height:
					img = img[(0):(width),(0):(width)]
				elif center[1]+width/2 > height:
					img = img[(height-width):(height),(0):(width)]
				else:
					img = img[(max(center[1]-width/2,0)):(min(center[1]+width/2,width)),(0):(width)]
		else:
			if width > height:
				img = img[(0):(height),(0):(height)]
				print [(0),(height),(0),(height)]
			elif height > width:
				img = img[(0):(width),(0):(width)]
		cv2.imwrite('cropped/{0}.jpg'.format(u.user_id),img)
   

def get_files_by_file_size(dirname, reverse=False):
    """ Return list of file paths in directory sorted by file size """

    # Get list of files
    filepaths = []
    for basename in os.listdir(dirname):
        filename = os.path.join(dirname, basename)
        if os.path.isfile(filename):
            filepaths.append(filename)

    # Re-populate list with filename, size tuples
    for i in xrange(len(filepaths)):
        filepaths[i] = (filepaths[i], os.path.getsize(filepaths[i]))

    # Sort list by file size
    # If reverse=True sort from largest to smallest
    # If reverse=False sort from smallest to largest
    filepaths.sort(key=lambda filename: filename[1], reverse=reverse)

    # Re-populate list with just filenames
    # for i in xrange(len(filepaths)):
    #     filepaths[i] = filepaths[i][0]

    return filepaths

# paths = [i[0] for i in get_files_by_file_size('cropped/') if i[1] == 0]
makeSquares(User.objects.all())



