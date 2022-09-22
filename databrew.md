# Databrew를 이용한 전처리 

[Amazon Personalize with Glue Databrew Front](https://github.com/aws-samples/amazon-personalize-with-glue-databrew-front)의 [demogoprime-click-source-data.parquet](https://github.com/kyopark2014/aws-personalize/blob/main/src/demogoprime-click-source-data.parquet)을 변환합니다.

[demogoprime-click-source-data.parquet](https://github.com/kyopark2014/aws-personalize/blob/main/src/demogoprime-click-source-data.parquet)의 내용은 아래와 같습니다.

```java
{"user_id":32,"item_id":27,"timestamp":870267583,"event_type":"click"}
{"user_id":24,"item_id":84,"timestamp":876141696,"event_type":"view"}
{"user_id":64,"item_id":59,"timestamp":886014096,"event_type":"click"}
{"user_id":48,"item_id":42,"timestamp":899817965,"event_type":"click"}
{"user_id":19,"item_id":4,"timestamp":895917658,"event_type":"view"}
{"user_id":38,"item_id":51,"timestamp":896500732,"event_type":"view"}
```

1) 소스 데이터인 [demogoprime-click-source-data.parquet](https://github.com/kyopark2014/aws-personalize/blob/main/src/demogoprime-click-source-data.parquet)을 적당한 곳에 다운로드 합니다.

2) [AWS Glue DataBrew Console](https://ap-northeast-2.console.aws.amazon.com/databrew/home?region=ap-northeast-2#landing)에 접속하여 [Create project]를 선택합니다. 

3) [Project name]으로 "personalize-preprocessing"으로 입력하면, Recipe name도 자동으로 입력됩니다. 아래로 이동하여 [New dataset]을 선탁한후에 [File upload]와 [Choose file]을 선택한 후에, 다운로드한 parquet 파일을 업로드 합니다. 

![noname](https://user-images.githubusercontent.com/52392004/191629327-c0741d0a-6788-48f2-89a4-26b9ccc5400a.png)

4) 아래로 스크롤하여 [Permissions]의 [Role name]에서 "Create new IAM role"을 선택한 후에 [New IAM role suffix]로 "personalize"라고 입력합니다. 이후 [Create project]를 선택합니다. 

## Reference

[AWS Personalize Workshop - DemoGo 2.0 Prime](https://catalog.us-east-1.prod.workshops.aws/workshops/ed82a5d4-6630-41f0-a6a1-9345898fa6ec/ko-KR)

[Amazon Personalize with Glue Databrew Front](https://github.com/aws-samples/amazon-personalize-with-glue-databrew-front)
