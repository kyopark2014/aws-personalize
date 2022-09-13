# AWS Personalize

여기서는 AWS의 대표적인 Managed AI service인 AWS Personalize에 대해 소개합니다. 

## 개인화 추천

고객의 특성에 기반에 개인화 추천을 제공하여 고객의 경험을 향상 시킬 수 있습니다. 

#### Content-based Filtering

컨텐츠 기반 필터링(Content-based Filtering)은 Item의 특성에 따라 유사한 Item을 구분하는것입니다. 전통적인 형태로 고객을 여러개의 집단으로 나누어 마케팅하는 방법입니다. 

#### Collaborative filtering 

협업필터링(Collaborative filtering)은 사용자(User)와 item의 상호 작용(interaction) 정보를 통해 user가 좋아할 만한 item을 추천하는것 입니다. 초개인화 추천에 적합한 형태로서 한 남성이 파란색의 티셔츠를 선택했다면, 이후에도 파란색의 아이템의 노출을 증가시키는 형태입니다. 이것은 A가 구매했던 제품을 B에게도 노출하는 User-based와, 텐트를 구매하였다면 이후에 침낭이나 버너를 노출하는것과 같은 item-based로 나누어집니다. 일반적으로 Item-based가 더 높은 효과를 보입니다. 


## Amazon Personalize 특징

#### New items in fast-changing catalogs

새로운 Item이 추가될때 과거의 상호 작용기록이 없으므로 개인화 설정이 어렵습니다(cold start). Amazon Personalize는 Catalog의 새항목과 이전항목에 대한 권장사항 간의 균형을 새항목 가중치(Item exploration weight)을 이용해 설정할 수 있습니다. 이것은 Interaction dataset과 item dataset의 비율을 조정할 수 있습니다. 

#### User segmentation

- 장르, 카테고리 또는 기타 항목 속성에 관심이 있는 사용자를 식별할 수 있습니다.

- 영화, 제품 등과 같은 특정 항목에 관심이 있는 사용자를 식별할 수 있습니다. (Item affinity)

#### Unlock information in unstructured text

가치 있는 신호는 종종 설명, 개요 및 리뷰에 갇혀 있을 수 있습니다. Amazon Personalize는 [자연어 처리(NLP)를 사용하여 구조화되지 않은 텍스트에서 주요 정보를 자동으로 추출](https://aws.amazon.com/ko/blogs/machine-learning/unlock-information-in-unstructured-text-to-personalize-product-and-content-recommendations-with-amazon-personalize/
)합니다.


## 입력 데이터 유형 (Dataset)

#### User events/interactions 

- Event는 사용자(User)의 활동을 의미합니다.
- User와 Item간의 상호작용에서 발생하는 과거 및 실시간 데이터를 저장하여 사용합니다.
- 개인화를 위한 매우 중요한 정보로서, 필수 Dataset 입니다. 
- 조회수, 가입수, 전환수 등을 의미합니다. 
- userId, ItemId, timestamp와 같은 데이터가 있을수 있습니다. 여기서 Item은 750k까지 등록할 수 있고, timestamp는 884182806과 같은 UNIX time format을 사용하여야 합니다. 

#### Item metadata 

- Item에 대한 세부정보를 가지고 있습니다. 
- 가격, 제품명, 영화제목 등을 의미합니다.

#### User metadata

- User에 대한 세부정보를 가지고 있습니다. 
- 나이, 성별, 고객 충성도, 멤버쉽 등을 의미합니다. 


## Personalize 동작

![image](https://user-images.githubusercontent.com/52392004/189830158-227c74ce-6b96-408d-837c-986392dfe67d.png)

1) 준비된 Dataset를 처리하기 위하여 준비된 group으로 묶고, 검사를 진행하고 의미있는것을 식별합니다.
2) Dataset의 특성에 맞게 적절한 알고리즘을 선택합니다. Personalize에서는 이러한 알고리즘을 Recipe라고 합니다. 
3) 개인화에 맞는 Recipe를 훈련하고 최적화하는 솔루션 형성 과정을 진행합니다. Personalize은 Hyperparameter tuning은 기본적으로 off하지만 on하여 사용할 수 있습니다.
4) 이후 campaign이라고 불리는 배포를 하게 됩니다.
5) 추천결과의 피드백을 event tracker를 이용해 반영할 수 있습니다.




## Algorithm

Personalize에서 사용할 수 있는 알고리즘에는 아래와 같은 항목들이 있습니다. [Personalize Algorithm](https://github.com/kyopark2014/aws-personalize/blob/main/algorithm.md)에서 상세 알고리즘에 대해 설명합니다. 

아래는 Personalize에서 제공하는 4가지 Recipe 유형의 19개 Built-in Recipe를 제공하고 있습니다. 

![image](https://user-images.githubusercontent.com/52392004/189832435-955dfdf8-12da-4213-9651-bf27a201b916.png)


## Campaign

솔루션을 지정 및 배포하여 캠페인을 생성합니다.

업데이트 방식에는 솔루션이 업데이트 될 때마다 가장 최신 버전의 솔루션으로 자동배포하는 방식과 updatecampaign을 call 해서 캠페인을 수동으로 업데이트하는 방식이 있습니다.

캠페인의 Status가 active로 변경 된 후 캠페인 작업 사용 가능합니다. 

API 형태로 이용되는데, TPS를 기준으로 비용이 청구가 되는데, [Creating a campaign](https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html)와 같이 AWS CLI와 SDK를 이용해 설정할 수 있습니다. 아래는 AWS CLI로 설정하는 예제입니다. 

```c
aws personalize create-campaign \
--name campaign name \
--solution-version-arn solution version arn \
--min-provisioned-tps 1 \
--campaign-config "{\"itemExplorationConfig\":{\"explorationWeight\":\"0.3\",\"explorationItemAgeCutOff\":\"30\"}}"
```

사용하는 Recipy에 따라 Campaign 호출시에 사용하는 API가 상이합니다. 

![image](https://user-images.githubusercontent.com/52392004/189916799-bdc7a6ed-78eb-41dd-b12e-ca3c4596e426.png)

## Inference

#### Real-time recommendation

Application에서는 GetRecommendations이나 GetPersonalizedRanking API를 통하여 원하는 추천기능을 동기방식으로 사용할 수 있습니다. 

또한, 시계를 검색하던 사용자가 구두를 검색하면 실시간 Interaction을 반영하여 시계와 관련된 Item을 추천할 수 있어야 합니다. 이와같이 실시간 피드백을 Event Tracker를 이용해 반영할 수 있는데, 이대, PutEvents를 이용합니다. 단, EventTracker는 User-Personalization, Personalized-Ranking recipes 경우에만 사용할 수 있습니다. 

![image](https://user-images.githubusercontent.com/52392004/189919241-526670d9-575b-42eb-ae95-b872dc7db253.png)


#### Batch recommendation

S3를 통해 데이터를 가져와서 Batch 작업을 할 수 있습니다. 

![image](https://user-images.githubusercontent.com/52392004/189919113-cd11ec85-1eb3-4162-abe3-b7248e071227.png)



## Workshop

[Peronalize Workshop](https://github.com/kyopark2014/aws-personalize/blob/main/workshop.md)에서는 실습할수 있는 예제를 제공하고 있습니다. 


## Reference

[Amazon Personalize recipes](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html)
