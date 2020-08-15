# murid-mentor

This repository contains code for three different Machine-Learning APIs with replaceable models. These three apis are:

1. Student Financial Capacity API
2. Candidate Recommendation API
3. Job Recommendation API

Now a brief overview of each api with purpose and deployment infrastructure. Each api is hosted on Digital Ocean droplet. 

## Student Financial Capacity API
This api holds a model to predict the financial capacity of each student given his/her data. By financial capacity we mean: How much a student can afford to pay for educational expenses. We use this model
to come up with personalized financial-aid cum scholarship for each student. Thus each deserving student can study and grow. The hosted port for this api is **70**

## Candidate Recommendation API
This api holds a model which recommend a list of student candidates to an SME for a specific job. We make sure that each student is filtered for the job criteria and rank them for the best capability ,growth
potential and passion. This API holds all the placeholders to have differnt models running underneath. The hosted port for this api is **80**.

## Job Recommendation API
This api holds a model which recommend a list of jobs to a student. We make sure that each job is tailored to student's future goals, growth potential,  financial support and that the student fits the criteria.  This API holds all the placeholders to have differnt models running underneath. The hosted port for this api is **90**.
