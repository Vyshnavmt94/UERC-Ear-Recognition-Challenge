def create_dataset(path,num_classes,data_splitno):
	data_split=[]
    subjects = os.listdir(path) # getting each subject folders (no. of classes=166)
    for subject in subjects[:num_classes]:     ## selcting only 150 classes
        os.makedirs(os.path.join('Data/train',subject))  ## creating new folder for train and test with 60/40 split from each subjects
        os.makedirs(os.path.join('Data/test',subject))
        subject_images = os.listdir(os.path.join(path,train,subject))
        for image in subject_images:
            if(image.endswith('.png')):
                data_split.append(image)
                train_no = int(data_splitno*len(data_split))
		for i in range(0,len(data_split)):
        
			if(i<=train_no-1):
				source_train=os.path.join(path,train,subject,data_split[i])
				destination_train=os.path.join('Data/train',subject)
				shutil.copy(source_train,destination_train)
        
			else:
				source_test=os.path.join(path,train,subject,data_split[i])
				destination_test=os.path.join('Data/test',subject)
				shutil.copy(source_test,destination_test)
			
		data_split=[]  