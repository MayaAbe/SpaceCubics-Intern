import json


# JSONファイルからmetadata辞書を読み取る関数
def load_metadata_from_json(json_path):
    """
    Read metadata from a JSON file and return it as a Python dictionary.
    
    Parameters:
        json_path (str): Path to the JSON file containing the metadata.
        
    Returns:
        dict: Metadata as a Python dictionary.
    """
    try:
        with open(json_path, 'r') as f:
            metadata = json.load(f)
        return metadata
    except FileNotFoundError:
        print(f"File {json_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {json_path}.")
        return None


# 関数のテスト
test_json_path = 'Product\metadata.json'
loaded_metadata = load_metadata_from_json(test_json_path)
print(loaded_metadata)