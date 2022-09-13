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

Personalize에서 사용할 수 있는 알고리즘에는 아래와 같은 항목들이 있습니다. [Personalize Algorithm](https://github.com/kyopark2014/aws-personalize/blob/main/algorithm.md)에서 상세 알고리즘에 대해 설명합니다. 

아래는 Personalize에서 제공하는 Built-in Algorithm입니다. 

![image](https://user-images.githubusercontent.com/52392004/189832435-955dfdf8-12da-4213-9651-bf27a201b916.png)


## Workshop

[Peronalize Workshop](https://github.com/kyopark2014/aws-personalize/blob/main/workshop.md)에서는 실습할수 있는 예제를 제공하고 있습니다. 


## Reference

[Amazon Personalize recipes](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html)
