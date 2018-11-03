import { FormGroup, ValidationErrors, FormControl } from '@angular/forms';

export class CustomValidator {
  static validatePasswordMismatch(group: FormGroup): ValidationErrors {
    const pwd = group.get('password').value;
    const pwdConfirm = group.get('confirmPassword').value;
    if (pwd === '' || pwdConfirm === '') {
      return null;
    }
    return pwd === pwdConfirm ? null : { passwordMismatch: true };
  }

  static validateStudentId(control: FormControl): ValidationErrors {
    const { value } = control;
    if (!value || value === '') {
      return null;
    }
    const regExp = new RegExp('^[0-9]{4}-[0-9]{5}$');
    return regExp.test(value) ? null : { invalidStudentId: true };
  }

  static validatePassword(control: FormControl): ValidationErrors {
    const { value } = control;
    if (!value || value === '') {
      return null;
    }
    const regExp = new RegExp(
      '^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)[a-zA-Z\\d]{8,}$'
    );
    return regExp.test(control.value) ? null : { invalidPassword: true };
  }

  static validateDepartment(control: FormControl): ValidationErrors {
    const { value } = control;
    if (!value || value === '') {
      return null;
    }
    return value.id ? null : { invalidDepartment: true };
  }
}
