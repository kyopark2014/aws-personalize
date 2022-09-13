# AWS Personalize

여기서는 AWS의 대표적인 Managed AI service인 AWS Personalize에 대해 소개합니다. 


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

#### [User personalization](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-new-item-USER_PERSONALIZATION.html)

- 상호 작용, 항목 및 사용자 데이터 세트를 기반으로 사용자가 상호 작용할 항목을 예측합니다.
- 영화 추천과 같이 좋아하는 아이템을 추천합니다. 

<img width="390" alt="image" src="https://user-images.githubusercontent.com/52392004/189833703-539cccc6-d0cc-45ca-86c7-e2688faab4e2.png">


#### [Similar Items](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-similar-items.html)

- 상호작용 데이터를 통해 유사 아이템 추천. 상품 탐색과 상세페이지 구성 시 활용합니다.

- 이전에 customer들이 보았던 아이템들을 보여줍니다.

<img width="458" alt="image" src="https://user-images.githubusercontent.com/52392004/189833900-6f06feff-68e0-4846-9698-9a459e6f5760.png">


#### [Personalized ranking](https://docs.aws.amazon.com/personalize/latest/dg/personalized-ranking-recipes.html)

- 소비자의 예측 관심도에 따른 순위로 추천 생성합니다.

<img width="494" alt="image" src="https://user-images.githubusercontent.com/52392004/189834433-9487b7e4-ebed-4859-8ec8-eb9da113f0e3.png">




![image](https://user-images.githubusercontent.com/52392004/189832435-955dfdf8-12da-4213-9651-bf27a201b916.png)


## Reference

[Amazon Personalize recipes](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html)
