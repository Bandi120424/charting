import openai
import config

openai.api_key = config.SECRET_KEY


def get_meeting_note(msg: str = "") -> str:
    DIRECTIONS = ["1. 내용 요약", "2. 해야할 일 나열",
                  "가능하다면, 다음 미팅에서 논의해야할 주요 내용들을 나열한다."]
    system_role = "\n".join(
        ["입력받은 회의 내용을 바탕으로 다음 지시사항에 따라 간단한 회의록을 작성한다", *DIRECTIONS])

    response = openai.ChatCompletion.create(
        model="gpt-4",
        #   prompt=(f"다음을 요약해줘:\n{msg}\n\nSummary:"),
        messages=[{"role": "system", "content": f"{system_role}"},
                  {"role": "user", "content": f"{msg}"}],
        temperature=0,
        max_tokens=200
    )
    return response.choices[0]["message"]["content"]
