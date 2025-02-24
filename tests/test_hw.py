import os

from selene import browser, have, command


# успешная отправка формы со всеми заполненными полями
def test_form_submitted():
    browser.open("/")
    browser.element("#firstName").set_value("Maria")
    browser.element("#lastName").set_value("Lopez")
    browser.element("#userEmail").set_value("MLopez@gmail.com")
    browser.element('[for = "gender-radio-2"]').click()
    browser.element("#userNumber").set_value("0123456789")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click().element(
        'option[value="9"]'
    ).click()
    browser.element(".react-datepicker__year-select").click().element(
        'option[value="1996"]'
    ).click()
    browser.element(".react-datepicker__day--010").click()
    browser.element("#subjectsInput").type("Bio").press_enter()
    browser.element('[for = "hobbies-checkbox-2"]').click()
    browser.element('[for = "hobbies-checkbox-3"]').click()
    browser.element("#uploadPicture").send_keys(
        os.path.abspath("../images/unnamed.jpg")
    )
    browser.element("#currentAddress").type("Main street, 55 bld, 10 apt.")
    browser.element("#state").perform(command.js.scroll_into_view).click().element(
        "#react-select-3-option-3"
    ).click()
    browser.element("#city").click().element("#react-select-4-option-0").click()
    browser.element("#submit").click()

    # проверки
    browser.element("#example-modal-sizes-title-lg").should(
        have.exact_text("Thanks for submitting the form")
    )
    browser.all("//div[@class='table-responsive']//td[2]").should(
        have.exact_texts(
            "Maria Lopez",
            "MLopez@gmail.com",
            "Female",
            "0123456789",
            "10 October,1996",
            "Biology",
            "Reading, Music",
            "unnamed.jpg",
            "Main street, 55 bld, 10 apt.",
            "Rajasthan Jaipur",
        )
    )


# попытка отправки формы только с обяз. полями
def test_form_required_fields_only():
    browser.open("/")
    browser.element("#firstName").set_value("Maria")
    browser.element("#lastName").set_value("Lopez")
    browser.element("#gender-radio-2").click()
    browser.element("#userNumber").set_value("0123456789")
    browser.element("#submit").click()

    # проверки
    browser.element("#example-modal-sizes-title-lg").should(
        have.exact_text("Thanks for submitting the form")
    )
    browser.all("//div[@class='table-responsive']//td[2]").should(
        have.exact_texts(
            "Maria Lopez",
            "",
            "Female",
            "0123456789",
            "24 February,2025",
            "",
            "",
            "",
            "",
            "",
        )
    )


# попытка отправки формы без заполнения обязательных полей (не отправляем last name & number)
def test_form_error_required_fields_not_filled():
    browser.open("/")
    browser.element("#firstName").set_value("Maria")
    browser.element("#gender-radio-2").click()
    browser.element("#userNumber").set_value("0123456789")
    browser.element("#submit").click()

    # проверки
    browser.element("#userForm").should(have.attribute("class").value("was-validated"))


# попытка отправки формы c некорректным полем Mobile
def test_form_required_fields_but_wrong_number():
    browser.open("/")
    browser.element("#firstName").set_value("Maria")
    browser.element("#lastName").set_value("Lopez")
    browser.element("#gender-radio-2").click()
    browser.element("#userNumber").set_value("123456789")
    browser.element("#submit").click()

    # проверки
    browser.element("#userForm").should(have.attribute("class").value("was-validated"))
