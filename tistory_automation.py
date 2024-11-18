def write_post():
    global driver
    initialize_driver()
    try:
        driver.get(WRITE_POST_URL)
        log_message("Navigated to Write Post page.")
        time.sleep(3)

        # 팝업 처리
        try:
            Alert(driver).accept()
            log_message("Popup detected and accepted.")
        except Exception:
            log_message("No popup detected.")

        # 제목 입력
        title_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "post-title-inp"))
        )
        title_input.clear()
        title_input.send_keys("111")
        log_message("Post title '111' entered.")

        # 내용 입력
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))  # iframe으로 전환
        body_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "tinymce"))
        )
        body_input.clear()
        body_input.send_keys("222")
        driver.switch_to.default_content()  # iframe에서 나옴
        log_message("Post content '222' entered.")

        # 글쓰기 버튼 자동 클릭
        try:
            write_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.publish_btn"))
            )
            write_button.click()
            log_message("'Write Post' button clicked successfully.")
        except Exception as e:
            log_message(f"Error clicking 'Write Post' button: {e}")

        # 공개 발행 옵션 선택
        try:
            radio_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "open20"))
            )
            if not radio_button.is_selected():
                radio_button.click()
            log_message("'Public Publish' option selected.")
        except Exception as e:
            log_message(f"Error selecting publish option: {e}")

        # 공개 발행 버튼 클릭
        try:
            publish_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "publish-btn"))
            )
            publish_button.click()
            log_message("'Publish' button clicked. Post published successfully.")
        except Exception as e:
            log_message(f"Error clicking 'Publish' button: {e}")

    except Exception as e:
        log_message(f"Error during write post: {e}")

# 종료 버튼 동작
def close_driver():
    global driver
    if driver:
        driver.quit()
        driver = None
        log_message("Chrome Driver closed.")
    else:
        log_message("No active Chrome Driver to close.")
