def data_augmentation(image,path):
    flip =iaa.Sequential([iaa.Fliplr(0.5)]).augment_images(image)
    io.imsave(path+'flip.png',flip)
    
    crop = iaa.Sequential([iaa.Crop(percent=(0,0.01))]).augment_images(image)
    io.imsave(path+'crop.png',crop)
    
    GB = iaa.Sequential([iaa.GaussianBlur(sigma=(0,3.0))]).augment_images(image)
    io.imsave(path+'GB.png',GB)
    
    GN = iaa.Sequential([iaa.AdditiveGaussianNoise(scale=(0.0,0.2))]).augment_images(image)
    io.imsave(path+'GN.png',GN)
    
    CN = iaa.Sequential([iaa.ContrastNormalization(0.5,per_channel=0.5)]).augment_images(image)
    io.imsave(path+'CN.png',CN)
    
    BR = iaa.Sequential([iaa.Multiply((0.8,1.2))]).augment_images(image)
    io.imsave(path+'BR.png',BR)
    
    scale= iaa.Sequential([iaa.Affine(scale={"x": (0.8, 1.2), "y": (0.8,1.2)})]).augment_images(image)
    io.imsave(path+'scale.png',scale)
    
    rotate = iaa.Sequential([iaa.Affine(rotate=(-45,45))]).augment_images(image)
    io.imsave(path+'rotate.png',rotate)
    