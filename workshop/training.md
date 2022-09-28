# Personalize Training과 Campaign 생성 

[Personalize Workshop](https://github.com/kyopark2014/aws-personalize/blob/main/workshop.md)에서 [전처리한 Dataset](https://github.com/kyopark2014/aws-personalize/blob/main/src/personalize-preprocessing-job_22Sep2022_1663810890438_part00000.csv)을 가지고 학습(Training)을 하고, Campaign으로 배포할 수 있습니다. 

1) [Personalize Console](https://ap-northeast-2.console.aws.amazon.com/personalize/home?region=ap-northeast-2#createDatasetGroup)로 진입하여, [Name]으로 "personalize-dataset"이라고 입력하고, 아래처럼 [Domain]으로 "Custom"을 선택합니다. 이후 [Create dataset group and continue]을 선택합니다. 

<img src="https://user-images.githubusercontent.com/52392004/191674302-1783ffe8-ad4d-4839-aa02-e490cfe18054.png" width="600">
 
2) 아래와 같이 [Configure interactions schema]에서 [Dataset name]을 "personalize-dataset"으로 하고, [Schema name]을 "personalize-shcema"로 설정합니다. 이후 아래로 스크롤하여 [Next]를 선택합니다. 

<img src="https://user-images.githubusercontent.com/52392004/191698093-450de98e-7b53-4223-af87-0d0c9484bd99.png" width="600">
 
3)  [Configure interactions dataset import job]에서 [Dataset import job name]으로 "personalize-import-job"을 입력합니다.

<img src="https://user-images.githubusercontent.com/52392004/191698972-c36ef22d-2b7f-457d-bfe3-f66e983f8ea1.png" width="600">


4) [Data import source]에 아래와 같이 preprcessing 단계에서 생성한 csv 파일의 S3 경로를 입력합니다.

<img src="https://user-images.githubusercontent.com/52392004/191702956-1d49ab46-8350-4882-b8c5-f932b8033cdf.png" width="600">

5) S3의 dataset 경로에 대한 permission을 설정합니다.

[S3 Console](https://s3.console.aws.amazon.com/s3/buckets?region=us-east-1)에서 기생성한 bucket인 "personalize-dataset-ksp"한 후에 아래처럼 [Permission]을 선택합니다. 

<img src="https://user-images.githubusercontent.com/52392004/191704536-c8a6f92b-a38b-48ad-9d71-5ebac89e7d98.png" width="400">

아래와 같이 [Bucket policy]에서 [Edit]를 선택합니다. 

<img src="https://user-images.githubusercontent.com/52392004/191705105-94a4953b-3dae-4119-b2a2-8587b5b12690.png" width="800">

아래의 Policy를 넣고 [Save changes]를 선택합니다.

```java
{
    "Version": "2012-10-17",
    "Id": "PersonalizeS3BucketAccessPolicy",
    "Statement": [
        {
            "Sid": "PersonalizeS3BucketAccessPolicy",
            "Effect": "Allow",
            "Principal": {
                "Service": "personalize.amazonaws.com"
            },
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::personalize-dataset-ksp",
                "arn:aws:s3:::personalize-dataset-ksp/*"
            ]
        }
    ]
}
```


6) 아래로 스크롤하여 [IAM Role]에서 "Create a new role"을 선택합니다.


<img src="https://user-images.githubusercontent.com/52392004/191699699-b17b1434-8789-443b-bf6f-f3195d8af4a0.png" width="600">

이후 나오는 팝업에서 아래와 같이 [S3 buckets you specify]을 "Any S3 bucket"로 설정합니다. 

<img src="https://user-images.githubusercontent.com/52392004/191700496-9a41983a-7bc1-4f2a-9747-aa12f0ea74d6.png" width="700">

7) 아래와 같이 IAM Role이 생성된것을 확인후에 [Start import]를 선택합니다. 

<img src="https://user-images.githubusercontent.com/52392004/191701095-4df645a9-11ce-4c5e-83e0-5359d66d4df4.png" width="700">



8) 아래와 같이 dataset이 "Interaction data active"이 될때까지 기다립니다.

<img src="https://user-images.githubusercontent.com/52392004/191706361-9b5e5568-d267-4f10-bdbe-ba416c508f5d.png" width="700">

이후, 아래처럼 [Create solution]을 선택합니다.

<img width="700" alt="image" src="https://user-images.githubusercontent.com/52392004/191707034-603f4f7c-4cae-443a-97be-bd330cd930d9.png">


9) [Solution detail]에서 [Solution name]으로 "personalize-solution"으로 입력하고, [Solutions type]을 "Item recommendation"을 선택하고, [Recipe]로 "aws-user-personalization"을 선택합니다. 스크롤하여 [Create and train solution]을 선택합니다.

<img src="https://user-images.githubusercontent.com/52392004/191707727-d562944d-d0db-455f-8ab0-6adf851d8edd.png" width="700">

10) 약 20-30분후 Training이 완료되면, 배포를 위해 아래처럼 2번의 [Get recommendation]에서 [Create campaign]을 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/191763958-67ce1fe8-3901-4aa9-ad79-30a9e62f9745.png)

11) 아래와 같이 [Create new campaign] - [Campaign details]에서 [Campaign name]으로 "personalize-campaign"을 입력하고, Solution으로 기 생성한 "personalize-solution"을 선탁합니다. [Minimum provisioned transactions per second]은 Personalize에서 Inference 조회 요청에 대해 처리할수 있는 최대 TPS(Transaction per Second)를 의미하는데, 여기서는 편의상 5를 입력합니다. 이후에 아래로 스크롤하여 [Create campaign]을 입력합니다. 

12) Campagin이 생성되고 있는 것을 아래와 같이 Detail 탭에서 확인하실 수 있습니다. Campaign의 ARN을 아래와 같이 알 수 있습니다. 이 ARN은 getRecommendation API call를 호출할때 필요합니다. 

![noname](https://user-images.githubusercontent.com/52392004/191766859-c5c105f5-1a4f-41b0-aabf-1afd150283f3.png)
