# Amazon Personalize

AWS Personalizes는 AWS의 대표적인 Managed AI service입니다. Interaction, Item, User에 대한 데이터를 PutEvent, PutItem, PutUser를 하고, Solution을 Recipe로 생성한 후 Campaign을 배포합니다. 

![image](https://user-images.githubusercontent.com/52392004/227815579-9e9754f0-4790-401e-b37f-bc570d06b778.png)

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

### 데이터 포맷 

#### User events/interactions 

- Event는 사용자(User)의 활동을 의미하며, User와 Item 간의 인터랙션(Interaction) 정보를 제공합니다.
- User와 Item간의 상호작용에서 발생하는 과거 및 실시간 데이터를 저장하여 사용합니다.
- 개인화를 위한 매우 중요한 정보로서, 필수 Dataset 입니다. 
- 조회수, 가입수, 전환수 등을 의미합니다. 
- userId, ItemId, timestamp와 같은 데이터가 있을수 있습니다. 여기서 Item은 750k까지 등록할 수 있고, timestamp는 884182806과 같은 UNIX time format을 사용하여야 합니다. 

#### Item metadata 

- Item의 메타데이터 제공합니다. 
- 가격, SKU(상품 재고 관리 단위) 유형, 재고 여부와 같은 Item에 대한 세부정보를 가지고 있습니다.
- 가격, 제품명, 영화제목 등을 의미합니다.

#### User metadata

- 사용자에 대한 메타데이터 제공합니다.
- 개인화 시스템에 활용 가능한 연령, 성별, 고객 충성도, 기타 정보가 있습니다.
- User에 대한 세부정보를 가지고 있습니다. 

### 데이터 가져오기 

Personalize는 [comma-separated values (CSV) format을 import](https://docs.aws.amazon.com/personalize/latest/dg/data-prep-formatting.html) 할 수 있습니다. (parquet 미지원)
- 전체 대량 데이터 세트 가져오기

- 실시간 수집: PutEvents, PutItems, PutUsers와 같은 API를 통해 실시간으로 데이터 수집을 할 수 있습니다. 

- 증분 방식 (incremental bulk) 가져오기: [incremental bulk dataset imports](https://aws.amazon.com/about-aws/whats-new/2022/08/amazon-personalize-incremental-bulk-dataset-imports/?nc1=h_ls)와 같이 2022년 8월부터 증분방식의 데이터 가져오기를 제공합니다. Console에서 Add to existing data를 선택하거나, CreateDatasetImportJob API 작업에서 가져오기 모드를 INCREMENTAL로 지정하여 기존 데이터에 새로운 레코드를 추가할 수 있습니다.


## Personalize 동작

![image](https://user-images.githubusercontent.com/52392004/189830158-227c74ce-6b96-408d-837c-986392dfe67d.png)

1) 준비된 Dataset를 처리하기 위하여 준비된 group으로 묶고, 검사를 진행하고 의미있는것을 식별합니다.

2) Dataset의 특성에 맞게 적절한 알고리즘을 선택합니다. Personalize에서는 이러한 알고리즘을 Recipe라고 합니다. 

3) 개인화에 맞는 Recipe를 훈련하고 최적화하는 솔루션 형성 과정을 진행합니다. Personalize은 Hyperparameter tuning은 기본적으로 off하지만 on하여 사용할 수 있습니다.

4) 이후 campaign이라고 불리는 배포를 하게 됩니다.

5) 추천결과의 피드백을 event tracker를 이용해 반영할 수 있습니다.




## Algorithm

Personalize에서 사용할 수 있는 알고리즘에는 아래와 같은  항목들이 있습니다. [Personalize Algorithm](https://github.com/kyopark2014/aws-personalize/blob/main/algorithm.md)에서 상세 알고리즘에 대해 설명합니다. 

아래는 Personalize에서 제공하는 4가지 Recipe 유형의 19개 Built-in Recipe를 제공하고 있습니다. 알고리즘은 자동선택(AutoML)을 통해 손쉽게 설정이 가능합니다. 

![image](https://user-images.githubusercontent.com/52392004/189832435-955dfdf8-12da-4213-9651-bf27a201b916.png)

- HRNN(Hierachical Recurrent Neural Network): 사용자 행동이 시간에 따라 계속 변화하는 경우 사용합니다.
- HRNN-coldstart: 신규 아이템 추가가 빈번하고, 해당 아이템들이 추천 결과에 바로 반영되었으면 할때 적합합니다.
- HRNN-metadata: 높은 퀄리티의 메타데이터를 상요할 수 있을 경우에 메타데이터가 없는 경우보다 훨씬 더 좋은 결과를 얻습니다. 반연에 트레이닝 시간이 길어질 수 있습니다. 
- PersonalizeReranking: 사용자 각각에게 추천할 아이템의 순위를 쿼리를 이용하여 재정리합니다. 검색 결과 또는 선별된 목록의 개인화된 순위 변경에 사용됩니다.
- Popularity-baseline: Dataset 내에서 아이템의 출현횟수 계산 기준에 따라 Top-K popular items를 결과로 출력합니다. 여러 사용자에게 동일한 결과를 제공하며, 다른 알고리즘의 성능 비교 평가시 많이 활용됩니다.
- SIMS: Item-to-item 유사성활을하여 사용자 이력에서 동일하게 나타나는 아이템을 기반으로 유사 아이템 목록을 생성합니다. 아이템 검색 가능성을 개선하고, 디테일 페이지에서의 빠른 성능을 위해 사용합니다. 

## Campaign

- 솔루션을 지정 및 배포하여 캠페인을 생성합니다.

- 업데이트 방식에는 솔루션이 업데이트 될 때마다 가장 최신 버전의 솔루션으로 자동배포하는 방식과 UpdateCampaign을 call해서 캠페인을 수동으로 업데이트하는 방식이 있습니다. 

- 캠페인의 status가 active로 변경 된 후에 캠페인 작업 사용 가능(DescribeCampaign 참조)합니다. 

- 초당 최소 프로비저닝 트랜잭션 및 auto-scaling: GetRecommendations 또는 GetPersonalizedRanking의 실시간 트랜젝션 기능을 제공하고 있습니다. 초당 트랜젝션 수(TPS)는 Personalize의 청구의 기준중 하나 입니다. Provisioning된 최소 TPS(minProvisionedTPS)은 Provisioning한 기본 처리량을 지정하므로 최소 청구 요금을 지정하게 됩니다. TPS가 minProvisionedTPS이상이면 auto-scaling이 되지만, 짧은 시간이 용량이 급격하게 늘어나면 trasnsaction이 손실될 수 있습니다. TPS는 5분 동안의 평균 요청/초로 계산됩니다.

API 형태로 이용되는데, TPS를 기준으로 비용이 청구가 되는데, [Creating a campaign](https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html)와 같이 AWS CLI와 SDK를 이용해 설정할 수 있습니다. 아래는 AWS CLI로 설정하는 예제입니다. Campaign을 생성할때 min Provisioned TPS를 설정할 수 있습니다. 

```c
aws personalize create-campaign \
--name campaign name \
--solution-version-arn solution version arn \
--min-provisioned-tps 1 \
--campaign-config "{\"itemExplorationConfig\":{\"explorationWeight\":\"0.3\",\"explorationItemAgeCutOff\":\"30\"}}"
```

사용하는 Recipe에 따라 Campaign 호출시에 사용하는 API가 상이합니다. 

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

[Personalize Workshop](https://github.com/kyopark2014/aws-personalize/tree/main/workshop)에서는 실습할수 있는 예제를 제공하고 있습니다. 


## Reference

[Amazon Personalize recipes](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html)

[Deep Dive on Amazon Personalize](https://www.youtube.com/watch?v=dczs8cORHhg)

[Formatting your input data](https://docs.aws.amazon.com/personalize/latest/dg/data-prep-formatting.html)

[Amazon Personalize now supports incremental bulk dataset imports](https://aws.amazon.com/about-aws/whats-new/2022/08/amazon-personalize-incremental-bulk-dataset-imports/?nc1=h_ls)

[초당 최소 프로비저닝 트랜잭션 및 auto-scaling](https://docs.aws.amazon.com/ko_kr/personalize/latest/dg/campaigns.html)
