def data(path):
    images=[]
    label=[]
    subjects = os.listdir(path)
    for subject in subjects:
        subject_path=os.path.join(path,subject)
        subject_images = os.listdir(subject_path)
        for image in subject_images:
            if(image.endswith('.png')):
                image_path=os.path.join(path,subject,image)
                image = cv2.resize(cv2.imread(image_path),(224,224))
                images.append(image)
                label.append(subject)
    
    images=np.array(images)
    label=np.array(label)
    return images,label