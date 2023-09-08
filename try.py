from itertools import combinations_with_replacement, permutations
from sklearn.metrics.pairwise import cosine_similarity

# def get_value_to_one():
#     for task in tasks:
#         # Load the JSON file
#         for transformer in transformers:
#             with open(logs_path + '/' + task + '_#####_test_#####_' + transformer + '.json', "r") as f:
#                 json_preds = json.load(f)
                
#             for index, preds in json_preds.items():
#                 json_preds[index]['soft_label'] = {j: if for j, v in preds['soft_label'].items()}
                    
                    
#             # Save the dictionary as a JSON file
#             with open(logs_path + '/' + task + '_#####_test_#####_' + model + '_round_to_closes_value' +'.json', "w") as f:
#                 json.dump(json_preds, f, indent=2)

# def generate_possible_comb(combination_length = 4, target_sum=1):
#     value_list = [0.0, 0.16666666666666666, 0.3333333333333333, 0.5, 0.6666666666666666, 0.8333333333333334, 1.0]
#     valid_combinations = []

#     # Generate all combinations with replacement
#     combinations = combinations_with_replacement(value_list, combination_length)

#     # Filter combinations that sum up to the target sum
#     for combination in combinations:
#         if sum(combination) == target_sum:
#             valid_combinations.append(list(combination))

#     valid_combinations = sorted(valid_combinations)

#     return valid_combinations


    # def sorted_labels(preds):
    #     possible_values = [0.0, 0.16666666666666666, 0.3333333333333333, 0.5, 0.6666666666666666, 0.8333333333333334, 1.0]

    #     preds_list = []
    #     for label, value in preds.items():
    #         closes_label= min(possible_values, key=lambda x: abs(value - x))
    #         preds_list.append((label, value, abs (closes_label - value), closes_label))
            
    #     # Sort the list based on the third value of each tuple
    #     # sorted_data = sorted(preds_list, key=lambda x: x[2])
    #     sorted_data = sorted(preds_list, key=lambda x: x[3])
    #     return sorted_data

# def sample_close_values(preds, combination_length = 4, target_sum=1):
#     sorted_data = sorted_labels(preds)
#     possible_combs = generate_possible_comb(combination_length, target_sum)
    
#     ranked_data = {}
#     list_labels = []
#     for i, (label, value, diff, possible_value) in enumerate(sorted_data):
#         if i == 0:
#             ranked_data[label] = possible_value
#             # list_labels.append(possible_value)
#         else:
#             # list_labels.append(possible_value)
#             if (sum(ranked_data.values()) + possible_value) <= 1.0:
#                 ranked_data[label] = possible_value
#             else:
#                 for comb_labels in possible_combs:
#                     if list(ranked_data.values()) == comb_labels[:i]:
#                         print(ranked_data.values())
#                         print(comb_labels)
#                         print(i)
#                         ranked_data[label] = comb_labels[i]
#                         break
        
#     ranked_data = dict(sorted(ranked_data.items()))

#     return ranked_data

# def generate_possible_comb(combination_length = 4, target_sum=1):
#     value_list = [0.0, 0.16666666666666666, 0.3333333333333333, 0.5, 0.6666666666666666, 0.8333333333333334, 1.0]
#     valid_combinations = []

#     # Generate all combinations with replacement
#     combinations = combinations_with_replacement(value_list, combination_length)

#     # Filter combinations that sum up to the target sum
#     for combination in combinations:
#         if sum(combination) == target_sum:
#             valid_combinations.append(list(combination))

#     return valid_combinations


# def sorted_labels(preds):
#     possible_values = [0.0, 0.16666666666666666, 0.3333333333333333, 0.5, 0.6666666666666666, 0.8333333333333334, 1.0]

#     preds_list = []
#     for label, value in preds.items():
#         closes_label= min(possible_values, key=lambda x: abs(value - x))
#         preds_list.append((label, value, abs(closes_label - value), closes_label))
        
#     # Sort the list based on the third value of each tuple
#     sorted_data = sorted(preds_list, key=lambda x: x[2])
#     return sorted_data

# def sample_close_values(preds):
#     sorted_data = sorted_labels(preds)
#     ranked_data = {}
#     list_labels = []
#     for i, label, value, diff, possible_value in enumerate(sorted_data):
#         if i == 0:
#             ranked_data[label] = possible_value
#             list_labels.append(possible_value)
#         else:
#             list_labels.append(possible_value)
#             if sum(list_labels) < 0.9:
#                 ranked_data[label] = possible_value
#             else:
#                 ranked_data[label] = 0.0
        
#     ranked_data = dict(sorted(ranked_data.items()))

#     return ranked_data

# #################################
# def calculate_cosine_similarity(list1, list2):
#     # Reshape the lists to be 2D arrays with a single row
#     list1 = [list1]
#     list2 = [list2]

#     # Calculate cosine similarity
#     similarity = cosine_similarity(list1, list2)

#     return similarity[0][0]


# def remove_identical_lists(list_of_lists):
#     unique_lists = []

#     for sublist in list_of_lists:
#         # Convert the sublist to a tuple for hashability
#         sublist_tuple = tuple(sublist)

#         if sublist_tuple not in unique_lists:
#             unique_lists.append(sublist_tuple)

#     # Convert the unique lists back to lists
#     unique_lists = [list(sublist) for sublist in unique_lists]

#     return unique_lists

# def generate_possible_comb(task):
#     value_list = [0.0, 0.16666666666666666, 0.3333333333333333, 0.5, 0.6666666666666666, 0.8333333333333334, 1.0]
#     combination_length = {'task1': 2, 'task2': 3, 'task3': 5}
#     valid_combinations = []
#     perm_list = []
    
#     combinations = combinations_with_replacement(value_list, combination_length[task])
#     for combination in combinations:
#         if task != 'task3':
#             if sum(combination) == 1:
#                 valid_combinations.append(list(combination))
#         else:
#             valid_combinations.append(list(combination))
            
#     for list_values in valid_combinations:
#         permuts = permutations(list_values, combination_length[task])
#         for permut in permuts:
#             perm_list.append(list(permut))
            
#     return remove_identical_lists(perm_list)

# def sample_close_values(dict_preds , possible_preds):
#     pred_tuples = list(dict_preds.items())
#     value_list = []
#     key_list = []
#     for item in pred_tuples:
#         value_list.append(item[0])
#         key_list.append(item[1])
        
#     most_similar_pred = max(possible_preds, key=lambda x: calculate_cosine_similarity(value_list, x))
    
#     new_preds = {}
#     for i in range(len(dict_preds)):
#         new_preds[key_list[i]] = most_similar_pred[i]
        
#     return new_preds
    

import json
import config
import os

def count_instances(json_file):
    with open(json_file) as file:
        data = json.load(file)

    num_instances = len(data)

    return num_instances

folder = config.LOGS_PATH + '/results'

for path in os.listdir(folder):
    print('file:', path)
    print('Instances: ', count_instances(folder + '/' + path))