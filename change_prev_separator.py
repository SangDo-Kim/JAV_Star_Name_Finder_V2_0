"""Change previous seperator V2.0
This module gets new file name string based on previous and new star position and seperator.
"""

class NoWorkError(Exception):
    pass


def change_prev_separator(
        file_base_name, star_position="파일 뒷부분", star_separator="#", star_position_prev="파일 뒷부분",
        star_separator_prev="출)"
        ):
    if len(file_base_name) <= 4:
        raise NoWorkError
    file_base_name_new = ""
    other_name = ""
    s = ""

    if star_separator_prev == "출)" and file_base_name.find(", 출)") >= 0:  #기존 구분자가 출)일 경우, '출)'도 있고, ', 출)'도 있음.
        star_separator_prev = ", 출)"

    if file_base_name.find(star_separator_prev) == -1:  #기존 구분자를 파일 이름에서 찾지 못한 경우
        raise NoWorkError

    if star_position_prev == "파일 뒷부분":  #기존 출연자 이름이 뒤에 붙은 경우
        iSepPosition = file_base_name.find(star_separator_prev)
        other_name = file_base_name[:iSepPosition].strip()
        star_name = file_base_name[iSepPosition + len(star_separator_prev):].strip()
    else:  #기존 출연자 이름이 앞에 붙은 경우
        iSepPosition = file_base_name.find(star_separator_prev)
        star_name = file_base_name[:iSepPosition].strip()
        other_name = file_base_name[iSepPosition + len(star_separator_prev):].strip()

    if len(other_name) <= 4 or len(star_name) < 1:  #분리된 파일 이름과 출연자 이름의 길이가 너무 짧으면 오류로 판단
        raise NoWorkError

    if star_position == "파일 뒷부분":  #출연자 이름을 뒤에 붙여야 할 경우
        if star_separator == "출)":
            file_base_name_new = other_name + " 출) " + star_name
        else:
            file_base_name_new = other_name + " " + star_separator + star_name
    else:
        if star_separator == "출)":
            file_base_name_new = star_name + " 출) " + other_name
        else:
            file_base_name_new = star_name + star_separator + " " + other_name

    return file_base_name_new


# 테스트 실행
if __name__ == "__main__":
    sample_file_names = [
        "JUL-322 출) 미즈노 아사히", "550ENE-323 #아오리", "FC2-PPV-3806605 출)이부키", "1P-072023-001",
        "Tokyo-Hot-n0588 출)킴", "032출)영수", "EUN#-232", "EUN영상JUL-333-한국어Uncensored", "ESFF231"]
    for i in range(len(sample_file_names)):
        try:
            print(sample_file_names[i], "\t|\t", change_prev_separator((sample_file_names[i])))
        except NoWorkError:
            print(sample_file_names[i], "\t|\t", "NoWorkError")
