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










## 입력데이터

1) User events/interactions 

- 반드시 입력되어야하는 기본 데이터입니다. 
- 조회수, 가입수, 전환수 등을 의미합니다. 

2) Item metadata 

- 가격, 세부정보, 제품명, 영화제목 등을 의미합니다.

3) User metadata
 
- 나이, 성별, 충성도, 멤버쉽 등을 의미합니다. 




배포는 campaign 

## 내부 동작

![image](https://user-images.githubusercontent.com/52392004/189830158-227c74ce-6b96-408d-837c-986392dfe67d.png)

- 알고리즘을 Recipe라고 하고 이것을 통해 훈련을 하게 되면 솔루션을 생성하게 됩니다. 

- Hyperparameter tuning은 기본적으로 off지만 on하여 사용할 수 있습니다.


## 알고리즘

Personalize에서 사용할 수 있는 알고리즘에는 아래와 같은 항목들이 있습니다. [Personalize Algorithm](https://github.com/kyopark2014/aws-personalize/blob/main/algorithm.md)에서 상세 알고리즘에 대해 설명합니다. 

아래는 Personalize에서 제공하는 Built-in Algorithm입니다. 

![image](https://user-images.githubusercontent.com/52392004/189832435-955dfdf8-12da-4213-9651-bf27a201b916.png)


## Workshop

[Peronalize Workshop](https://github.com/kyopark2014/aws-personalize/blob/main/workshop.md)에서는 실습할수 있는 예제를 제공하고 있습니다. 


## Reference

[Amazon Personalize recipes](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html)
