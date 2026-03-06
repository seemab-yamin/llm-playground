# pip3 install transformers torch
# python3 deepseek_tokenizer.py
import transformers

chat_tokenizer_dir = "./"

tokenizer = transformers.AutoTokenizer.from_pretrained(
    chat_tokenizer_dir, trust_remote_code=True
)

result = tokenizer.encode("Hello!")
print(f"Result: {result}")
print(f"Result type: {type(result)}")
print(f"Result length: {len(result)}")
print(f"Result first element: {result[0]}")
print(f"Result last element: {result[-1]}")
print(f"Result first element type: {type(result[0])}")
print(f"Result last element type: {type(result[-1])}")
print(f"Result first element value: {result[0]}")
print(f"Result last element value: {result[-1]}")
