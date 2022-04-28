# 18RegularExpression.py

import re

def passwdValidationCheck(pwd):
    """
    비밀번호 유효성 검사하는 함수
    비밀번호에 영문, 숫자로 6~12자리만 OK
    영문에는 반드시 대문자와 소문자가 함께 포함되어야 한다.
    :param pwd:
    :return:
        True : if valid pwd
        False : if invalid pwd
    """

    # re.findall("[A-Za-z0-9]",pwd) → 결과값을 List로 줌
    if len(re.findall("^[A-Za-z0-9]{6,12}$",pwd)) == 0:
        print(pwd,"의 패턴이 잘못되었습니다.")
        return False

    if len(re.findall("[A-Z]",pwd)) == 0 or re.findall("[a-z]",pwd) == 0:
        print(pwd,'의 영문 대소문자가 섞여있지 않습니다.')
        return False

    print(pwd,'는 비밀번호로 적당합니다.')
    return True

# if __name__ === "__main__":
    passwdValidationCheck("asdA")
    passwdValidationCheck("asdA21234")
    passwdValidationCheck("asdA@D15")
    passwdValidationCheck("asda123")
    passwdValidationCheck("@asdA541$")

def checkEmailValidation(email):
    """
    이메일 패턴 [\w.-]+@[\w.-]+.\w+  --> 숫자문자,특문(.-)이 한번 이상
    :param email:
    :return:
        True : if valid email
        False : if invalid email
    """

    if re.findall("^[\w.-]+@[\w.-]+\.[\w]+$", email):
        print("True")
        return True
    else:
        print("False")
        return False

checkEmailValidation("yeji2501@gmail.com")
checkEmailValidation("hanmail.com")
checkEmailValidation("yeji@gmail.")
checkEmailValidation("yeji.-@gmail.com")
checkEmailValidation("y!d@h.c")
checkEmailValidation("y@h.c")
checkEmailValidation("y@df#.co")
checkEmailValidation("y@df.")
checkEmailValidation("y-@sda.dh5h")