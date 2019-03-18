def get_augmented_data(path):
    subjects = os.listdir(path)
    for subject in subjects:
        subject_path=os.path.join(path,subject)
        subject_images = os.listdir(subject_path)
        for image in subject_images:
            if(image.endswith('.png')):
                image_path=os.path.join(path,subject,image)
                image = cv2.resize(cv2.imread(image_path),(100,100))
                im_path=os.path.join(os.path.splitext(image_path)[0])
                data_augmentation(image,im_path)