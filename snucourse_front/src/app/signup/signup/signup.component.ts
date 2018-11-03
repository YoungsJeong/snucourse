import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../core/auth.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { CustomValidator } from './custom-validator';
import { LectureService } from '../../core/lecture.service';
import { Observable } from 'rxjs';
import {
  debounceTime,
  filter,
  switchMap,
  distinctUntilChanged,
  map,
  tap
} from 'rxjs/operators';
import { NgbTypeaheadConfig } from '@ng-bootstrap/ng-bootstrap';

@Component({
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {
  signUpForm: FormGroup;
  search;
  formatter;
  pending: boolean;
  error: any;
  constructor(
    private auth: AuthService,
    private fb: FormBuilder,
    private lecture: LectureService,
    private config: NgbTypeaheadConfig
  ) {
    // config.showHint = true;
    config.editable = false;
  }

  ngOnInit() {
    this.createForm();
    this.search = (text$: Observable<string>) =>
      text$.pipe(
        filter((text: string) => text && text.length > 1),
        debounceTime(10),
        distinctUntilChanged(),
        switchMap((text: string) => this.lecture.searchDepartment(text))
      );
    this.formatter = ({ name }) => name;
  }

  createForm() {
    this.signUpForm = this.fb.group(
      {
        email: [
          '',
          Validators.compose([Validators.email, Validators.required])
        ],
        name: ['', Validators.required],
        student_id: [
          '',
          Validators.compose([
            Validators.required,
            CustomValidator.validateStudentId
          ])
        ],
        major: [
          null,
          Validators.compose([
            Validators.required,
            CustomValidator.validateDepartment
          ])
        ],
        minor: [null, CustomValidator.validateDepartment],
        double_major: [null, CustomValidator.validateDepartment],
        password: [
          '',
          Validators.compose([
            Validators.required,
            CustomValidator.validatePassword
          ])
        ],
        confirmPassword: ['', Validators.required]
      },
      {
        validator: CustomValidator.validatePasswordMismatch,
        updateOn: 'change'
      }
    );
  }
  signUpRequest() {
    this.pending = true;
    this.error = false;
    const transformToInteger = Number.parseInt(
      this.formStudentId.value.replace('-', '')
    );
    const payload = {
      name: this.formName.value,
      student_id: transformToInteger,
      major: this.formMajor.value && this.formMajor.value.id,
      minor: this.formMinor.value && this.formMinor.value.id,
      double_major: this.formDoubleMajor.value && this.formDoubleMajor.value.id,
      email: this.formEmail.value,
      password: this.formPassword.value
    };
    this.auth.signup(payload).subscribe({
      complete: () => {
        this.pending = false;
      },
      error: () => {
        this.pending = false;
        this.error = true;
      }
    });
  }

  get formName() {
    return this.signUpForm.get('name');
  }
  get formEmail() {
    return this.signUpForm.get('email');
  }
  get formPassword() {
    return this.signUpForm.get('password');
  }
  get formConfirmPassword() {
    return this.signUpForm.get('confirmPassword');
  }
  get formMajor() {
    return this.signUpForm.get('major');
  }
  get formMinor() {
    return this.signUpForm.get('minor');
  }
  get formDoubleMajor() {
    return this.signUpForm.get('double_major');
  }
  get formStudentId() {
    return this.signUpForm.get('student_id');
  }
}
