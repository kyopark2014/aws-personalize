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

- 알고리즘을 Recipy라고 하고 이것을 통해 훈련을 하게 되면 솔루션을 생성하게 됩니다. 

- Hyperparameter tuning은 기본적으로 off지만 on하여 사용할 수 있습니다.

