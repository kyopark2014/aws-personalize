# Personalize Training


1) [Personalize Console](https://ap-northeast-2.console.aws.amazon.com/personalize/home?region=ap-northeast-2#createDatasetGroup)로 진입하여, [Name]으로 "personalize-dataset"이라고 입력하고, 아래처럼 [Domain]으로 "Custom"을 선택합니다. 이후 [Create dataset group and continue]을 선택합니다. 

<img src="https://user-images.githubusercontent.com/52392004/191674302-1783ffe8-ad4d-4839-aa02-e490cfe18054.png" width="600">
 
2) 아래와 같이 [Configure interactions schema]에서 [Dataset name]을 "personalize-dataset"으로 하고, [Schema name]을 "personalize-shcema"로 설정합니다. 이후 아래로 스크롤하여 [Next]를 선택합니다. 

<img src="https://user-images.githubusercontent.com/52392004/191698093-450de98e-7b53-4223-af87-0d0c9484bd99.png" width="600">
 
3)  [Configure interactions dataset import job]에서 [Dataset import job name]으로 "personalize-import-job"을 입력합니다.

<img src="https://user-images.githubusercontent.com/52392004/191698972-c36ef22d-2b7f-457d-bfe3-f66e983f8ea1.png" width="600">

4) 아래로 스크롤하여 [IAM Role]에서 "Create a new role"을 선택합니다.


<img src="https://user-images.githubusercontent.com/52392004/191699699-b17b1434-8789-443b-bf6f-f3195d8af4a0.png" width="600">

이후 나오는 팝업에서 아래와 같이 [S3 buckets you specify]을 "Any S3 bucket"로 설정합니다. 

<img src="https://user-images.githubusercontent.com/52392004/191700496-9a41983a-7bc1-4f2a-9747-aa12f0ea74d6.png" width="600">

