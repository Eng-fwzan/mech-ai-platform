import os 
import json 
from src.mechlib.core import load_json, save_json, ensure_dir 
 
def test_save_and_load_json(): 
    data = {"name": "Fawzan", "value": 42} 
    save_json("test.json", data) 
    loaded = load_json("test.json") 
    assert loaded == data 
 
def test_ensure_dir(): 
    ensure_dir("test_dir") 
    assert os.path.exists("test_dir") 
