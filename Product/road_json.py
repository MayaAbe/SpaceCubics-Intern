import json
import parameters


# JSONファイルからmetadata辞書を読み取る関数
def list_to_tuple_recursive(data):
    if isinstance(data, list):
        return tuple(list_to_tuple_recursive(item) for item in data)
    elif isinstance(data, dict):
        return {key: list_to_tuple_recursive(value) for key, value in data.items()}
    else:
        return data


def load_metadata_from_json_with_tuple(json_path):
    try:
        with open(json_path, 'r') as f:
            metadata = json.load(f)
        return list_to_tuple_recursive(metadata)
    except FileNotFoundError:
        print(f"File {json_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {json_path}.")
        return None


if __name__ == "__main__":
    # 関数のテスト
    test_json_path = 'Product\metadata.json'
    loaded_metadata = load_metadata_from_json_with_tuple(test_json_path)
    print(loaded_metadata)
    print("\n-------------------------------\n")
    parameters.describe_metadata(loaded_metadata)