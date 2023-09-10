import streamlit as st
import summarizer

st.set_page_config(page_title="회의록 생성기", page_icon="image/notepad_yellow.png")


def main_page():
    st.markdown('입력하시는 내용을 바탕으로 간단한 회의록을 생성합니다.')
    st.write('\n')  # add spacing

    st.subheader("회의 내용을 입력해주세요.")
    with st.expander("회의 내용"):
        input = st.text_input("회의 내용을 입력해주세요.")
        if input:
            st.write(summarizer.get_meeting_note(input))


if __name__ == "__main__":
    main_page()
