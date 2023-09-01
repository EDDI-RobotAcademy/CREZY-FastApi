import pandas as pd
from collections import Counter

# def most_common_label(row):
#     emotion_columns = ['1번 감정', '2번 감정', '3번 감정', '4번 감정', '5번 감정']
#     emotions = row[emotion_columns].tolist()
#     most_common = Counter(emotions).most_common(1)[0][0]
#     if most_common == 'Fear' or most_common == 'fear':
#         return 0
#     elif most_common == 'Surprise' or most_common == 'surprise':
#         return 1
#     elif most_common == 'Angry' or most_common == 'angry':
#         return 2
#     elif most_common == 'Sadness' or most_common == 'sadness':
#         return 3
#     elif most_common == 'Neutral' or most_common == 'neutral':
#         return 4
#     elif most_common == 'Happiness' or most_common == 'happiness':
#         return 5
#     elif most_common == 'Disgust' or most_common == 'disgust':
#         return 6


files = ["4차년도", "5차년도", "5차년도_2차"]
result_data = []

for file in files:
    data = pd.read_csv(file + ".csv", encoding='cp949')

    result_data.append(data)

    # data['label'] = data.apply(most_common_label, axis=1)
    # output_file_name = file + "_labeled.xlsx"
    # data.to_excel(output_file_name, index=False)

result = pd.concat(result_data)

result.to_excel('result_labeled.xlsx', index=False)
