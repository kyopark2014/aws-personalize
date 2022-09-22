# Personalize Workshop

[AWS Personalize Workshop - DemoGo 2.0 Prime](https://catalog.us-east-1.prod.workshops.aws/workshops/ed82a5d4-6630-41f0-a6a1-9345898fa6ec/ko-KR)에 따라 personalize를 위한 데이터를 databrew를 이용해 preprocessing하고, api gateway와 lambda를 이용해 inference를 위한 api를 만들수 있습니다. 이때의 전체적인 Architecture는 아래와 같습니다.

![image](https://user-images.githubusercontent.com/52392004/189862404-fe5aa5a2-90fc-45eb-be61-9169878e70ab.png)

여기서 client로 cloud9을 사용합니다. 

## Glue DataBrew를 이용한 전처리 

[DataBrew를 이용한 Preprocessing](https://github.com/kyopark2014/aws-personalize/blob/main/databrew.md)에서는 parquet 파일을 열어서 불필요한 Column을 제거하고, 적절한 데이터 포맷으로 CSV 파일을 생성합니다. [생성된 파일의 예](https://github.com/kyopark2014/aws-personalize/blob/main/src/personalize-preprocessing-job_22Sep2022_1663810890438_part00000.csv)를 보면, "event_type"이 제거되어 있음을 알 수 있습니다. 

## Personalize Training과 Campaign 생성

[Personalize Training과 Campaign 생성](https://github.com/kyopark2014/aws-personalize/blob/main/training.md)에 따라, 전처리한 Dataset을 가지고 학습(Training)과 배포(Campaign)를 할 수 있습니다.

## Reference 

[AWS Personalize Workshop - DemoGo 2.0 Prime](https://catalog.us-east-1.prod.workshops.aws/workshops/ed82a5d4-6630-41f0-a6a1-9345898fa6ec/ko-KR)

[Amazon Personalize with Glue Databrew Front](https://github.com/aws-samples/amazon-personalize-with-glue-databrew-front)
