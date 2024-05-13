"""JAV Star Names Finder V2.12 GUI Version
Written by SangDo_Kim, a user in AVDBS.com
This Python GUI program reads file names in a folder which is containing JAV (Japanese Adult Video) files,
extract a product code from file names, and search a star name on Google UK search results
from AVDBS.com (one of the biggest JAV information site in South Korea)
It uses Pyside6 and its Designer. Converted py files from Designer were not changed by me.

이 파이썬 GUI 프로그램은 JAV(일본 야동) 파일이 포함된 폴더와 모든 하위 폴더의 파일 이름들을 읽은 후
출연자(여배우) 이름을 한글로 각 파일에 붙입니다. JAV 파일 이름은 품번(예: JEL-223)을 포함해야 합니다.
출연자 정보는 구글 영국에 저장된 AVDBS.com의 페이지 제목에서 읽어 옵니다.

유효한 JAV 파일 이름:
- [HD]JUL-222 유모 야동.mp4 (품번이 맨 앞에 있지 않아도 상관 없음)
- CutyGirl.JUL-222-Uncensored.srt (자막 파일이라도 상관 없음)
- JUL222 High Quality.mp4 (품번이 영문자가 2~3개이고 숫자가 3개인 경우 중간에 대시 '-'가 없어도 품번으로 인식)

유효하지 않은 파일 이름:
- 히마리 야동.mp4 (품번이 없음)
- 히마리 JUL 222.mp4 (품번 중간에 공백이 있으면 안 됨)

V1.12 변경 사항
- 출연자 구분자를 4개로 제한: "#", "^", "`", "출)"
   기존에 허용했던 구분자 "@", "$", ";"는 파일 이름에서 흔히 사용되므로 구분자로 쓰지 않기로 함.
- 품번 인식: 특수 문자(@, $, ', & 등)이 포함된 파일 이름에서 품번 인식을 제대로 하지 못함.
예) HD@JUL-333의 품번을 HDJUL-333으로 잘못 인식했음. 이를 JUL-333로 바로 잡음.

V1.13 변경 사항
- 품번 인식: 품번 뒤에 대시가 또 붙어 있는 경우 품번 인식 오류
   예) JUL-333-Uncensored.mp에서 품번을 JUL-333-으로 잘못 인식하던 것을 바로 잡음.
- 독립 실행 파일(EXE 파일)이 실행 안 되는 문제 해결(특정 모듈이 포함 안 됨)

V1.14 변경 사항: 품번 인식 개선

V1.15 변경 사항
- Tokyo-Hot-n3232, 550ENE-323 등 특수 품번 처리
- 새 출연자 추가 작업 시, 우선 품번이 있는지 확인한 다음 출연자 구분자가 있는지 점검하는 것으로 작업 순서 번경.

V2.0 변경 사항
- 명령 프롬프트 창에서 GUI로 변경(Pyside6 및 Designer 사용)
- JAV_prod_code 최신 버전으로 교체(품명 인식 개선)
- 변수 이름 명명 규칙 변경(스네이크 형태)
- 한국어만 지원(영어 제거)

V2.01 변경 사항
- 버그 잡기: 경로 선택 없이 출연자 검색 버튼을 누르면 프로그램 비정상 종료되던 문제 해결

V2.1 변경 사항
- 구글 검색 전 대기 시간 처리 부분을 기존 스레드에서 평범한 함수로 변경
- 정보 및 질문 대화 상자를 기존 QDialog에서 QMessageBox로 교제.
- 작업 결과 테이블 내용을 작업 시작 시 초기화함. 열 너비 조정.

V2.11 변경 사항
- 구글 검색 중 대기 시 진행 표시줄 표시

V2.12 변경 사항
- 설정 파일을 json 형식으로 변경
"""
import json
import os
import random
import time

import requests
from PySide6.QtCore import Qt, QMimeData, QThread, Signal, QTimer
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QDialog, QTableWidgetItem, QMessageBox
from bs4 import BeautifulSoup

from JAV_config import JAVConfig
from JAV_star_names_finder_ui import Ui_Form
from JAV_prod_code import JAV_prod_code, NoCodeError
from change_prev_separator import change_prev_separator, NoWorkError
from add_star_name import add_star_name, NoWorkError
from ask_question import ask_question


class MainWindow(QWidget, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # instance variables
        self.program_path = os.getcwd()
        self.request_no = 0
        self.request_failure_counter = 0

        # initial works
        self.JAV_config = JAVConfig()
        self.load_config_file()
        self.tableWidget.setColumnWidth(0, 55)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 315)
        self.tableWidget.setColumnWidth(3, 345)
        self.update_label_example_prev()
        self.update_label_example_new()
        self.label_status.setText("안녕하세요!")
        self.progressBar.hide()

        # push buttons
        self.pushButton.clicked.connect(self.select_path)
        self.pushButton_2.clicked.connect(self.change_prev_separator)
        self.pushButton_3.clicked.connect(self.search_stars)
        self.pushButton_4.clicked.connect(QApplication.exit)
        self.pushButton_5.clicked.connect(self.copy_to_clipboard)

        # combo boxes
        self.comboBox_position_prev.currentIndexChanged.connect(self.update_label_example_prev)
        self.comboBox_sep_prev.currentIndexChanged.connect(self.update_label_example_prev)
        self.comboBox_position_new.currentIndexChanged.connect(self.update_label_example_new)
        self.comboBox_sep_new.currentIndexChanged.connect(self.update_label_example_new)

    def select_path(self):
        dialog = QFileDialog()
        path = dialog.getExistingDirectory()
        if path in ("C:/", "C:/Windows", "C:/Program Files (x86)", "C:/Program Files"):
            QMessageBox.information(self, "알림",
                "C 드라이브 최상위 경로 또는 Windows 주요 폴더를 선택했습니다. "
                + "이러한 시스템 폴더에 대한 작업은 위험하므로 다른 경로를 선택해 주십시오.")
        elif path == "":
            self.label_work_path.setText(self.JAV_config.path_not_set)
        else:
            self.label_work_path.setText(path)

    def update_label_example_prev(self):
        if self.comboBox_position_prev.currentText() == "파일 뒷부분":
            self.label_example_prev.setText(f"예: URE-066 유) 상점가의 구멍 부인들 {self.comboBox_sep_prev.currentText()}미즈노 아사히")
        else:
            self.label_example_prev.setText(f"예: 미즈노 아사히{self.comboBox_sep_prev.currentText()} URE-066 유) 상점가의 구멍 부인들")

    def update_label_example_new(self):
        if self.comboBox_position_new.currentText() == "파일 뒷부분":
            self.label_example_new.setText(f"예: URE-066 유) 상점가의 구멍 부인들 {self.comboBox_sep_new.currentText()}미즈노 아사히")
        else:
            self.label_example_new.setText(f"예: 미즈노 아사히{self.comboBox_sep_new.currentText()} URE-066 유) 상점가의 구멍 부인들")

    def load_config_file(self):
        os.chdir(self.program_path)
        if self.JAV_config.load_from_file():
            self.comboBox_position_prev.setCurrentText(self.JAV_config.star_position)
            self.comboBox_position_new.setCurrentText(self.JAV_config.star_position)

            self.comboBox_sep_prev.setCurrentText(self.JAV_config.separator)
            self.comboBox_sep_new.setCurrentText(self.JAV_config.separator)

            self.label_work_path.setText(self.JAV_config.working_path)
        else:
            self.label_status.setText("기존 설정 파일 읽기 오류: 기존 설정 유지.")

    def change_prev_separator(self):
        if self.label_work_path.text() == self.JAV_config.path_not_set:
            QMessageBox.information(self, "알림",
                "먼저 작업 경로를 선택해 주십시오.")
            return None

        if (
                self.comboBox_position_prev.currentText() == self.comboBox_position_new.currentText()
                and self.comboBox_sep_prev.currentText() == self.comboBox_sep_new.currentText()
        ):
            QMessageBox.information(self, "알림",
                "기존 출연자 위치 및 구분자가 신규 설정과 동일하므로 작업할 내용이 없습니다.")
            return None

        answer = ask_question(self, "확인",
            "선택한 작업 경로 및 그 하위 폴더에 있는 모든 파일에 대해 기존 출연자 위치 및 구분자를 "
            "신규 설정으로 변경합니다. 이 작업을 진행하기 전에 Everything 등의 프로그램을 사용하여 혹시 기존 구분자가 "
            "잘못 들어가 있는 파일이 있는지 확인해 보기를 권장합니다.",
            "실행", "취소"
            )
        if not answer:
            return None

        self.save_config_file()
        file_no = -1  # Current working file number
        file_no_total = 0
        file_no_newly_changed = 0
        prod_code = ""
        prod_code_prev = ""
        file_base_name_new = ""
        file_replaced_no = 0

        # Get total number of files and set max row count of table object
        self.tableWidget.setRowCount(0)
        for (path, subfolders, files) in os.walk(self.label_work_path.text()):
            file_no_total += len(files)
        self.tableWidget.setRowCount(file_no_total)

        # Change file names based on new star position and separator
        for (path, subfolders, files) in os.walk(self.label_work_path.text()):
            for file_name in files:
                file_no += 1
                file_base_name, ext = os.path.splitext(file_name)
                if ext[1:].lower() not in JAV_prod_code.formats_video_sub:
                    self.tableWidget.setItem(file_no, 0, QTableWidgetItem("건너 뛰기"))
                    self.tableWidget.setItem(file_no, 1, QTableWidgetItem("비디오 또는 자막 파일이 아님."))
                    self.tableWidget.setItem(file_no, 2, QTableWidgetItem(file_name))
                    continue
                if len(file_base_name) <= 4:
                    self.tableWidget.setItem(file_no, 0, QTableWidgetItem("건너 뛰기"))
                    self.tableWidget.setItem(file_no, 1, QTableWidgetItem("파일 이름이 4자리 이하임."))
                    self.tableWidget.setItem(file_no, 2, QTableWidgetItem(file_name))
                    continue
                try:
                    prod_code = JAV_prod_code.get_prod_code(file_base_name)
                except NoCodeError:
                    self.tableWidget.setItem(file_no, 0, QTableWidgetItem("건너 뛰기"))
                    self.tableWidget.setItem(file_no, 1, QTableWidgetItem("파일 이름에서 품번을 찾을 수 없음."))
                    self.tableWidget.setItem(file_no, 2, QTableWidgetItem(file_name))
                    continue
                except IndexError:
                    self.tableWidget.setItem(file_no, 0, QTableWidgetItem("프로그램 오류"))
                    self.tableWidget.setItem(file_no, 1, QTableWidgetItem(
                        "인덱스 오류. 파일 이름을 개발자에게 알려주시면 프로그램을 수정하겠습니다."))
                    self.tableWidget.setItem(file_no, 2, QTableWidgetItem(file_name))
                    continue
                except ValueError:
                    self.tableWidget.setItem(file_no, 0, QTableWidgetItem("프로그램 오류"))
                    self.tableWidget.setItem(file_no, 1, QTableWidgetItem(
                        "값 오류. 파일 이름을 개발자에게 알려주시면 프로그램을 수정하겠습니다."))
                    self.tableWidget.setItem(file_no, 2, QTableWidgetItem(file_name))
                    continue
                else:
                    if file_base_name.find(self.comboBox_sep_prev.currentText()) < 0:
                        self.tableWidget.setItem(file_no, 0, QTableWidgetItem("건너 뛰기"))
                        self.tableWidget.setItem(file_no, 1, QTableWidgetItem("품번 있는 영상이지만 구분자 변경 작업 중에는 구글 검색 안 함."))
                        self.tableWidget.setItem(file_no, 2, QTableWidgetItem(file_name))

                if file_base_name.find(self.comboBox_sep_prev.currentText()) >= 0:  # 기존 구분자가 있는 파일 이름 변경
                    try:
                        file_base_name_new = change_prev_separator(
                            file_base_name, self.comboBox_position_new.currentText(),
                            self.comboBox_sep_new.currentText(),
                            self.comboBox_position_prev.currentText(),
                            self.comboBox_sep_prev.currentText()
                        )
                    except NoWorkError:
                        self.tableWidget.setItem(file_no, 0, QTableWidgetItem("건너 뛰기"))
                        self.tableWidget.setItem(file_no, 1, QTableWidgetItem(
                            "파일 이름에 기존 구분자가 있지만 문제가 있어 파일 이름을 바꾸지 않음."))
                        self.tableWidget.setItem(file_no, 2, QTableWidgetItem(file_name))
                        continue
                    except IndexError:
                        self.tableWidget.setItem(file_no, 0, QTableWidgetItem("프로그램 오류"))
                        self.tableWidget.setItem(file_no, 1, QTableWidgetItem(
                            "인덱스 오류. 파일 이름을 개발자에게 알려 주시면 프로그램을 수정하겠습니다."))
                        self.tableWidget.setItem(file_no, 2, QTableWidgetItem(file_name))
                        continue

                    full_path_prev = os.path.join(path, file_name)  # 기존, 현재 구분자 기준으로 파일 이름 변경
                    full_path_new = os.path.join(path, file_base_name_new + ext)
                    os.rename(full_path_prev, full_path_new)
                    self.tableWidget.setItem(file_no, 0, QTableWidgetItem("성공"))
                    self.tableWidget.setItem(file_no, 1, QTableWidgetItem("기존 구분자 교체"))
                    self.tableWidget.setItem(file_no, 2, QTableWidgetItem(file_name))
                    self.tableWidget.setItem(file_no, 3, QTableWidgetItem(file_base_name_new + ext))
                    file_replaced_no += 1
                    continue

        self.label_status.setText(
            f"작업 완료. 확인한 파일: {str(file_no + 1)}개. 기존 구분자 변경: {str(file_replaced_no)}개"
        )

        self.comboBox_position_prev.setCurrentText(self.comboBox_position_new.currentText())
        self.comboBox_sep_prev.setCurrentText(self.comboBox_sep_new.currentText())

    def save_config_file(self):
        self.JAV_config.star_position = self.comboBox_position_new.currentText()
        self.JAV_config.separator = self.comboBox_sep_new.currentText()
        self.JAV_config.working_path = self.label_work_path.text()
        os.chdir(self.program_path)
        self.JAV_config.save_to_file()

    def copy_to_clipboard(self):
        if self.tableWidget.rowCount() == 0:
            QMessageBox.information(self, "알림",
                "작업 내용이 없어서 클립보드로 복사할 수 없습니다.")
            return None

        # Create a QMimeData object to hold the data to be copied
        mime_data = QMimeData()

        # Get all the contents from the table
        contents = []
        for row in range(self.tableWidget.rowCount()):
            row_contents = []
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item is not None:
                    row_contents.append(item.text())
                else:
                    row_contents.append("")  # Empty cell
            contents.append(row_contents)

        # Convert list to text with '\t' and '\n'
        contents_text = '\n'.join('\t'.join(map(str, row)) for row in contents)
        contents_text = "작업\t작업 상세\t기존 파일 이름\t신규 파일 이름\n" + contents_text

        mime_data.setText(contents_text)
        # Get a reference to the clipboard and set the mime data
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mime_data)

        # Optionally, you can check if the data was successfully copied
        if clipboard.mimeData().hasText():
            QMessageBox.information(self, "알림",
                "작업 내용이 클립보드로 복사되었습니다.\n메모장 또는 엑셀에 붙여넣어 활용할 수 있습니다.")
        else:
            QMessageBox.information(self, "알림",
                "알 수 없는 이유로 클립보드로 복사되지 않았습니다.")

    def request_no_over_50_inform(self):
        QMessageBox.information(self, "알림",
            "웹 검색 횟수가 50회를 넘었습니다. "
            + "잠시 다른 일을 하다가 나중에 다시 시도하십시오(대략 몇 시간 후).")

    def search_stars(self):
        self.pushButton_3.setEnabled(False)
        self.save_config_file()

        if self.request_no > 50:
            self.request_no_over_50_inform()
            self.pushButton_3.setEnabled(True)
            return None

        if self.label_work_path.text() == self.JAV_config.path_not_set:
            QMessageBox.information(self, "알림",
                "먼저 작업 경로를 선택해 주십시오.")
            self.pushButton_3.setEnabled(True)
            return None
        self.label_status.setText("품번을 구글 영국에서 검색하여 새 출연자 추가 작업을 진행합니다.")
        file_no = -1  # Current working file number
        file_no_total = 0
        file_no_newly_changed = 0
        self.request_no = 0  # The number of the Internet search tries.
        prod_code = ""
        prod_code_prev = ""  # To check if the prod_code has been searched on the internet
        file_base_name_new = ""

        # Get total number of files and set max row count of table object
        self.tableWidget.setRowCount(0)
        for (path, subfolders, files) in os.walk(self.label_work_path.text()):
            file_no_total += len(files)
        self.tableWidget.setRowCount(file_no_total)

        # Check all files and search for JAV star on the Internet.
        for (path, subfolders, files) in os.walk(self.label_work_path.text()):
            for file_name in files:
                file_no += 1
                file_base_name, ext = os.path.splitext(file_name)
                if ext[1:].lower() not in JAV_prod_code.formats_video_sub:
                    self.tableWidget.setItem(file_no, 0, QTableWidgetItem("건너 뛰기"))
                    self.tableWidget.setItem(file_no, 1, QTableWidgetItem("비디오 또는 자막 파일이 아님."))
                    self.tableWidget.setItem(file_no, 2, QTableWidgetItem(file_name))
                    self.label_status.setText(f"{file_no}번 파일 처리.")
                    continue
                if file_base_name.upper().find("FC2") >= 0:
                    self.tableWidget.setItem(file_no, 0, QTableWidgetItem("건너 뛰기"))
                    self.tableWidget.setItem(file_no, 1, QTableWidgetItem("FC2 품번은 ABDBS에 등록되지 않음."))
                    self.tableWidget.setItem(file_no, 2, QTableWidgetItem(file_name))
                    self.label_status.setText(f"{file_no}번 파일 처리.")
                    continue
                if len(file_base_name) <= 4:
                    self.tableWidget.setItem(file_no, 0, QTableWidgetItem("건너 뛰기"))
                    self.tableWidget.setItem(file_no, 1, QTableWidgetItem("파일 이름이 4자리 이하임."))
                    self.tableWidget.setItem(file_no, 2, QTableWidgetItem(file_name))
                    self.label_status.setText(f"{file_no}번 파일 처리.")
                    continue

                # Get a product code from a file name.
                try:
                    prod_code = JAV_prod_code.get_prod_code(file_base_name)
                except NoCodeError:
                    self.tableWidget.setItem(file_no, 0, QTableWidgetItem("건너 뛰기"))
                    self.tableWidget.setItem(file_no, 1, QTableWidgetItem("파일 이름에서 품번을 찾을 수 없음."))
                    self.tableWidget.setItem(file_no, 2, QTableWidgetItem(file_name))
                    self.label_status.setText(f"{file_no}번 파일 처리.")
                    continue
                except IndexError:
                    self.tableWidget.setItem(file_no, 0, QTableWidgetItem("프로그램 오류"))
                    self.tableWidget.setItem(file_no, 1, QTableWidgetItem(
                        "인덱스 오류. 파일 이름을 개발자에게 알려 주시면 프로그램을 수정하겠습니다."))
                    self.tableWidget.setItem(file_no, 2, QTableWidgetItem(file_name))
                    self.label_status.setText(f"{file_no}번 파일 처리.")
                    continue
                except ValueError:
                    self.tableWidget.setItem(file_no, 0, QTableWidgetItem("프로그램 오류"))
                    self.tableWidget.setItem(file_no, 1, QTableWidgetItem(
                        "값 오류. 파일 이름을 개발자에게 알려 주시면 프로그램을 수정하겠습니다."))
                    self.tableWidget.setItem(file_no, 2, QTableWidgetItem(file_name))
                    self.label_status.setText(f"{file_no}번 파일 처리.")
                    continue

                if file_base_name.find(self.comboBox_sep_new.currentText()) >= 0:
                    self.tableWidget.setItem(file_no, 0, QTableWidgetItem("건너 뛰기"))
                    self.tableWidget.setItem(file_no, 1, QTableWidgetItem("이미 출연자 구분자 있음."))
                    self.tableWidget.setItem(file_no, 2, QTableWidgetItem(file_name))
                    self.label_status.setText(f"{file_no}번 파일 처리.")
                    continue

                # Search the star on the Internet.
                if prod_code != prod_code_prev:
                    # If web search failure occurs repeatedly
                    if self.request_failure_counter >= 7:
                        QMessageBox.information(self, "알림",
                            "품번 인터넷 검색 실패가 7회 이상 반복되고 있습니다. "
                            "구글이 차단했기 때문일 수도 있습니다. "
                            "차단했는데도 계속 검색을 시도하면 차단 시간이 길어지므로 "
                            "나중에 다시 시도하는 것을 권장합니다(대략 몇 시간 후). "
                            "몇 시간 후에도 여전히 차단될 경우 내일 다시 시도하면 될 가능성이 높습니다."
                            )

                        self.label_status.setText(
                            f"부분 작업 완료. 확인한 파일: "
                            + f"{str(file_no + 1)}개. 새로 출연자 추가: {str(file_no_newly_changed)}개. "
                            + f"구글 검색: {str(self.request_no)}번"
                        )
                        self.pushButton_3.setEnabled(True)
                        return None

                    if self.request_no > 50:
                        self.request_no_over_50_inform()
                        self.label_status.setText(
                            f"부분 작업 완료. 확인한 파일: {str(file_no + 1)}개. "
                            + f"새로 출연자 추가: {str(file_no_newly_changed)}개. "
                            + f"구글 검색: {str(self.request_no)}번."
                        )
                        self.pushButton_3.setEnabled(True)
                        return None

                    # Sleep for a few seconds to prevent Google's blocking
                    if self.request_no > 0:
                        wait_time = int(random.uniform(2000, 7000))
                        progress = 0
                        self.progressBar.show()
                        self.progressBar.setValue(0)
                        while progress <= wait_time:
                            time.sleep(0.1)
                            progress += 100
                            self.progressBar.setValue(
                                int((progress / wait_time) * 100)
                                )
                            self.label_status.setText(
                                "나 로봇 아님(아마도?). 잠깐 노는 중... {:.1f}초".format(
                                    abs((wait_time - progress) / 1000)
                                )
                            )
                            QApplication.processEvents()
                        self.progressBar.hide()
                        self.label_status.setText("작업 재개")

                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                      "(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
                    }
                    httpContents = requests.get(
                        "https://www.google.co.uk/search?q=" + prod_code + "%20AVDBS&gl=uk", headers=headers
                    )
                    self.request_no += 1
                    prod_code_prev = prod_code
                    soup = BeautifulSoup(httpContents.text, "html.parser")

                    # Check if Google blocks
                    warn_text_location = soup.text.find(
                        "detected unusual traffic")
                    if warn_text_location > 0:
                        QMessageBox.information(self, "알림",
                            f"웹 검색 오류: '일상적이지 않은 트래픽 발견', "
                            + f"구글 차단 알림 위치: {str(warn_text_location)} \n"
                            + f"구글 검색 수: {str(self.request_no)}, 현재 작업 파일: {file_name}\n"
                            + "반복적인 웹 검색으로 인해 구글이 이 프로그램을 로봇으로 생각하는 모양입니다. "
                            + "나중에 다시 시도하십시오(대략 몇 시간 후). "
                            + "몇 시간 후에도 여전히 차단될 경우 내일 다시 시도하면 될 가능성이 높습니다."
                            )
                        self.label_status.setText(
                            f"부분 작업 완료. 확인한 파일: {str(file_no + 1)}개. "
                            + f"새로 출연자 추가: {str(file_no_newly_changed)}개. "
                            + f"구글 검색: {str(self.request_no)}번"
                        )

                        self.request_failure_counter += 1
                        self.pushButton_3.setEnabled(True)
                        return None

                    web_title = soup.find("h3", "LC20lb MBeuO DKV0Md")
                    if web_title is None:
                        self.tableWidget.setItem(file_no, 0, QTableWidgetItem("실패"))
                        self.tableWidget.setItem(file_no, 1, QTableWidgetItem("품번 구글 검색 실패"))
                        self.tableWidget.setItem(file_no, 2, QTableWidgetItem(file_name))

                        self.label_status.setText(f"{file_no}번 파일 처리.")
                        self.request_failure_counter += 1
                        continue

                    # Thre are two type of AVDBS's title: type 1) BDA-179 모치즈키 아야카
                    # type 2) 시라토 하나 - APNS-246
                    if web_title.text.find(" - ") > 0:
                        web_star_name = web_title.text[:web_title.text.find(" - ")]
                        web_prod_code = web_title.text[web_title.text.find(" - ") + 3:]
                    else:
                        web_star_name = web_title.text[web_title.text.find(' ') + 1:]
                        web_prod_code = web_title.text[:web_title.text.find(" ")]

                    if len(web_prod_code) <= 4:
                        self.tableWidget.setItem(file_no, 0, QTableWidgetItem("실패"))
                        self.tableWidget.setItem(file_no, 1, QTableWidgetItem("품번 검색 실패"))
                        self.tableWidget.setItem(file_no, 2, QTableWidgetItem(file_name))

                        self.label_status.setText(f"{file_no}번 파일 처리.")
                        self.request_failure_counter += 1
                        continue

                    if prod_code != web_prod_code:
                        # It found something similar, but not exactly the same.
                        self.tableWidget.setItem(file_no, 0, QTableWidgetItem("실패"))
                        self.tableWidget.setItem(file_no, 1, QTableWidgetItem("정확히 일치하는 품번 검색 실패"))
                        self.tableWidget.setItem(file_no, 2, QTableWidgetItem(file_name))

                        self.label_status.setText(f"{file_no}번 파일 처리.")
                        self.request_failure_counter = 0
                        continue

                    self.request_failure_counter = 0

                # Attach the searched star name to the file name.
                star_name = web_star_name
                star_name = star_name.replace("/", "")
                star_name = star_name.replace(".", "")
                star_name = star_name.strip()

                if len(star_name) == 0:  # AVDBS에 출연자가 등록되지 않았거나 기타 다른 이유로 출연자 이름이 공백으로 나오는 경우
                    self.tableWidget.setItem(file_no, 0, QTableWidgetItem("실패"))
                    self.tableWidget.setItem(file_no, 1, QTableWidgetItem(
                        "출연자 이름이 AVDBS에 등록되지 않았거나 기타 이유로 검색 실패"))
                    self.tableWidget.setItem(file_no, 2, QTableWidgetItem(file_name))
                    self.label_status.setText(f"{file_no}번 파일 처리.")
                    continue

                # Change the file name
                file_base_name_new = add_star_name(
                    file_base_name, star_name,
                    self.comboBox_position_new.currentText(),
                    self.comboBox_sep_new.currentText()
                )
                full_path_prev = os.path.join(path, file_name)
                full_path_new = os.path.join(path, file_base_name_new + ext)
                os.rename(full_path_prev, full_path_new)

                self.tableWidget.setItem(file_no, 0, QTableWidgetItem("성공"))
                self.tableWidget.setItem(file_no, 1, QTableWidgetItem("출연자 추가"))
                self.tableWidget.setItem(file_no, 2, QTableWidgetItem(file_name))
                self.tableWidget.setItem(file_no, 3, QTableWidgetItem(file_base_name_new + ext))
                self.label_status.setText(f"{file_no}번 파일 처리.")
                file_no_newly_changed += 1

        # All the files are checked.
        self.label_status.setText(
            f"작업 완료. 확인한 파일: {str(file_no + 1)}개. 새로 출연자 추가: {str(file_no_newly_changed)}개. "
            + f"구글 검색: {str(self.request_no)}번."
            )
        self.pushButton_3.setEnabled(True)


app = QApplication()
main_window = MainWindow()
main_window.show()
app.exec()
