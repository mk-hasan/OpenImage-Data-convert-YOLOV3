## Make YOLO format data label from OpenImage dataset

# DataSet Description
- **Train** : 1.7 million almost
- **Test** : 125k almost
- **Validation** : 40k almost

# Data label from OpenImage annotations csv file 
![sample oi data labels](/oiorig.png)

**The yolo format**
![sample oi data labels](/oiconv.png)

# What you can do with this python(Jupyter) file
* Creat yolo v2/v3 format labels 
* Creat single class to n(600) class labels
* Create hierarcichal labels (Animals, Vehicles, Toy)

# Requiremnts
- Only need the Train, Test and Validation dataset from OpenImage website
- Jupyter Notebook (Python)
- Python and Pandas
- Need powerful workstation as the Train CSV has 14 million row, it takes long time to process this amound of rows. I sued server consists of 2TB RAM though :p

# Hierarcical Labeling
- Sometimes people may need to train the model with the parent class of some subclass (For ex, i trained with Animal class, under Animal there are Tiger, Dog,Cat , etc subclass belongs to. So if you want to train with only Animal then you can do that also, buy mapping the sub class labelName to Parent class LabelName according to the hirarcical format of OpenImage dataset)

# Step to do this
- 1) Load csv files
- 2) Give catagorical class label to class number(ClassID)
- 3) Rearrange dataset column to yolo style format (ClassId, X1,Y1,X2,Y2) 
- 4) Write those classId and Bouding-Box to labels/train or labels/test folder with .txt format for each image
- 5) Write image file location into tran.txt and test.txt file

# If you have questions, please open a issue and if it helps, give star. Thanks !!!!

**Yeee ** Evrything is fine now. You can start training for yolo with Open Image so easily. This is the easiest way to do this work

## I have other repo for creating COCO dataset tfrecord for tensorflow (single class or multi class, overlapping iamge or withour overlapping image in a single image). You can check it out in my repo
