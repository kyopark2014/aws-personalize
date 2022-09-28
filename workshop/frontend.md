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

## CloudFront를 구성

아래와 같이 build를 수행합니다. 

```
npm install
npm run build
```

build 폴더에 아래 파일들이 생성됩니다. 

```c
-rw-rw-r-- 1 ec2-user ec2-user  869 Sep 28 18:47 asset-manifest.json
-rw-rw-r-- 1 ec2-user ec2-user 6148 Sep 28 18:46 .DS_Store
-rw-rw-r-- 1 ec2-user ec2-user 3870 Sep 28 18:46 favicon.ico
drwxrwxr-x 2 ec2-user ec2-user 4096 Sep 28 18:46 image
-rw-rw-r-- 1 ec2-user ec2-user 2425 Sep 28 18:47 index.html
-rw-rw-r-- 1 ec2-user ec2-user 5347 Sep 28 18:46 logo192.png
-rw-rw-r-- 1 ec2-user ec2-user 9664 Sep 28 18:46 logo512.png
-rw-rw-r-- 1 ec2-user ec2-user  492 Sep 28 18:46 manifest.json
-rw-rw-r-- 1 ec2-user ec2-user   67 Sep 28 18:46 robots.txt
drwxrwxr-x 4 ec2-user ec2-user 4096 Sep 28 18:47 static
```

이 파일들을 CloudFront에서 저징한 S3 bucket에 복사합니다. 

```c
aws s3 sync ./build s3://cf-simple-s3-origin-personalize-stack-123456789012
```

이후 CloudFront 주소로 접속하면 아래와 같이 보여집니다. 

![image](https://user-images.githubusercontent.com/52392004/192904233-2d10383e-cdc8-405a-b456-174539a7ec00.png)


## Reference 

[Amazon personalize with glue databrew front](https://github.com/aws-samples/amazon-personalize-with-glue-databrew-front)

[GroupLens Research](https://grouplens.org/datasets/movielens/)

[Workshop - Frontend 구성 실습](https://catalog.us-east-1.prod.workshops.aws/workshops/ed82a5d4-6630-41f0-a6a1-9345898fa6ec/ko-KR/prerequisites/frontend-setup/frontend-setup-lab)
