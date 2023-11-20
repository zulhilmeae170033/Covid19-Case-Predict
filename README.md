# COVID-19 Case Prediction Using Deep Learning in Malaysia

Introduction
The COVID-19 pandemic has posed a significant challenge to global health. Accurate prediction of new COVID-19 cases is crucial for implementing effective preventive measures and resource allocation. This project aims to develop deep learning models using LSTM neural networks to predict new COVID-19 cases in Malaysia.

## Objectives
Develop two deep learning models using LSTM neural networks for single-step window and multi-step window scenarios.
Utilize only the following features: cases_new, cases_import, cases_recovered, cases_active.
Achieve a Mean Absolute Percentage Error (MAPE) of less than 1% on the testing dataset.
Visualize training loss using TensorBoard.

## Model Specifications
Implement only LSTM, Dense, and Dropout layers in the models.
Determine the model depth based on performance optimization.
Adhere to the specified window size configurations:
Single-step window: input width of 30, output width of 30, offset of 1
Multi-step window: input width of 30, output width of 30, offset of 30

## Evaluation Criteria
Achieve a MAPE of less than 10% on the testing dataset.
Monitor training loss using TensorBoard.

## Results Example For :
### Single-Step (Predict new cases after 1 days)
<img width="336" alt="single_step_pred" src="https://github.com/zulhilmeae170033/Covid19-Case-Predict/assets/65061987/321842ad-662e-4abb-bf3f-cfb2942c337a">

### Multi-Step (Predict new cases after 30 days)
<img width="334" alt="multi_step_pred" src="https://github.com/zulhilmeae170033/Covid19-Case-Predict/assets/65061987/209bdc97-c02c-42c3-a0b2-eea356bb6d75">
