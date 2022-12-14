# Glue DataBrew를 이용한 전처리 

[Amazon Personalize with Glue Databrew Front](https://github.com/aws-samples/amazon-personalize-with-glue-databrew-front)의 [demogoprime-click-source-data.parquet](https://github.com/kyopark2014/aws-personalize/blob/main/workshop/src/demogoprime-click-source-data.parquet)을 변환합니다. 이 파일의 내용은 아래와 같습니다.

```java
{"user_id":32,"item_id":27,"timestamp":870267583,"event_type":"click"}
{"user_id":24,"item_id":84,"timestamp":876141696,"event_type":"view"}
{"user_id":64,"item_id":59,"timestamp":886014096,"event_type":"click"}
{"user_id":48,"item_id":42,"timestamp":899817965,"event_type":"click"}
{"user_id":19,"item_id":4,"timestamp":895917658,"event_type":"view"}
{"user_id":38,"item_id":51,"timestamp":896500732,"event_type":"view"}
```

## 전처리 방법 

1) 소스 데이터인 [demogoprime-click-source-data.parquet](https://github.com/kyopark2014/aws-personalize/blob/main/workshop/src/demogoprime-click-source-data.parquet)을 적당한 곳에 다운로드 합니다.

2) [S3 Console](https://s3.console.aws.amazon.com/s3/buckets?region=ap-northeast-2)에 접속하여 Glue DataBrew에서 처리한 데이터를 저장할 bucket을 만듧니다. 여기서는 편의상 이름을 "personalize-dataset-ksp"로 하였습니다.

![noname](https://user-images.githubusercontent.com/52392004/191634610-173cb149-f1dd-4d60-8006-c4128ca41de0.png)


3) [AWS Glue DataBrew Console](https://ap-northeast-2.console.aws.amazon.com/databrew/home?region=ap-northeast-2#landing)에 접속하여 [Create project]를 선택합니다. 

4) [Project name]으로 "personalize-preprocessing"으로 입력하면, Recipe name도 자동으로 입력됩니다. 아래로 이동하여 [New dataset]을 선탁한후에 [File upload]와 [Choose file]을 선택한 후에, 다운로드한 parquet 파일을 업로드 합니다. 

![noname](https://user-images.githubusercontent.com/52392004/191629327-c0741d0a-6788-48f2-89a4-26b9ccc5400a.png)

5) 이후 아래와 같이 [Enter S3 destination]으로 기 생성한 "personalize-dataset-ksdyb"를 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/191634837-b3e2560c-27bd-41b1-bb98-8688f86bb0dc.png)


6) 아래로 스크롤하여 [Permissions]의 [Role name]에서 "Create new IAM role"을 선택한 후에 [New IAM role suffix]로 "personalize"라고 입력합니다. 이후 [Create project]를 선택합니다. 


7) 프로젝트가 생성되면 아래와 같이 [SCHEMA] - [Data type]을 선택하여, "user_id", "Item_id"은 string으로 "timestamp"은 long으로 변경합니다. 

![noname](https://user-images.githubusercontent.com/52392004/191635541-99f15b57-8ba2-467f-9550-e0b3ebc932aa.png)

변환을 하면 아래처럼 recipe가 등록됩니다. 

![noname](https://user-images.githubusercontent.com/52392004/191635849-aa4de627-836f-4896-a96d-51dd9ec47897.png)

8) 상단의 [GRID]를 선택하여 전체 데이터창으로 복귀합니다. Event Type 컬럼의 Filter 모양의 아이콘 [Column Filter] 을 클릭합니다.

![noname](https://user-images.githubusercontent.com/52392004/191636412-abd7fe72-348f-4f6f-8577-9e61b36f88ce.png)

아래처럼 "view"에 대한 필터링을 해제하고, [Add to receipe]을 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/191636766-9da62c02-c756-4136-97fc-c2b7592a089b.png)

9) "event_type"는 학습에서 사용되지 않으므로, 아래처럼 "event_type"을 선택하고, [COLUMN]을 선택한 후에 [Delete]를 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/191637389-52753ea2-5500-4998-9a0e-c67afe1eceb9.png)

이후 아래처럼 [Apply]를 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/191637169-9d20fe57-1f93-4031-8bf0-10192ccc9c4a.png)

결과적으로 아래처럼 receipe에 4개의 step이 등록되었습니다.

![image](https://user-images.githubusercontent.com/52392004/191637484-49f9785e-4a36-41ec-aac2-b480e885f451.png)

10) 좌측 메뉴의 [JOBS]를 선태한 후에 [Create job]에서 [Job name]으로 적당한 이름을 입력합니다. 여기서는 "personalize-preprocessing-job"으로 입력하였습니다. 이후 Output에서 "Amazon S3"와 "CSV"확인후에 아래처럼 [S3 location] - [Browse]를 하여, 기생성한 S3 Bucket을 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/191639332-e1355f79-8cc0-48c8-899d-bad3228ce026.png)

11) 아래로 스크롤하여 [Role name]으로, 이전 단계에서 생성한 "personalize"를 prefix로 가지는 Role을 선택합니다. 이후 [Create and run job]을 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/191639600-4ee46c2e-8660-4d72-a7ef-b6a763a484ee.png)

이후, [JOBS]에 가면 아래와 같은 DataBrew Job이 수행중임을 알수 있습니다. 

![noname](https://user-images.githubusercontent.com/52392004/191639866-2b30ccd2-a473-4409-bace-a1d0fa3b38c1.png)


12) Job이 완료가 되면 아래와 같이 S3에 CSV 파일이 생성됩니다. 


![image](https://user-images.githubusercontent.com/52392004/191640032-d7d761b7-c13b-4281-8361-4f4b2ac2bfcd.png)


[생성된 파일의 예](https://github.com/kyopark2014/aws-personalize/blob/main/workshop/src/personalize-preprocessing-job_22Sep2022_1663810890438_part00000.csv)를 보면, "event_type"이 제거되어 있음을 알 수 있습니다. 

## Reference

[AWS Personalize Workshop - DemoGo 2.0 Prime](https://catalog.us-east-1.prod.workshops.aws/workshops/ed82a5d4-6630-41f0-a6a1-9345898fa6ec/ko-KR)

[Amazon Personalize with Glue Databrew Front](https://github.com/aws-samples/amazon-personalize-with-glue-databrew-front)
