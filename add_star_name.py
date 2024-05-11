"""Add star name V2.0
This module adds a star name to file name string based on new star position and separator.
"""

class NoWorkError(Exception):
    pass


def add_star_name(file_base_name, star_name, star_position="파일 뒷부분", star_separator="#"):
    file_base_name_new = ""
    if len(star_name) <= 0 or len(file_base_name) <= 4:
        raise NoWorkError

    if star_position == "파일 뒷부분":        #출연자 이름을 뒤에 붙여야 할 경우
        if star_separator == "출)":
            file_base_name_new = file_base_name + " 출) " + star_name
        else:
            file_base_name_new = file_base_name + " " + star_separator + star_name
    else:
        if star_separator == "출)":
            file_base_name_new = star_name + " 출) " + file_base_name
        else:
            file_base_name_new = star_name + star_separator + " " + file_base_name

    return file_base_name_new

# 테스트 실행
if __name__ == "__main__":
    print(f"[HD]MPA-334 유모|"
          + f"{add_star_name(
              "[HD]MPA-334 유모", "미아쟈키 하야오", "파일 뒷부분","#"
              )}"
          )

    print(f"[HD]MPA-334 유모|"
          + f"{add_star_name(
        "[HD]MPA-334 유모", "미아쟈키 하야오", "파일 앞부분", "출)"
    )}"
          )
