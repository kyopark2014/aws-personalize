# Movie 데이터를 보여주는 FrontEnd 만들기

아래와 같이 Personalize worhshop의 github에서 데이터를 다운로드 합니다. 

```c
git clone https://github.com/aws-samples/amazon-personalize-with-glue-databrew-front
cd amazon-personalize-with-glue-databrew-front
```

아래와 같이 Movie Table과 User Table을 DynamoDB에 넣습니다. 이때 사용한 데이터는 GroupLens Research에서 제공하는 [MovieLens Latest Small](https://grouplens.org/datasets/movielens/)입니다. 


```c
aws dynamodb batch-write-item --request-items file://User.json
aws dynamodb batch-write-item --request-items file://Movie.json
aws dynamodb batch-write-item --request-items file://Movie2.json
aws dynamodb batch-write-item --request-items file://Movie3.json
aws dynamodb batch-write-item --request-items file://Movie4.json
aws dynamodb batch-write-item --request-items file://Movie5.json
```
			
## Reference 

[Amazon personalize with glue databrew front](https://github.com/aws-samples/amazon-personalize-with-glue-databrew-front)

[GroupLens Research](https://grouplens.org/datasets/movielens/)

[Workshop - Frontend 구성 실습](https://catalog.us-east-1.prod.workshops.aws/workshops/ed82a5d4-6630-41f0-a6a1-9345898fa6ec/ko-KR/prerequisites/frontend-setup/frontend-setup-lab)
