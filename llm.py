import requests

MODEL_NAME = "DeepSeek-V4-Flash"

def call_llm(model=MODEL_NAME, prompt="hello"):
    url = "https://llmservice.phfund.com.cn/xuanyuan/v1/chat/completions"
    headers = {'Authorization': 'Bearer ffwfewfgwDDfwefwefFWEWjlll198JFF',
                'content-type': 'application/json'}
    payload = {
                "model": model,
                "messages": [
                    {
                    "role": "user",
                    "content": prompt
                    }
                ],
                "temperature": 0.6,
                "stream": False
            }
    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=120
    )

    response.raise_for_status

    result = response.json()
    print(result)
    answer = result['choice'][0]['message']['content']
    print(answer)

if __name__ == "__main__":
    call_llm()
