from models import EmotionTest, RavenTest

def raven_test_key(model: RavenTest):
    right_answers = {
        "a_1": 4,
        "a_2": 5,
        "a_3": 1,
        "a_4": 2,
        "a_5": 6,
        "a_6": 5,
        "a_7": 1,
        "a_8": 3,
        "a_9": 4,
        "a_10": 2,
        "a_11": 3,
        "a_12": 6,
        "ab_1": 4,
        "ab_2": 5,
        "ab_3": 1,
        "ab_4": 6,
        "ab_5": 2,
        "ab_6": 5,
        "ab_7": 4,
        "ab_8": 3,
        "ab_9": 2,
        "ab_10": 3,
        "ab_11": 1,
        "ab_12": 6,
        "b_1": 4,
        "b_2": 1,
        "b_3": 3,
        "b_4": 6,
        "b_5": 5,
        "b_6": 4,
        "b_7": 1,
        "b_8": 3,
        "b_9": 2,
        "b_10": 5,
        "b_11": 2,
        "b_12": 6,
    }

    input_answers = {
        "a_1": model.a_1,
        "a_2": model.a_2,
        "a_3": model.a_3,
        "a_4": model.a_4,
        "a_5": model.a_5,
        "a_6": model.a_6,
        "a_7": model.a_7,
        "a_8": model.a_8,
        "a_9": model.a_9,
        "a_10": model.a_10,
        "a_11": model.a_11,
        "a_12": model.a_12,
        "ab_1": model.ab_1,
        "ab_2": model.ab_2,
        "ab_3": model.ab_3,
        "ab_4": model.ab_4,
        "ab_5": model.ab_5,
        "ab_6": model.ab_6,
        "ab_7": model.ab_7,
        "ab_8": model.ab_8,
        "ab_9": model.ab_9,
        "ab_10": model.ab_10,
        "ab_11": model.ab_11,
        "ab_12": model.ab_12,
        "b_1": model.b_1,
        "b_2": model.b_2,
        "b_3": model.b_3,
        "b_4": model.b_4,
        "b_5": model.b_5,
        "b_6": model.b_6,
        "b_7": model.b_7,
        "b_8": model.b_8,
        "b_9": model.b_9,
        "b_10": model.b_10,
        "b_11": model.b_11,
        "b_12": model.b_12,
    }

    bin_dict = {}

    for key, value in right_answers.items():
        if input_answers[key] != value:
            bin_dict[key] = 0
        else:
            bin_dict[key] = 1

    returned_dict = {} #{"a": sum_all_a, "ab": sum_all_ab, "b": sum_all_b,"sum": sum_all_a + sum_all_ab + sum_all_b}
    for key, value in bin_dict.items():
        if key.startswith("a_"):
            returned_dict["a"] = returned_dict.get("a", 0) + value
        elif key.startswith("ab_"):
            returned_dict["ab"] = returned_dict.get("ab", 0) + value
        elif key.startswith("b_"):
            returned_dict["b"] = returned_dict.get("b", 0) + value

    returned_dict["sum"] = returned_dict.get("a", 0) + returned_dict.get("ab", 0) + returned_dict.get("b", 0)

    return returned_dict


def emotions_test_key(model: EmotionTest):
    right_answers = {
        "e_1": "а",
        "e_2": "г",
        "e_3": "д",
        "e_4": "е",
        "e_5": "б",
        "e_6": "в"
    }

    input_answers = {
        "e_1": model.e_1,
        "e_2": model.e_2,
        "e_3": model.e_3,
        "e_4": model.e_4,
        "e_5": model.e_5,
        "e_6": model.e_6,
    }

    bin_dict = {}

    for key, value in right_answers.items():
        if input_answers[key] != value:
            bin_dict[key] = 0
        else:
            bin_dict[key] = 1

    returned_dict = {} # summ all
    for key, value in bin_dict.items():
        returned_dict["sum"] = returned_dict.get("sum", 0) + value
    return returned_dict



if __name__ == "__main__":
    model = EmotionTest(child_id=1,
                        e_1="u",
                        e_2="г",
                        e_3="д",
                        e_4="е",
                        e_5="б",
                        e_6="в")
    print(emotions_test_key(model, 1))
    
