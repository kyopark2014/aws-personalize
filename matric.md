# Personalize Matric

## Retrieving Metrics

Solution을 SDK를 통해 확인하는 방법입니다. 

```python
import boto3

personalize = boto3.client('personalize')

response = personalize.get_solution_metrics(
    solutionVersionArn = 'solution version arn')

print(response['metrics'])
```

이때의 결과의 예는 아래와 같습니다. 

```python
{
    "solutionVersionArn": "arn:aws:personalize:us-west-2:acct-id:solution/MovieSolution/<version-id>",
    "metrics": {
        "coverage": 0.27,
        "mean_reciprocal_rank_at_25": 0.0379,
        "normalized_discounted_cumulative_gain_at_5": 0.0405,
        "normalized_discounted_cumulative_gain_at_10": 0.0513,
        "normalized_discounted_cumulative_gain_at_25": 0.0828,
        "precision_at_5": 0.0136,
        "precision_at_10": 0.0102,
        "precision_at_25": 0.0091,
        "average_rewards_at_k": 0.653
    }
}
```

또는 [Console에서 Solutions and recipes]에 접속해서 아래와 같이 확인할 수 있습니다. 

![image](https://user-images.githubusercontent.com/52392004/192874179-c5bab921-b662-487b-9582-6792a1d857ab.png)

## Metric의 의미

#### coverage

An evaluation metric that tells you the proportion of unique items that Amazon Personalize might recommend using your model out of the total number of unique items in Interactions and Items datasets. To make sure Amazon Personalize recommends more of your items, use a model with a higher coverage score. Recipes that feature item exploration, such as User-Personalization, have higher coverage than those that don’t, such as popularity-count.

#### mean reciprocal rank at 25
An evaluation metric that assesses the relevance of a model’s highest ranked recommendation. Amazon Personalize calculates this metric using the average accuracy of the model when ranking the most relevant recommendation out of the top 25 recommendations over all requests for recommendations.

This metric is useful if you're interested in the single highest ranked recommendation.

#### normalized discounted cumulative gain (NCDG) at K (5/10/25)
An evaluation metric that tells you about the relevance of your model’s highly ranked recommendations, where K is a sample size of 5, 10, or 25 recommendations. Amazon Personalize calculates this by assigning weight to recommendations based on their position in a ranked list, where each recommendation is discounted (given a lower weight) by a factor dependent on its position. The normalized discounted cumulative gain at K assumes that recommendations that are lower on a list are less relevant than recommendations higher on the list.

Amazon Personalize uses a weighting factor of 1/log(1 + position), where the top of the list is position 1.

This metric rewards relevant items that appear near the top of the list, because the top of a list usually draws more attention.

#### precision at K
An evaluation metric that tells you how relevant your model’s recommendations are based on a sample size of K (5, 10, or 25) recommendations. Amazon Personalize calculates this metric based on the number of relevant recommendations out of the top K recommendations, divided by K, where K is 5, 10, or 25.

This metric rewards precise recommendation of the relevant items.

#### average_rewards_at_k
When you create a solution version (train a model) for a solution with an optimization objective, Amazon Personalize generates an average_rewards_at_k metric. The score for average_rewards_at_k tells you how well the solution version performs in achieving your objective. To calculate this metric, Amazon Personalize calculates the rewards for each user as follows:

rewards_per_user = total rewards from the user's interactions with their top 25 reward generating recommendations / total rewards from the user's interactions with recommendations

The final average_rewards_at_k is the average of all rewards_per_user normalized to be a decimal value less than or equal to 1 and greater than 0. The closer the value is to 1, the more gains on average per user you can expect from recommendations.

For example, if your objective is to maximize revenue from clicks, Amazon Personalize calculates each user score by dividing total revenue generated by the items the user clicked from their top 25 most expensive recommendations by the revenue from all of the recommended items the user clicked. Amazon Personalize then returns a normalized average of all user scores. The closer the average_rewards_at_k is to 1, the more revenue on average you can expect to gain per user from recommendations.

For more information see Optimizing a solution for an additional objective.

#### hit (hit at K)
If you trained the solution version with a USER_SEGMENTATION recipe, the average number of users in the predicted top relevant K results that match the actual users. Actual users are the users who actually interacted with the items in the test set. K is the top 1% of the most relevant users. The higher the value the more accurate the predictions.

#### recall (recall at K)
If you trained the solution version with a USER_SEGMENTATION recipe, the average percentage of predicted users in the predicted top relevant K results that match the actual users. Actual users are the users who actually interacted with the items in the test set. K is the top 1% of the most relevant users. The higher the value, the more accurate the predictions.




Dataset groups
## Reference

[Evaluating a solution version with metrics](https://docs.aws.amazon.com/personalize/latest/dg/working-with-training-metrics.html)
