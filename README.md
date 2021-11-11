# RUG_Information_Retrieval

## Assignment 6

Implementing a face recognition algorith using cosine difference algorithm.

Application Usage:

Our program is very easy to use, user must choose the value for rejection threshhold, number of known people and number of training images per person then to compile the python file, which can be done by the following command : 
```bash
$ python3 face_recognition.py
```

During our testing we have tried to experiment with the values of **Rejection Threshhold** between 0.1 and 1, **Number of known people and number of training images per person** with the values 5 and 10 (maximum amount of pictures available)

When analyzing the output we found the following :

Rejection threshhold affects the accuracy, the lower the threshhold is the higher accuracy we get, this is due to the fact that we "accept" only the images with the lowest possible cosine difference, meaning that the face of the compared person is the most similar as it could be to the known person.

When we increase the number of known people, the accuracy also gets higher (considering we compare with the output having the same rejection threshhold and number of trained images per person), this is caused by the fact that the more people our algorithm knows, the more testing images are accepted.

When we decrease the number of training images per person (considering we compare with the output having the same parameters as before) we observe that the accuracy also decreases, this is due to the fact that less images are supplied, and therefore there are less comparisons of the test image with the ones from database. For example, if we don't have a lot of images with the person, or images with some changes such as : glasses, beard and so on, when we encounter such a image in the test section, the algorithm can not properly compare it to the existing one.

Below is the output for all our tests. The output prints also the parameters used to generate it.



<img width="394" alt="thresh0 2" src="https://user-images.githubusercontent.com/61204251/141375316-66a9a365-48da-4475-bd4e-54d1a540619b.png">
<img width="478" alt="thresh0 5" src="https://user-images.githubusercontent.com/61204251/141375319-597e42d1-9321-4c29-bb22-78a313b8bc85.png">
<img width="449" alt="thresh0 75" src="https://user-images.githubusercontent.com/61204251/141375322-c889f152-1f81-4477-9fef-8ca151a00095.png">

<img width="489" alt="img1" src="https://user-images.githubusercontent.com/61204251/141375350-0012da00-5fd9-4cbb-9249-37044aab9895.png">
<img width="507" alt="img3" src="https://user-images.githubusercontent.com/61204251/141375357-4cdf80f7-890f-4622-bfb0-ecedc4f33b7e.png">
<img width="517" alt="img5" src="https://user-images.githubusercontent.com/61204251/141375363-0fe4ce29-fb5a-46b9-932d-d82838135c35.png">
<img width="467" alt="img8" src="https://user-images.githubusercontent.com/61204251/141375365-628f7e78-21b1-4e30-a2d2-f7fca14d8774.png">

<img width="382" alt="people3" src="https://user-images.githubusercontent.com/61204251/141375368-e684f04b-3c6d-4bc4-aff0-fe9e522be5b9.png">
<img width="497" alt="people5" src="https://user-images.githubusercontent.com/61204251/141375370-7cba3bc6-ed54-4b8b-bc9e-c3b787ad8989.png">
<img width="477" alt="people8" src="https://user-images.githubusercontent.com/61204251/141375373-b13747b3-3d6e-4f04-a660-e50d055ed914.png">

