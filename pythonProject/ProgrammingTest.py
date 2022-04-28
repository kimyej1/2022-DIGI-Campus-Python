import re

def checkValidationNameMobile(name, mobile):
    if re.findall("^[가-힣]{2,4}$", name):
        if re.findall("^010-\d{4}-\d{4}$", mobile):
            print("True")
            return True
        else:
            print("휴대폰번호를 확인하세요.")
            return False
    else:
        print("이름을 확인하세요.")
        return False

checkValidationNameMobile("김예지", "010-8978-6405")
checkValidationNameMobile("예지1", "010-8978-6405")
checkValidationNameMobile("yejikim", "010-8978-6405")
checkValidationNameMobile("김예지", "0108978-6405")
checkValidationNameMobile("김예지", "011-8978-6405")
checkValidationNameMobile("김예지", "010-978-63405")
checkValidationNameMobile("김예지", "010-8978e-김6405")