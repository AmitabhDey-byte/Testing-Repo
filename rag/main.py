from transformers import pipeline

model = pipeline("text-generation", model='Qwen/Qwen3-Coder-Next')
response = model("Hello, how are you?", max_length=50)
print(response)    
